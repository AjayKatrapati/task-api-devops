FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY run.py .

EXPOSE 5000

ENV FLASK_APP=run.py

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

