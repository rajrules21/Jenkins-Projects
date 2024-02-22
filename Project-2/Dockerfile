# Use the official Python image as base
FROM python:3.12-slim

# Set environment variables
ENV FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Command to run the Flask application
CMD flask run --host=0.0.0.0
