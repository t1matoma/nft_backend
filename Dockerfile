FROM python:3.13.7-slim

WORKDIR /app

# Устанавливаем зависимости для psycopg2 (Postgres драйвер)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "nft_game/manage.py", "runserver", "0.0.0.0:8000"]