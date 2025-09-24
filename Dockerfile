# Dockerfile

# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file and install them
# This is done first to leverage Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the command to run the application using gunicorn
# Gunicorn is a professional-grade web server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]