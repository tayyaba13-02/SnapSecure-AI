# Deployment Guide for Render.com

This guide explains how to deploy the **SnapSecureAI** project as a single Web Service on Render.com.

## Prerequisites
1. A GitHub account with this project pushed to a repository.
2. A [Render.com](https://render.com) account.

## Step 1: Push Changes to GitHub
Ensure you have committed and pushed the latest changes (including the new `Dockerfile` and `main.py` updates) to your GitHub repository.

```bash
git add .
git commit -m "Prepare for single-service deployment"
git push origin main
```

## Step 2: Create a Web Service on Render
1. Log in to your Render dashboard.
2. Click **New +** and select **Web Service**.
3. Connect your GitHub repository.
4. Select the repository containing `SnapSecureAI`.

## Step 3: Configure the Service
Configure the service with the following settings:

- **Name**: `snapsecure-ai` (or any name you prefer)
- **Region**: Choose one close to you (e.g., Oregon, Frankfurt)
- **Branch**: `main` (or your working branch)
- **Runtime**: **Docker** (This is important!)
- **Build Command**: (Leave blank, Render uses the Dockerfile automatically)
- **Start Command**: (Leave blank, Render uses the Dockerfile CMD automatically)
- **Instance Type**: **Free** (or Starter/Standard depending on needs)

## Step 4: Environment Variables
You shouldn't need strictly necessary env vars for the basic app to run, but if you have any secret keys or standard settings, add them under the **Environment** tab.

Render automatically provides a `PORT` variable, and our application is configured to listen on it.

## Step 5: Deploy
1. Click **Create Web Service**.
2. Render will start the build process.
   - It will clone your repo.
   - It will run the Docker build (creating the frontend build and setting up python).
   - It may take a few minutes (especially installing system dependencies like Tesseract).
3. Once the build finishes, you will see "Service is live".

## Step 6: Verify
Click the URL provided by Render (e.g., `https://snapsecure-ai.onrender.com`).
- You should see the React frontend.
- Upload an image to test the Analyze functionality.
