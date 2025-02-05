FROM python:3.12.8-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y \
    netcat-traditional \
    gcc \
    python3-dev \
    libpq-dev \
    postgresql-client \
    && pip install -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Expose port
EXPOSE 8000 