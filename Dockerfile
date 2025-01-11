# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install system dependencies for audio handling and ffmpeg/ffprobe
RUN apt-get update && apt-get install -y \
    libasound2 \
    libasound2-dev \
    alsa-utils \
    pulseaudio \
    libffi-dev \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install ffmpeg and ffprobe
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz && \
    tar -xvf ffmpeg-release-amd64-static.tar.xz && \
    mv ffmpeg-*-amd64-static/ffmpeg /usr/local/bin/ && \
    mv ffmpeg-*-amd64-static/ffprobe /usr/local/bin/ && \
    chmod +x /usr/local/bin/ffmpeg /usr/local/bin/ffprobe && \
    rm -rf ffmpeg-release-amd64-static*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
