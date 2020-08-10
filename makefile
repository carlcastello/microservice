APP_NAME = microservice



# GIT hooks documentation 
# https://www.viget.com/articles/two-ways-to-share-git-hooks-with-your-team/

git-init:
	git config core.hooksPath .githooks

test:
	python3 -m unittest discover -v

install:
	pipenv install --dev

migrate:
	flask db migrate

upgrade:
	flask db upgrade

downgrade:
	flask db downgrade
