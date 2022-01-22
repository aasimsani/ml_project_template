# syntax=docker/dockerfile:1
FROM python:3.9
COPY deployment/requirements.txt app/
WORKDIR /app/
RUN pip install torch==1.9.0+cpu torchvision==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
RUN pip install -r requirements.txt
COPY deployment/* deployment/
# Customize the following line to import your own model
# COPY artifacts/model_weights/*.pt /app/artifacts/model_weights/
CMD ["uvicorn", "deployment.deploy:app","--host", "0.0.0.0", "--port", "8000"]