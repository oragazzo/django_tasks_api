FROM python:3.12.8-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN apk add --no-cache \
    netcat-openbsd \
    gcc \
    python3-dev \
    postgresql-dev \
    postgresql-client \
    musl-dev \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip/*

# Copy project files
COPY . .

# Expose port
EXPOSE 8000 