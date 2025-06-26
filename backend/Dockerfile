FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run migrations, collect static files, then run Gunicorn
CMD bash -c "python manage.py migrate --noinput && \
             python manage.py collectstatic --noinput && \
             gunicorn backend.wsgi:application --bind 0.0.0.0:8000"
