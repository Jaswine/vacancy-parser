# Makefile

# Phony targets
.PHONY: help setup install \
        mypy format lint \
        run-api \
        clean


# Set the default goal to 'help' to list available commands
.DEFAULT_GOAL := help

# Help
help:
	@echo "Available Make Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}' | \
		sort


# === ENVIRONMENT AND DEPENDENCIES ===

setup: ## Setting up virtual environment
	@echo "🚀  Setting up virtual environment..."
	python3 -m venv .venv
	@echo "🚀  Installing pre-commit and activating git hooks..."
	pip install pre-commit
	run pre-commit install
	@echo "✅  Environment is set up. Activate with: source .venv/bin/activate"

install: ## Install dependencies
	@echo "🚀  Installing dependencies"
# 	pip install -r requirements.txt
    poetry install
	@echo "✅  Dependencies installed."


# === DATABASE MIGRATIONS (ALEMBIC) ===

db-init: ## Initialize alembic (only first time)
	@echo "🚀  Initializing Alembic..."
	alembic init alembic
	@echo "✅  Alembic initialized. Don't forget to edit alembic.ini and env.py!"

db-head: ## Bring Alembic up to the latest migration (head) without applying
	uv run alembic stamp head

db-current: ## Show current database migration version
	uv run alembic current

db-migrate: ## Create new migration based on models (requires message, e.g. make db-migrate m="init")
	@if [ -z "$(name)" ]; then echo "❌ Error: Use 'make db-migrate m=\"your_message\"'"; exit 1; fi
	@echo "🔄  Generating new migration..."
	uv run alembic stamp head
	uv run alembic current
	@bash -c 'set -a; source .env; set +a; PYTHONPATH=src uv run alembic revision --autogenerate -m "$(name)"'
	@echo "✅  Migration created."

db-upgrade: ## Apply all migrations to the database
	@echo "🚀  Upgrading database to head..."
	@bash -c 'set -a; source .env; set +a; PYTHONPATH=src alembic upgrade head'
	@echo "✅  Database is up to date."

db-downgrade: ## Rollback last migration
	@echo "🔄  Rolling back last migration..."
	@bash -c 'set -a; source .env; set +a; PYTHONPATH=src alembic downgrade -1'


# === Code Quality ===

mypy: ## Running mypy checks
	@echo "🔄  Running mypy checks..."
	pip install mypy
	python3 -m mypy src/
	@echo "✅  Type checking complete."

format: ## Formatting code using ruff
	@echo "🔄  Formatting code..."
	pip install ruff
	python3 -m ruff format .
	python3 -m ruff check --fix .
	@echo "✅  Formatting complete."

lint: ## Checking code f    ormatting for CI
	@echo "🔄  Checking code formatting..."
	pip install ruff
	python3 -m ruff format --check .
	@echo "🔄  Checking linting..."
	python3 -m ruff check .
	@echo "✅  All checks passed!"


# === RUN APPS ===

run-api:  ## Running api
	@echo "🚀  Starting Api..."
	@bash -c 'set -a; source .env; set +a; PYTHONPATH=src uv run uvicorn src.api.main:app --host 0.0.0.0 --port 8100 --reload'


# === DOCKER COMPOSE ДЛЯ РАЗРАБОТКИ ===

compose-up: ## Собрать и запустить все сервисы через Docker Compose
	@echo "Starting services with Docker Compose..."
	@cd infrastructure && docker-compose up --build

compose-down: ## Остановить и удалить контейнеры Docker Compose
	@echo "Stopping services..."
	@cd infrastructure && docker-compose down

compose-logs: ## Показать логи всех сервисов
	@echo "Showing logs..."
	@cd infrastructure && docker-compose logs -f

compose-build: ## Пересобрать образы без запуска
	@echo "Building Docker images..."
	@cd infrastructure && docker-compose build


# === CLEANING ===

clean: ## Remove all temporary Python files
	@echo "🦄  Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@find . -type d -name ".pytest_cache" -exec rm -r {} +
	@find . -type d -name ".mypy_cache" -exec rm -r {} +
	@find . -type f -name "*.pyc" -delete