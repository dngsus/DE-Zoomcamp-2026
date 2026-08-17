# Start with image
FROM python:3.13.10-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /app

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files into image
COPY "pyproject.toml" "uv.lock" ".python-version" ./

# Install dependencies from lock file (ensures reproducible builds).
RUN uv sync --locked

# Copying of dependency files + running uv sync prior to copying of application code helps improved image layer caching

# Copy application code
COPY pipeline.py pipeline.py

# Set entry point
# See notes: 'uv run' is preferred, even if dropping it can still work, noting that we already specified the ENV PATH
ENTRYPOINT ["uv", "run", "python", "pipeline.py"]