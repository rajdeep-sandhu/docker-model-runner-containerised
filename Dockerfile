FROM python:3.13-slim

WORKDIR /app

# Install uv, copy files and sync project environment
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# Copy the rest of the app folder contents to WORKDIR
COPY app/ .

# Add environment to path
ENV PATH="/app/.venv/bin:$PATH"

# Set the default command
CMD ["streamlit", "run", "main.py"]