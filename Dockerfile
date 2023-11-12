FROM python:3.10.11-slim-buster

USER root
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg ca-certificates curl \
    libglib2.0-0 libnss3 libx11-6 \
    libx11-xcb1 libxcb1 libxcursor1 libxdamage1 \
    libxext6 libxfixes3 libxi6 libxrandr2 \
    libxrender1 libxss1 libxtst6 \
    libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libatk1.0-0 libc6 libcairo2 libcups2 \
    libdbus-1-3 libexpat1 libfontconfig1 libgcc1 \
    libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 \
    libnspr4 libpango-1.0-0 libpangocairo-1.0-0 \
    libstdc++6 libxcomposite1 libxdamage1 \
    libxinerama1 libxkbcommon0 libxkbfile1 \
    libxss1 libxtst6 xdg-utils \
    && apt-get clean && apt-get autoclean && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /z-app-core

COPY . .

# Install requirements
RUN pip3 install -r requirements.txt --no-cache-dir