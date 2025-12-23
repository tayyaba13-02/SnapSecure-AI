import pytest
from fastapi.testclient import TestClient
from main import app
import os
import io

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "SnapSecure AI API is running"}

def test_analyze_endpoint_no_file():
    response = client.post("/analyze")
    assert response.status_code == 422 # Validation Error

def test_analyze_endpoint_with_image():
    # Create a dummy image for testing
    from PIL import Image
    import numpy as np
    
    img = Image.fromarray(np.zeros((100, 100, 3), dtype=np.uint8))
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    files = {'file': ('test.png', img_byte_arr, 'image/png')}
    response = client.post("/analyze", files=files)
    
    # Even if OCR fails or finds nothing, the endpoint should return 200 if the flow finishes
    # Note: Tesseract might fail in this environment if not installed, but we test the API structure
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "success"
    assert "processed_url" in data
    assert "detections" in data
