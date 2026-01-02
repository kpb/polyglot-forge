SHELL := /usr/bin/env bash

UV ?= uv
PYTHON ?= python
PKG ?= example_pkg

# Resolve repo root relative to *this* Makefile location (blueprint/python/Makefile).
MKFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
REPO_ROOT  := $(abspath $(MKFILE_DIR)/../..)
PRE_COMMIT_CONFIG := $(REPO_ROOT)/.pre-commit-config.yaml

.PHONY: help init sync lock fmt lint test test-integration clean tree \
		hooks-install hooks-run hooks-update hooks-run-staged coverage coverage-xml coverage-html

help: ## Show targets
	@awk 'BEGIN {FS = ":.*##"; printf "\nTargets:\n"} /^[a-zA-Z_-]+:.*##/ {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

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

test: ## Run unit tests (default)
	$(UV) run -- pytest -m "not integration"

test-integration: ## Run integration tests (requires docker)
	$(UV) run -- pytest -m integration

coverage: ## Coverage (unit tests only)
	$(UV) run -- pytest -m "not integration" \
		--cov=$(PKG) --cov-report=term-missing --cov-fail-under=80

coverage-xml: ## Coverage (unit tests only) + coverage.xml (for CI)
	$(UV) run -- pytest -m "not integration" \
		--cov=$(PKG) --cov-report=term-missing --cov-report=xml --cov-fail-under=80

coverage-html: ## Coverage (unit tests only) + HTML report (htmlcov/)
	$(UV) run -- pytest -m "not integration" \
		--cov=$(PKG) --cov-report=term-missing --cov-report=html --cov-fail-under=80

clean: ## Remove caches/build artifacts and the venv
	rm -rf .venv .pytest_cache .ruff_cache __pycache__
	rm -rf dist build *.egg-info
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +

tree: ## Show a quick project tree (if `tree` is installed)
	@command -v tree >/dev/null && tree -a -I ".venv|__pycache__|.pytest_cache|.ruff_cache|dist|build" || true

hooks-install: ## Install pre-commit git hooks (uses repo root config)
	$(UV) run -- pre-commit install -c $(PRE_COMMIT_CONFIG)

hooks-run: ## Run hooks on all files (uses repo root config)
	$(UV) run -- pre-commit run --all-files -c $(PRE_COMMIT_CONFIG)

hooks-update: ## Bump hook versions in .pre-commit-config.yaml
	$(UV) run -- pre-commit autoupdate -c $(PRE_COMMIT_CONFIG)

hooks-run-staged: ## Run hooks on staged files only (uses repo root config)
	$(UV) run -- pre-commit run -c $(PRE_COMMIT_CONFIG)
