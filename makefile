APP_NAME = microservice



# GIT hooks documentation 
# https://www.viget.com/articles/two-ways-to-share-git-hooks-with-your-team/
# GIT 2.8 or below
# find .git/hooks -type l -exec rm {} \;
# find .githooks -type f -exec ln -sf ../../{} .git/hooks/ \;

init:
	chmod +x .githooks
	git config core.hooksPath .githooks

build:
	cat .env/${environment} > .flaskenv

install:
	pip install -r requirements/${environment}.txt

run:
	export FLASK_APP=${APP_NAME} && flask run --port 8000