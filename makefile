APP_NAME = microservice



# GIT hooks documentation 
# https://www.viget.com/articles/two-ways-to-share-git-hooks-with-your-team/

git-init:
	git config core.hooksPath .githooks

project-init:
	export FLASK_APP=${APP_NAME} 

init-windows:
	set FLASK_APP=${APP_NAME} 

test:
	python3 -m unittest discover -v

install:
	pip install -r requirements/${environment}.txt

migrate:
	flask db migrate

upgrade:
	flask db upgrade

downgrade:
	flask db downgrade

run:
	flask run --port 8000