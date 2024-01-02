# run site
run:
	source .env_variables
	pelican -s pelicanconf.py -t theme -o output -l -r
