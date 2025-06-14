import runpod
import subprocess
import uuid
import os

OUTPUT_DIR = "/workspace/output"

def generate_video(prompt, duration=4, fps=16, resolution="576x1024"):
    video_name = f"{uuid.uuid4()}.mp4"
    output_path = os.path.join(OUTPUT_DIR, video_name)

    cmd = [
        "python", "worker_runpod.py",
        "--prompt", prompt,
        "--fps", str(fps),
        "--duration", str(duration),
        "--resolution", resolution,
        "--output", output_path
    ]

    subprocess.run(cmd, check=True)
    return output_path

def handler(event):
    inputs = event["input"]
    prompt = inputs.get("prompt", "a panda riding a bicycle")
    duration = inputs.get("duration", 4)
    fps = inputs.get("fps", 16)
    resolution = inputs.get("resolution", "576x1024")

    try:
        path = generate_video(prompt, duration, fps, resolution)
        return {"video_path": path}
    except Exception as e:
        return {"error": str(e)}

runpod.serverless.start({"handler": handler})
