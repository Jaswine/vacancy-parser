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
	@echo "🚀 Setting up virtual environment..."
	python3 -m venv .venv
	@echo "🚀 Installing pre-commit and activating git hooks..."
	pip install pre-commit
	run pre-commit install
	@echo "✅ Environment is set up. Activate with: source .venv/bin/activate"

install: ## Install dependencies
	@echo "🚀 Installing dependencies"
	pip install -r requirements.txt
	@echo "✅ Dependencies installed."


# === Code Quality ===

mypy: ## Running mypy checks
	@echo "🔄 Running mypy checks..."
	@uv run mypy src/
	@echo "✅ Type checking complete."

format: ## Formatting code with using ruff
	@echo "🔄 Formatting code..."
	@uv run ruff format .
	@uv run ruff check --fix .
	@echo "✅ Formatting complete."

lint: ## Checking code formatting for CI
	@echo "🔄 Checking code formatting..."
	@uv run ruff format --check .
	@echo "🔄 Checking linting..."
	@uv run ruff check .
	@echo "✅ All checks passed!"

# === RUN APPS ===

run-api:  ## Running api
	@echo "🚀 Starting Api..."
	@bash -c 'set -a; source .env; set +a; PYTHONPATH=src uv run uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload'

# === CLEANING ===

clean: ## Remove all temporary Python files
	@echo "🦄 Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@find . -type d -name ".pytest_cache" -exec rm -r {} +
	@find . -type d -name ".mypy_cache" -exec rm -r {} +
	@find . -type f -name "*.pyc" -delete