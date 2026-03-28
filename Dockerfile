# ---------------------------------------
# Base Image
# ---------------------------------------
FROM python:3.10-slim

# Prevent Python from buffering stdout
ENV PYTHONUNBUFFERED=1

# ---------------------------------------
# Set Working Directory
# ---------------------------------------
WORKDIR /app

# ---------------------------------------
# Copy Requirements
# ---------------------------------------
COPY requirements.txt .

# ---------------------------------------
# Install Dependencies
# ---------------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ---------------------------------------
# Copy Project Files
# ---------------------------------------
COPY . .

# ---------------------------------------
# Expose Port for FastAPI
# ---------------------------------------
EXPOSE 7860

# ---------------------------------------
# Start FastAPI Server on HuggingFace
# ---------------------------------------
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
