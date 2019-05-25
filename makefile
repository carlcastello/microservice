APP_NAME = microservice

init:
	chmod +x .githooks
	# GIT 2.9 or greater
	git config core.hooksPath .githooks
	# GIT 2.8 or below
	# find .git/hooks -type l -exec rm {} \;
	# find .githooks -type f -exec ln -sf ../../{} .git/hooks/ \;


install:
	pip install -r requirements/${environment}.txt

run:
	export FLASK_APP=${APP_NAME} && flask run