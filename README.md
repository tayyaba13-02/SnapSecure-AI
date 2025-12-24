---
title: SnapSecureAI
emoji: 🔒
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# SnapSecure AI 🛡️

**SnapSecure AI** is a professional, privacy-focused web application designed to surgically detect and blur sensitive data in screenshots. Whether it's an email, a phone number, or a government ID, SnapSecure AI ensures your personal information stays private before you share it.

##  Key Features
- **AI-Powered OCR**: Fast and accurate text extraction from images.
- **Surgical Redaction**: Precise Gaussian blurring that only hides what needs to be hidden.
- **Privacy First**: Secure processing with no persistent data storage.
- **Professional Design**: A modern, responsive interface built for speed and clarity.

##  Architecture
SnapSecure AI is split into two specialized components:
- **Backend (FastAPI)**: The intelligence layer for OCR and Image Processing.
- **Frontend (React)**: The intuitive user interface for seamless interaction.

##  Quick Start
To get the full system up and running:

### 1. Start the Backend
```bash
cd backend
# Create venv, install requirements.txt, and run
python main.py
```

### 2. Start the Frontend
```bash
cd frontend
# Install node packages (see frontend/README.md)
npm run dev
```

## Technologies
- **Backend**: Python, FastAPI, Tesseract OCR, OpenCV, Pillow.
- **Frontend**: React, Vite, Vanilla CSS.

---
Developed for secure screenshot sharing.
