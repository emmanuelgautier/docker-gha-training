# Using the latest stable version of Python with the slim image (optimized)
FROM python:slim

# Defining a non root working directory (good security practices)
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the application code
COPY . .

# start the application
CMD ["python", "app/main.py"]