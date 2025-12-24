# Deployment Guide for Hugging Face Spaces

This guide explains how to deploy **SnapSecureAI** as a Docker Space on Hugging Face. This method is free and does not require a credit card.

## Prerequisites
1. A [Hugging Face](https://huggingface.co/) account.

## Step 1: Create a New Space
1. Log in to Hugging Face.
2. Click on your profile icon (top right) and select **New Space**.
3. Fill in the details:
   - **Space Name**: `SnapSecureAI` (or any name provided).
   - **License**: `Apache 2.0` or `MIT` (optional).
   - **Sdk**: Select **Docker**.
   - **Space Hardware**: Keep it as **Default (Free)**.
   - **Privacy**: **Public** (recommended to easily share) or Private.
4. Click **Create Space**.

## Step 2: Push Your Code
Hugging Face Spaces use Git. You can either (A) Sync from your existing GitHub repo (if you set that up in Settings) or (B) Push directly to the Space's Git repo.

### Option A: Push to GitHub (Easiest if already set up)
If you already have a GitHub repo, you can just push your changes there.
However, to deploy *this* code to the *Space*, you usually need to mirror it or push specifically to the Space's remote.

### Option B: Push Directly to Hugging Face
The Space page will show you the git commands. It looks like this:

```bash
# Initialize git if not done
git init

# Add the Hugging Face remote (replace YOUR_USERNAME and SPACE_NAME)
git remote add space https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME

# Pull (to get .gitattributes if any)
git pull space main

# Add files
git add .
git commit -m "Deploy to Hugging Face"

# Push to the Space
git push space main
```

## Step 3: Wait for Build
1. Once you push, the "App" tab in your Space will show "Building".
2. Click "Logs" to watch the Docker build process.
3. Once finished, it will change to "Running" and your app will be visible in the window!

## Troubleshooting
- **Port**: The app must listen on port `7860`. We have already configured `main.py` and `Dockerfile` to do this.
- **Permissions**: If you see permission errors, ensure the Dockerfile is simple (which ours is).
