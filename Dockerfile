# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY main.py /app/main.py

# Install any dependencies required by your Python script
# If your script has dependencies listed in a requirements.txt file, you can copy it and install dependencies
# COPY requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt

# Define the command to run your Python script when the container starts
CMD ["python", "main.py"]
