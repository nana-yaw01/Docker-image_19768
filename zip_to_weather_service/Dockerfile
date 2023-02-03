# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Install required packages
RUN pip install Flask
RUN pip install requests

# Copy the local source code to the container
COPY . .

# Specify the command to run when the container starts
CMD ["python", "weather.py"]
