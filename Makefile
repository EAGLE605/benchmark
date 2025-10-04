# Makefile for benchmark project

.PHONY: help install install-dev lint format type-check test test-coverage clean all check

help:  ## Show this help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

install:  ## Install production dependencies
	pip install -e .

install-dev:  ## Install development dependencies
	pip install -e .[dev]

lint:  ## Run linting checks
	@echo "Running flake8..."
	flake8 benchmark tests
	@echo "Running isort check..."
	isort --check-only benchmark tests
	@echo "Running black check..."
	black --check benchmark tests

format:  ## Format code with black and isort
	@echo "Formatting with black..."
	black benchmark tests
	@echo "Sorting imports with isort..."
	isort benchmark tests

type-check:  ## Run type checking with mypy
	@echo "Running mypy..."
	mypy benchmark

test:  ## Run tests
	@echo "Running tests..."
	pytest tests/ -v

test-coverage:  ## Run tests with coverage
	@echo "Running tests with coverage..."
	pytest tests/ -v --cov=benchmark --cov-report=term-missing --cov-report=html

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

check: lint type-check test  ## Run all checks (lint, type-check, test)

all: clean install-dev format check  ## Run complete setup and checks

# Development workflow targets
dev-setup: install-dev  ## Set up development environment
	@echo "Development environment set up successfully!"

ci-check: lint type-check test-coverage  ## Run CI checks with coverage