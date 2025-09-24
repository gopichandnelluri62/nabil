# Use an official lightweight Python 12 image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
# Note: This assumes your file is named 'requirements' with no extension
COPY requirements.txt

# Install any needed packages specified in requirements
RUN pip install --no-cache-dir -r requirements

# Copy the rest of the application code into the container
COPY . .

# Set the command to run the application using gunicorn
# The command 'agent:app' assumes your main file is 'agent.py' and your app object is named 'app'
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 "agent:app"