default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: install
install: # Install dependencies
	uv sync

.PHONY: run
run: # Run website locally
	rm -rf output
	uv run pelican -s pelicanconf.py -t theme -o output -l -r

.PHONY: build
build: # Build website for production
	rm -rf output
	uv run pelican -s publishconf.py -t theme -o output

.PHONY: lint
lint: # Lint and format python files with ruff
	uv run ruff check .
	uv run ruff format --check .

.PHONY: format
format: # Format and fix python files with ruff
	uv run ruff check --fix .
	uv run ruff format .
