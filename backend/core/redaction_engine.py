import cv2
import numpy as np

class RedactionEngine:
    def __init__(self):
        pass

    def redact(self, image_path, detections, output_path):
        """
        Redacts detected sensitive regions in the image.
        :param image_path: Path to local image file
        :param detections: List of dicts with 'box' keys {'left', 'top', 'width', 'height'}
        :param output_path: Path to save processed image
        :return: output_path
        """
        try:
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"Could not load image at {image_path}")

            for item in detections:
                box = item['box']
                x, y, w, h = box['left'], box['top'], box['width'], box['height']
                
                # Region of Interest
                roi = img[y:y+h, x:x+w]
                
                # Apply Gaussian Blur
                # Kernel size must be odd. 
                # We scale kernel size with region size for effective blur on large text.
                k_w = (w // 3) | 1 # Ensure odd
                k_h = (h // 3) | 1 # Ensure odd
                
                # Cap minimum kernel size
                k_w = max(15, k_w)
                k_h = max(15, k_h)

                blurred_roi = cv2.GaussianBlur(roi, (k_w, k_h), 30)
                
                # Put back
                img[y:y+h, x:x+w] = blurred_roi
                
                # Optional: Add a border or label? 
                # For high security, black box is safer, but blur is prettier (asked in README).
                # README says: "Blur card numbers", "Hide passwords".
                
            # Save result
            cv2.imwrite(output_path, img)
            return output_path
            
        except Exception as e:
            print(f"Error during redaction: {e}")
            return None
