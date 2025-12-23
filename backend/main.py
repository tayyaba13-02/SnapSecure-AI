from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

@app.get("/")
async def root():
    return {"message": "SnapSecure AI API is running"}

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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
