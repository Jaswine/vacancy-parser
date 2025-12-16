
# Stage 1: Builder - Install dependencies
FROM python:3.10 as builder

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

COPY requirements.txt ${APP_HOME}
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --system --no-cache -r requirements.txt

# Copy application code
COPY . ${APP_HOME}

RUN python

# Set Python path
ENV PYTHONPATH=/app/src

# Run migrations
RUN alembic upgrade head

# CMD
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
