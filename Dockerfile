# Use an official lightweight Python 12 image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements
# This command is often run in a single layer to make sure it's a single unit
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure gunicorn is in the path
# You can add a step to make sure the bin folder is in the PATH
# Or, you can use the absolute path to gunicorn
# For python:3.12-slim, the executable should be at /usr/local/bin/gunicorn

# Set the command to run the application using gunicorn
# The command 'agent:app' assumes your main file is 'agent.py' and your app object is named 'app'
CMD ["/usr/local/bin/gunicorn", "--bind", "0.0.0.0:$PORT", "--workers", "1", "--threads", "8", "agent:app"]