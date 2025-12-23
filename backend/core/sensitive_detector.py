import re

class SensitiveDetector:
    def __init__(self):
        self.patterns = {
            # Robust email pattern that handles double-at and common separators but requires a dot
            'EMAIL': r'\b[A-Za-z0-9._%+-]+(?:\s*[@]{1,2}\s*|\s*[\[\(]at[\]\)]\s*)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            # Surgical date exclusion for phone numbers (specifically ignores common year ranges 19xx/20xx)
            'PHONE': r'\b(?!(?:[\s.\-\/\\(]*\d{1,4}){2}[\s.\-\/\\(]*(?:19|20)\d{2}\b)(?:\+?(\d{1,3}))?[\s.\-\/\\(]*(\d{2,4})[\s.\-\/\\)]*(\d{2,4})[\s.\-\/\\]*(\d{4,6})\b',
            # Ultra-resilient CNIC structure (5-7-1) allowing common OCR digit and separator misreads (incl pars)
            'CNIC': r'\b[0-9\$S]{5}[\s.\-\/\\|()]{1,3}[0-9\$S]{7}[\s.\-\/\\|()]{1,3}[0-9\$S]{1}\b',
            'SSN': r'\b\d{3}[\-]?\d{2}[\-]?\d{4}\b',
            'IPV4': r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        }
        # Special case: map OCR misreads back to digits for regex (internal logic if needed)
        # For now, we stick to strict digit counts but will allow any separator

    def detect(self, ocr_results):
        """
        Analyzes OCR results and tags sensitive items.
        Uses a full-text matching strategy to detect items split across OCR blocks.
        """
        detected_items = []
        if not ocr_results:
            return detected_items

        # 1. Build full text and index map
        full_text = ""
        index_map = [] # List of (char_index, ocr_item_index)

        for i, item in enumerate(ocr_results):
            start_pos = len(full_text)
            text = item['text']
            full_text += text + " "
            for _ in range(len(text) + 1): # +1 for the space
                index_map.append(i)

        # 2. Run regex patterns on full text
        for type_name, pattern in self.patterns.items():
            for match in re.finditer(pattern, full_text):
                start, end = match.span()
                matched_text = full_text[start:end].strip()
                
                # Special handling for passwords to only blur the actual secret
                if type_name == 'PASSWORD' and match.groups():
                    # If regex has a capture group (the secret part), use its span
                    start, end = match.span(1)
                    matched_text = full_text[start:end].strip()

                # Trim match to avoid including trailing spaces in block mapping
                stripped_match = matched_text.strip()
                match_start_offset = matched_text.find(stripped_match)
                precise_start = start + match_start_offset
                precise_end = precise_start + len(stripped_match)

                # 3. Map back to OCR blocks
                # Find all blocks that overlap with this precise match
                affected_block_indices = sorted(list(set(index_map[precise_start:precise_end])))
                
                if not affected_block_indices:
                    continue

                # Calculate bounding box encompassing all affected blocks
                first_block = ocr_results[affected_block_indices[0]]
                left = first_block['left']
                top = first_block['top']
                right = first_block['left'] + first_block['width']
                bottom = first_block['top'] + first_block['height']

                for idx in affected_block_indices[1:]:
                    block = ocr_results[idx]
                    left = min(left, block['left'])
                    top = min(top, block['top'])
                    right = max(right, block['left'] + block['width'])
                    bottom = max(bottom, block['top'] + block['height'])

                detected_items.append({
                    'type': type_name,
                    'text': matched_text,
                    'box': {
                        'left': left,
                        'top': top,
                        'width': right - left,
                        'height': bottom - top
                    }
                })

        return detected_items
