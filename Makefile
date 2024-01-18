.ONESHELL:
SHELL := bash
.DEFAULT_GOAL := help
OS := $(shell uname)

.PHONY: help build_and_test build_wheel clean deploy_test deploy_prod pip_install pip_install_dev test check mypy_check compile_req install create_venv rebuild_venv run_test_uvicorn

PYENV_VERSION=3.11.7
VENV_NAME=tiny-dungeon-chargen

build_and_test: clean build_wheel pip_install test ## Build wheel, install, and execute tests

build: ## build the wheel for this package
	python -m build

clean: ## clean out dist/ directory
	rm -r dist/*

deploy_test: ## run all checks, build dist files, upload to test pypi
	ruff check .
	rm -f dist/*
	python -m build
	twine check dist/*
	twine upload --repository testpypi dist/*

deploy_prod: ## run all checks, build dist files, upload to prod pypi
	ruff check .
	rm -f dist/*
	python -m build
	twine check dist/*
	twine upload --repository account dist/*

install_wheel: ## pip install this package
	python -m pip install dist/tiny_dungeon-*-py3-none-any.whl --force-reinstall

test: ## Run pytest tests
	python -m pytest --cov-report term-missing tests/

check: ## Run all linting/formatting checks
	ruff check .

install: ## install/reinstall all packages in the environment
	python -m pip install --upgrade pip setuptools wheel
	python -m pip install -e .[dev]
	pyenv rehash
	pre-commit install

create_venv: ## create virtualenv for this project
	pyenv install ${PYENV_VERSION} --skip-existing
	pyenv rehash
	pyenv virtualenv-delete --force ${VENV_NAME}
	pyenv virtualenv ${PYENV_VERSION} ${VENV_NAME}
	pyenv local ${VENV_NAME}

rebuild_venv: create_venv install ## rebuild project virtualenv

help: ## Generate and display help info on make commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
