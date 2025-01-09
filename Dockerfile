# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Set the PORT environment variable (optional for local testing)
ENV PORT 8080

# Expose the port
EXPOSE 8080

# Start the app
CMD ["sh", "-c", "streamlit run main.py --server.port=$PORT --server.address=0.0.0.0"]

