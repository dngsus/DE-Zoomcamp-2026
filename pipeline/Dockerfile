# Start with image
FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
# Dependencies are all inside the pyproject.toml
RUN uv sync --locked
# We install all dependencies from lock file (ensures reproducible builds)


COPY ingest_data.py .
# This used to be pipeline.py

ENTRYPOINT ["uv", "run", "python", "ingest_data.py"]
# Entrypoint used to be just ["python", "pipeline.py"]
# Our new entrypoint makes it so the ingestion script runs first thing