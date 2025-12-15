# Use official Python 3.9 image based on Alpine 3.13 for a lightweight environment
FROM python:3.9-alpine3.13

# Set maintainer label
LABEL maintainer="Chukwuebuka"

# Ensure Python output is sent straight to terminal (no buffering)
ENV PYTHONUNBUFFERED=1

# Copy main requirements file to temporary location
COPY ./requirements.txt /tmp/requirements.txt

# Copy development requirements file to temporary location
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Copy application source code to /app directory in container
COPY ./app /app

# Set working directory to /app
WORKDIR /app

# Expose port 8000 for application
EXPOSE 8000

# Define build argument to distinguish between dev and prod environments
ARG DEV=false

# Create Python virtual environment, upgrade pip, install dependencies,
# conditionally install dev dependencies, clean up temp files, and add a non-root user
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Adding postgres additional dependencies   and adapters
    apk add  --update --no-cache postgresql-client gcc python3-dev musl-dev libffi-dev && \
    apk add --no-cache --virtual .build-deps build-base postgresql-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    # Remove build dependencies to reduce image size
    apk del .build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \ 
    django-user

# Add virtual environment's bin directory to PATH
ENV PATH="/py/bin:$PATH"

# Switch to non-root user for security
USER django-user