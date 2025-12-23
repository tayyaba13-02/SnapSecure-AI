# SnapSecure AI - Backend

The core intelligence of SnapSecure AI, built with **FastAPI** and **Tesseract OCR**. This service handles high-precision detection and surgical blurring of sensitive data in screenshots.

##  Getting Started

### Prerequisites
- **Python 3.10+**
- **Tesseract OCR**: Must be installed on the host system.
  - Windows: [Download Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
  - Linux: `sudo apt-get install tesseract-ocr`

### Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Or `venv\Scripts\activate` on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server
Start the development server on port 8001:
```bash
python main.py
```
Or via uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

##  Features
- **OCR Engine**: Uses Tesseract with PSM 6 for high-accuracy screenshot text extraction.
- **Sensitive Detector**: Custom regex-based detection for Emails, Phone Numbers, CNIC/SSNs, and IP Addresses.
- **Redaction Engine**: Uses OpenCV for Gaussian blurring with sub-pixel precision.
- **Privacy First**: Temporary files are cleared after processing; no user data is stored persistently.

##  API Endpoints
- `POST /analyze`: Accepts an image file and returns detection coordinates and a processed image URL.
- `GET /processed/{filename}`: Serves the redacted (blurred) images.

## Directory Structure
- `core/`: Contains the logic for OCR, Detection, and Redaction.
- `data/`: Temporary storage for uploaded and processed images.
- `tests/`: Automated test suite for detection patterns.
