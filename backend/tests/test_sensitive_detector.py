import pytest
from core.sensitive_detector import SensitiveDetector

@pytest.fixture
def detector():
    return SensitiveDetector()

def test_detect_email(detector):
    ocr_results = [
        {'text': 'Contact us at test@example.com', 'left': 10, 'top': 10, 'width': 100, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'EMAIL'
    assert detections[0]['text'] == 'Contact us at test@example.com'

def test_detect_phone(detector):
    ocr_results = [
        {'text': 'Call 123-456-7890', 'left': 10, 'top': 40, 'width': 100, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'PHONE'

def test_detect_credit_card(detector):
    # Test single block
    ocr_results = [
        {'text': '1234-5678-9012-3456', 'left': 10, 'top': 70, 'width': 200, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'CREDIT_CARD'

def test_detect_split_credit_card(detector):
    # Test split blocks (common in OCR)
    ocr_results = [
        {'text': '1234', 'left': 10, 'top': 70, 'width': 40, 'height': 20},
        {'text': '5678', 'left': 60, 'top': 70, 'width': 40, 'height': 20},
        {'text': '9012', 'left': 110, 'top': 70, 'width': 40, 'height': 20},
        {'text': '3456', 'left': 160, 'top': 70, 'width': 40, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'CREDIT_CARD'
    assert detections[0]['box']['width'] >= 190 # Should cover all blocks

def test_detect_cnic(detector):
    ocr_results = [
        {'text': 'CNIC: 12345-1234567-1', 'left': 10, 'top': 100, 'width': 150, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'CNIC'

def test_detect_ipv4(detector):
    ocr_results = [
        {'text': 'Server IP: 192.168.1.1', 'left': 10, 'top': 130, 'width': 150, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'IPV4'

def test_detect_password(detector):
    ocr_results = [
        {'text': 'Password:', 'left': 10, 'top': 160, 'width': 50, 'height': 20},
        {'text': 'secret123', 'left': 70, 'top': 160, 'width': 80, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'PASSWORD'
    assert detections[0]['text'] == 'secret123'

def test_detect_address(detector):
    ocr_results = [
        {'text': '123 Main St, New York, NY 10001', 'left': 10, 'top': 190, 'width': 300, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 1
    assert detections[0]['type'] == 'ADDRESS'

def test_no_sensitive_data(detector):
    ocr_results = [
        {'text': 'This is just a normal sentence.', 'left': 10, 'top': 220, 'width': 200, 'height': 20}
    ]
    detections = detector.detect(ocr_results)
    assert len(detections) == 0
