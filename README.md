# Python Playground (North Star)

A WSL-first, production-style Python sandbox with enforced engineering standards.

## What this repo proves

- Reproducible local dev via WSL + venv
- Consistent quality gates: formatting, linting, tests
- Automated enforcement via pre-commit
- Simple developer UX via Makefile

## Quickstart
```bash
cd ~/dev/python_playground
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install ruff black pytest pre-commit
pre-commit install
make check
make run
```

## Commands

- `make fmt`   : format (black)
- `make lint`  : lint (ruff)
- `make test`  : tests (pytest)
- `make check` : fmt + lint + test
- `make run`   : run the demo script