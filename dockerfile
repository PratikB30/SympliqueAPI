FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y --no-install-recommends wget unzip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN chmod +x /app/gunicorn.sh

EXPOSE 8000
ENV PORT=8000

CMD ["gunicorn", "—bind", "0.0.0.0:8000", "uvicorn.workers.UvicornWorker", "—-reload", "-k", "app:app" ]