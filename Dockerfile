# Use an official Python runtime as the base image
FROM python:3.8-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY city_to_zip.py .

RUN pip3 install flask

RUN pip3 install requests

# Install the necessary packages for the program
RUN pip install --no-cache-dir flask

# Define environment variable
ENV FLASK_APP=city_to_zip.py

# Run the command to start the program
CMD ["flask", "run", "--host=0.0.0.0"]