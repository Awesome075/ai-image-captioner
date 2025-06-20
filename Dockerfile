FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit","run","image_captioner.py","--server.port=8501","--server.address=0.0.0.0"]