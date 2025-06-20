FROM python:3.11-slim as base

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

FROM base as downloader
CMD ["python3", "main.py"]

FROM base as service
EXPOSE 5001
CMD ["python3", "server.py"]
