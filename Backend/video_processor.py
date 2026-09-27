import subprocess
import os


def extract_frames(video_path):

    # Get the video filename without its extension
    video_name = os.path.splitext(
        os.path.basename(video_path)
    )[0]

    # Create a separate folder for this video's frames
    output_folder = os.path.join(
        "frames",
        video_name
    )

    os.makedirs(output_folder, exist_ok=True)

    # Output path for extracted frames
    output_path = os.path.join(
        output_folder,
        "frame_%03d.jpg"
    )

    # FFmpeg command
    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-vf",
        "fps=1",
        output_path
    ]

    subprocess.run(command)

    # Return the folder containing the extracted frames
    return output_folder