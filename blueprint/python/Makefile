SHELL := /usr/bin/env bash

UV ?= uv
PYTHON ?= python
PKG ?= example_pkg

.PHONY: help init sync lock fmt lint test clean tree

help: ## Show targets
	@awk 'BEGIN {FS = ":.*##"; printf "\nTargets:\n"} /^[a-zA-Z_-]+:.*##/ {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

init: ## Create venv and sync dependencies (generates uv.lock on first run)
	$(UV) venv
	$(UV) sync

sync: ## Sync environment to pyproject + uv.lock
	$(UV) sync

lock: ## Update uv.lock without necessarily running code
	$(UV) lock

fmt: ## Format code (ruff)
	$(UV) run -- ruff format .

lint: ## Lint (ruff)
	$(UV) run -- ruff check .

test: ## Run unit tests
	$(UV) run -- pytest -m "not integration"

test-integration: ## Run integration tests (requires docker)
	$(UV) run -- pytest -m "integration"

clean: ## Remove caches/build artifacts and the venv
	rm -rf .venv .pytest_cache .ruff_cache __pycache__
	rm -rf dist build *.egg-info
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +

tree: ## Show a quick project tree (if `tree` is installed)
	@command -v tree >/dev/null && tree -a -I ".venv|__pycache__|.pytest_cache|.ruff_cache|dist|build" || true
