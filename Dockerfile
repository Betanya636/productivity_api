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

# Copy templates and static assets (if used)
COPY templates/ ./templates/

# Expose port
EXPOSE 8000

# Run the Flask app from /src
CMD ["python", "src/app.py"]