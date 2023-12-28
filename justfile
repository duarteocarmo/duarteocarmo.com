set dotenv-filename := ".env_variables"

# run site
site:
	pelican -s pelicanconf.py -t theme -o output -l -r
	

