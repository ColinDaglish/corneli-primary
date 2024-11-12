# Use the Python 3.12 slim bookworm image as the base image
FROM python:3.12-slim-bookworm

# Server port defaults to 8000 which is overridden during deployment builds.
ARG SERVER_PORT=8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_DIR=/usr/src/app

# Set the working directory in the container
# Set work directory.
WORKDIR ${APP_DIR}


# Install system packages
RUN apt-get update \
    && apt-get install -y \
    build-essential \
    curl

# Copy requirements to the container
COPY requirements.txt .

# Install app packages
RUN pip install --upgrade pip wheel setuptools \
    && pip install -r requirements.txt

# Copy the entire Django project into container according to .dockerignore
COPY . .
COPY deploy ${APP_DIR}/deploy/

# Make scripts executable.
RUN chmod +x ${APP_DIR}/deploy/*.sh && sed -i 's/\r$//g' ${APP_DIR}/deploy/*.sh

# Expose the port on which the Django app will run
EXPOSE ${SERVER_PORT}

