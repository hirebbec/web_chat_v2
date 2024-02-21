FROM python:3.12

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY . .

ENV PORT=8000

EXPOSE $PORT

#CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
