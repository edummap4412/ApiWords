# Stage 1: Build
FROM python:3.10.11-slim-buster
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY api/app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]