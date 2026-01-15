FROM python:3.10-slim

LABEL maintainer="Chukwuebuka"

ENV PYTHONUNBUFFERED=1

# Copy requirements first (better caching)
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Set working directory consistently
WORKDIR /app
COPY ./app /app

EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        libffi-dev \
        python3-dev \
        postgresql-client \
    && /py/bin/pip install -r /tmp/requirements.txt \
    && if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi \
    && rm -rf /tmp/requirements* \
    && apt-get purge -y --auto-remove gcc python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m django-user && chown -R django-user:django-user /app

ENV PATH="/py/bin:$PATH"

USER django-user
