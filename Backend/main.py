from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import os
import shutil

from video_processor import extract_frames
from ai import generate_video_captions, generate_summary

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Video Summarizer backend is running!"
    }


@app.post("/upload")
async def upload_videos(
    videos: Annotated[list[UploadFile], File()]
):
    results = []

    upload_folder = "uploads"

    for video in videos:

        file_path = os.path.join(
            upload_folder,
            video.filename
        )

        # Save the uploaded video
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        # Extract frames from the video
        frame_folder = extract_frames(file_path)

        # Generate captions for the extracted frames
        captions = generate_video_captions(frame_folder)

        # Generate a summary from the captions
        summary = generate_summary(captions)

        results.append({
            "filename": video.filename,
            "summary": summary
        })

    return {
        "message": "Videos uploaded successfully!",
        "results": results
    }