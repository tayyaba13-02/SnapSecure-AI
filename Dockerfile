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
# Install system dependencies for Tesseract
# We use opencv-python-headless, so we don't need X11 libs.
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user

WORKDIR /app

# Copy backend requirements and install
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .
COPY --from=build-frontend /app/frontend/dist /app/frontend/dist

# Ensure the user owns everything (including the newly copied frontend files)
RUN mkdir -p /app/data/uploads /app/data/processed && chown -R user:user /app

# Switch to the "user" user
USER user

# Define environment variables
ENV PYTHONUNBUFFERED=1
ENV HOME=/home/user
ENV PATH=/home/user/.local/bin:$PATH

# Expose the port (Hugging Face Spaces uses 7860)
EXPOSE 7860

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
