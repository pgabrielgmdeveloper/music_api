FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
COPY . .

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]