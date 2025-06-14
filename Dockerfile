FROM camenduru/hunyuan-video-temp:latest

WORKDIR /content/HunyuanVideo/

# Vytvoř si vlastní handler pro RunPod
COPY handler.py .

# Nainstaluj runpod SDK
RUN pip install runpod

# Start point
CMD ["python3", "handler.py"]
