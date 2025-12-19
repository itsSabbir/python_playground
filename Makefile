.PHONY: help install fmt lint test run check

help:
	@echo "Targets:"
	@echo "  make fmt    - format code (black)"
	@echo "  make lint   - lint code (ruff)"
	@echo "  make test   - run tests (pytest)"
	@echo "  make run    - run main script"
	@echo "  make check  - fmt + lint + test"

fmt:
	black .

lint:
	ruff check .

test:
	pytest -q

run:
	python -m python_playground.main

check: fmt lint test

install:
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt
	pre-commit install

db-up:
	docker compose up -d

db-down:
	docker compose down -v

unit:
	pytest -q -m "not integration"

itest:
	pytest -q -m "integration"
