FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Flask application code into the container
COPY . /app

# Install dependencies
RUN pip install Flask

# Copy the SQLite database file into the container
COPY loginapp.db /app

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
# Run the Flask application
CMD flask run --host=0.0.0.0
