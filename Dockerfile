FROM python:3.13-slim

WORKDIR /app

# Install uv, copy files and sync project environment
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync

# Copy the rest of the app code
COPY . .

# Set the default command
CMD ["streamlit", "run", "main.py"]