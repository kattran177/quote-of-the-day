# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the code into the container
COPY app.py .

# Install Flask
RUN pip install flask

# Command to run the app
CMD ["python", "app.py"]