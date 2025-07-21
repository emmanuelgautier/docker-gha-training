# Use official Python image as base
FROM python:3.13.1-slim-bookworm

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Expose port (Flask default is 5000)
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask app
CMD ["poetry", "run", "python", "app/main.py"]
