# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
# CMD ["flask", "run"]


# Copy the Gunicorn configuration file
COPY gunicorn_config.py /app/gunicorn_config.py

# Command to run the Flask app with Gunicorn
CMD gunicorn --config gunicorn_config.py wsgi:app