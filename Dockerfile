# Use the official Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory inside the container
WORKDIR /app

# Enable bytecode compilation for improved startup performance
ENV UV_COMPILE_BYTECODE=1


# Copy the project's dependency files into the image
COPY pyproject.toml uv.lock /app/

# Install the project's dependencies using the lockfile
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application code into the image
COPY . /app

# Install the project itself
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Ensure the virtual environment's binaries are in the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Set the default command to run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]