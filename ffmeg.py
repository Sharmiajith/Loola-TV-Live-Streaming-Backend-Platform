import subprocess

command = [
    "ffmpeg",
    "-re",
    "-i", "sample.mp4",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-f", "flv",
    "rtmp://localhost/live/test"
]

subprocess.run(command)
