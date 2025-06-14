FROM camenduru/hunyuan-video-temp:latest

WORKDIR /workspace/

COPY handler.py .
RUN pip install runpod

CMD ["python3", "handler.py"]