# Stage 1: Build
FROM python:3.10.11-slim-buster AS builder
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false --local
COPY  Dockerfile poetry.lock* pyproject.toml* /app/
RUN poetry install --no-root
COPY . /app/

# Stage 2: Runtime
FROM python:3.10.11-slim-buster
WORKDIR /app
COPY --from=builder /app/ /app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
