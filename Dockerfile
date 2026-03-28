FROM python:3.9.12-alpine3.15

EXPOSE 5000

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY wsgi.py .
COPY config.py .
COPY application application

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:$PORT wsgi:app"]