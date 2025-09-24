# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Cloud Run injects the PORT environment variable.
# Your application must listen on this port.
# We modify the gunicorn command to use this variable.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 "main:app"