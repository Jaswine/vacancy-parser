
# Builder - Install dependencies
FROM python:3.10

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files
COPY pyproject.toml ${APP_HOME}/
COPY requirements.txt ${APP_HOME}/

# Install dependencies based on file availability     poetry install --no-root --no-interaction --no-ansi
RUN uv pip compile pyproject.toml -o requirements.txt \
    && uv pip install --system --no-cache -r requirements.txt

# Copy installed dependencies from builder
#COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
#COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . ${APP_HOME}

# Set Python path
ENV PYTHONPATH=/app/src

# CMD
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
