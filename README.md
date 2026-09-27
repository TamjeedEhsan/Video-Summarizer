# AI Video Summarizer

An AI-powered video summarization application that analyzes uploaded videos, extracts representative frames, generates visual descriptions using a vision-language model, and produces a concise text summary of the video.

Built as a 24-hour hackathon project.

---

## Features

- Upload and process multiple videos
- Supports up to 10 videos per upload
- Extracts video frames using FFmpeg/OpenCV
- Generates frame-level descriptions using BLIP
- Combines visual information into a text summary using BART
- Displays generated summaries through a web interface
- Input validation and error handling
- Temporary file cleanup after processing
- FastAPI backend for video processing and AI inference
- JavaScript frontend for interacting with the backend

---

## How It Works

```text
                    ┌─────────────────┐
                    │   User Uploads  │
                    │     Video(s)    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ FastAPI Backend │
                    │   Validation    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ FFmpeg / OpenCV │
                    │ Frame Extraction│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      BLIP       │
                    │ Frame Captioning│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      BART       │
                    │ Text Summarizer │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Video Summary   │
                    │   Returned to   │
                    │    Frontend     │
                    └─────────────────┘
