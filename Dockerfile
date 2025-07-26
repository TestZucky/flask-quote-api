# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app/main.py"]
