from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import os
import shutil
import uuid
from core.ocr_engine import OCREngine
from core.sensitive_detector import SensitiveDetector
from core.redaction_engine import RedactionEngine

app = FastAPI(title="SnapSecure AI API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory Setup (Assuming running from backend/ directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
UPLOADS_DIR = os.path.join(DATA_DIR, "uploads")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

# Ensure directories exist
os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Mount processed directory to serve images
app.mount("/processed", StaticFiles(directory=PROCESSED_DIR), name="processed")

# Initialize Engines
ocr_engine = OCREngine()
detector = SensitiveDetector()
redactor = RedactionEngine()

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/analyze")
async def analyze_screenshot(request: Request, file: UploadFile = File(...)):
    try:
        # 1. Save uploaded file
        filename = f"{uuid.uuid4()}_{file.filename}"
        file_path = os.path.join(UPLOADS_DIR, filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 2. OCR Detection
        ocr_results = ocr_engine.extract_text(file_path)
        
        # 3. Sensitive Data Detection
        detections = detector.detect(ocr_results)
        
        # 4. Redaction
        processed_filename = f"redacted_{filename}"
        processed_path = os.path.join(PROCESSED_DIR, processed_filename)
        
        output_path = redactor.redact(file_path, detections, processed_path)
        
        if not output_path:
            raise HTTPException(status_code=500, detail="Redaction failed")

        # 5. Return result
        # Construct URL dynamically using the request's base URL
        base_url = str(request.base_url).rstrip("/")
        processed_url = f"{base_url}/processed/{processed_filename}"
        
        return {
            "filename": filename,
            "status": "success",
            "processed_url": processed_url,
            "detections": detections, # Return details for frontend to show list
            "message": "Analysis completed successfully"
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

# Locate the frontend dist folder
# In Docker, we'll copy it to a known location like /app/frontend/dist
# Locally, it might be ../frontend/dist relative to backend/
FRONTEND_DIST = os.path.join(os.path.dirname(BASE_DIR), "frontend", "dist")
if not os.path.exists(FRONTEND_DIST):
    # Fallback for Docker structure if different
    FRONTEND_DIST = "/app/frontend/dist"

if os.path.exists(FRONTEND_DIST):
    # Mount assets (Vite builds into dist/assets by default)
    # We mount it to /assets so the frontend requests to /assets/index.js work
    app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIST, "assets")), name="assets")

    # Catch-all route for SPA
    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        # Allow requests to API endpoints to pass through if they weren't caught above
        # (Though simple strings wouldn't match specific paths unless defined after)
        # But @app.get("/") is specific.
        # Ideally, API routes are defined first (which they are).
        
        # If it's a file request that wasn't caught by assets or processed, check if it exists in dist root?
        # (e.g. favicon.ico)
        possible_file = os.path.join(FRONTEND_DIST, full_path)
        if os.path.isfile(possible_file):
             return FileResponse(possible_file)

        # Otherwise serve index.html
        return FileResponse(os.path.join(FRONTEND_DIST, "index.html"))

@app.get("/")
async def root():
    if os.path.exists(FRONTEND_DIST):
        return FileResponse(os.path.join(FRONTEND_DIST, "index.html"))
    return {"message": "SnapSecure AI API is running"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
