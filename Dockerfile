# Start from base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install pip, build, and wheel
RUN pip install --upgrade pip build

# Copy pyproject.toml and optional poetry.lock (if using poetry)
COPY pyproject.toml ./

# Install project dependencies
RUN pip install .

# Copy the rest of the code
COPY . .

# Run your application
CMD ["python", "app/main.py"]
