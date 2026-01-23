default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: run
run: # Run website
	rm -rf output
	pelican -s pelicanconf.py -t theme -o output -l -r

.PHONY: lint
lint: # Lint markdown files
	markdownlint-cli2 "content/**/*.md"
