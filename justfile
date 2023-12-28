set dotenv-filename := ".env_variables"

# run site
run:
	pelican -s pelicanconf.py -t theme -o output -l -r
