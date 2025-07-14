FROM python:3.11-slim

# Install libdmtx dependencies (updated: libdmtx0a → libdmtx0b)
RUN apt-get update && apt-get install -y \
    libdmtx0b \
    libdmtx-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Streamlit to run on port 8000 and expose it
EXPOSE 8000

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.enableCORS=false"]
