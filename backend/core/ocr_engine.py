import pytesseract
from PIL import Image
import cv2
import numpy as np

class OCREngine:
    def __init__(self, tesseract_cmd=None):
        """
        Initialize OCR Engine.
        :param tesseract_cmd: Optional path to tesseract executable.
        """
        # 1. Try provided path
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
            return

        # 2. Try default PATH (check if working)
        try:
            pytesseract.get_tesseract_version()
            return # It works from PATH
        except Exception:
            pass # Continue to search

        # 3. Try common Windows paths
        common_paths = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
            r"C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe"
        ]
        
        import os
        for path in common_paths:
            if os.path.exists(path):
                print(f"INFO: Found Tesseract at {path}")
                pytesseract.pytesseract.tesseract_cmd = path
                return

        print("WARNING: Tesseract not found in PATH or common locations. Please install it.")

    def extract_text(self, image_path, preprocess=True):
        """
        Extracts text and bounding boxes from an image.
        :param preprocess: Whether to apply image preprocessing for better OCR.
        """
        try:
            # Load image using OpenCV
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Could not load image at {image_path}")
                
            if preprocess:
                # 1. Grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # 2. Resize (Upscale 2x for better OCR on small text)
                height, width = gray.shape[:2]
                final_img = cv2.resize(gray, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)
            else:
                final_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Get data with bounding boxes
            # PSM 6 (Assume a single uniform block of text) works significantly better for screenshots
            custom_config = r'--psm 6'
            data = pytesseract.image_to_data(final_img, config=custom_config, output_type=pytesseract.Output.DICT)
            
            results = []
            n_boxes = len(data['text'])
            
            # Important: scale back coordinates if we upscaled
            scale = 2 if preprocess else 1
            
            for i in range(n_boxes):
                # Filter out empty text and low confidence
                text = data['text'][i].strip()
                conf = int(data['conf'][i])
                
                if text and conf > 0:
                    results.append({
                        'text': text,
                        'conf': conf,
                        'left': data['left'][i] // scale,
                        'top': data['top'][i] // scale,
                        'width': data['width'][i] // scale,
                        'height': data['height'][i] // scale
                    })
                    
            return results
            
        except Exception as e:
            print(f"Error during OCR: {e}")
            return []
