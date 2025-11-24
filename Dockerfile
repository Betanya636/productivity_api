# Use Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code folder
COPY src/ ./src/

# Expose the port your Flask app runs on (default 5000)
EXPOSE 5000

# Run the Flask app from /src
CMD ["python", "src/app.py"]
