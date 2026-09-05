default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: install
install: # Install dependencies
	uv sync
	uv export --frozen --no-hashes -o requirements.txt

.PHONY: run
run: # Run website locally
	rm -rf output
	uv run pelican -s pelicanconf.py -t theme -o output -l -r

.PHONY: build
build: # Build website for production
	rm -rf output
	uv run pelican -s publishconf.py -t theme -o output

.PHONY: serve
serve: # Serve built website and API with Bun
	bun run server.js

.PHONY: test
test: # Test the Bun server over HTTP
	bun test

.PHONY: format
format: # Format Python and JavaScript files
	uv run ruff check --fix .
	uv run ruff format .
	npx --yes prettier@3.6.2 --write 'functions/**/*.js' 'theme/static/js/**/*.js' 'server*.js'

.PHONY: check
check: # Check Python files and JavaScript formatting
	uv run ruff check .
	uv run ruff format --check .
	uv run ty check
	npx --yes prettier@3.6.2 --check 'functions/**/*.js' 'theme/static/js/**/*.js' 'server*.js'
	$(MAKE) test

.PHONY: lint
lint: check # Alias for check
