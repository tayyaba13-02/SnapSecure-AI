# Stage 1: Build the React Frontend
FROM node:20-slim AS build-frontend
WORKDIR /app/frontend

# Copy package files and install dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy source code and build
COPY frontend/ .
RUN npm run build

# Stage 2: Setup the Python Backend
FROM python:3.10-slim

# Install system dependencies for Tesseract and OpenCV
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy backend requirements and install
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Copy built frontend assets from the previous stage
# We place them in /app/frontend/dist explicitly so main.py can find them at /app/frontend/dist
# Note: main.py expects: os.path.join(os.path.dirname(BASE_DIR), "frontend", "dist") 
# OR /app/frontend/dist fallback.
# Since WORKDIR is /app, and we copy backend/ content to /app, BASE_DIR (main.py's dir) is /app.
# So os.path.dirname(BASE_DIR) is /. 
# So it checks /frontend/dist. 
# BUT, we added a fallback in main.py: `if not os.path.exists... FRONTEND_DIST = "/app/frontend/dist"`
# So we should put it at /app/frontend/dist.

RUN mkdir -p /app/frontend/dist
COPY --from=build-frontend /app/frontend/dist /app/frontend/dist

# Define environment variables
ENV PYTHONUNBUFFERED=1

# Expose the port (Hugging Face Spaces uses 7860)
EXPOSE 7860

# Run the application
CMD ["python", "main.py"]
