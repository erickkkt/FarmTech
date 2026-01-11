# Multi-stage Dockerfile for FarmTech Platform
# This Dockerfile can build all components of the FarmTech platform
# Use docker-compose.yml for running the full stack

# Backend Stage
FROM python:3.9-slim as backend

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend

RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt /app/backend/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY backend/ /app/backend/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "farmtech_backend.wsgi:application"]
