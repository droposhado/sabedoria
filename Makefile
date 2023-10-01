DATABASE_URL=postgresql://sabedoria:sabedoria@localhost/sabedoria
FLASK_APP=sabedoria:create_app('sabedoria.config.TestConfig')
TOKEN=awesometoken
DEBUG=1
BASEROW_TOKEN=awesomesecrettoken
BASEROW_URL=https://api.baserow.io
COURSE_TABLE_ID=999999
DESCRIPTION_TABLE_ID=999999
EMAIL=mail@sample.com
GITHUB=username
HOST=0.0.0.0
INTEREST_TABLE_ID=999999
JOB_TABLE_ID=999999
LANGS=en-US,pt-BR
LINKEDIN=username
NAME="Real Name"
PORT=5000
PROJECT_TABLE_ID=999999
SITE=sample.com
WEB_BIND=0.0.0.0:5000

export DATABASE_URL
export FLASK_APP
export TOKEN
export DEBUG
export BASEROW_TOKEN
export BASEROW_URL
export COURSE_TABLE_ID
export DESCRIPTION_TABLE_ID
export EMAIL
export GITHUB
export HOST
export INTEREST_TABLE_ID
export JOB_TABLE_ID
export LANGS
export LINKEDIN
export NAME
export PORT
export PROJECT_TABLE_ID
export SITE
export WEB_BIND


bandit:
	bandit -v -r . -c pyproject.toml

pylint:
	pylint -j $(shell nproc) --recursive=y .

isort:
	isort .

ruff:
	ruff check .

liccheck:
	liccheck

lint: isort ruff pylint bandit liccheck

docker-pg-stop:
	docker container stop sabedoria_pg || true
	docker container prune -f
	docker volume prune --all -f

docker-pg-start: docker-pg-stop
	docker run --name sabedoria_pg \
	    -e POSTGRES_PASSWORD=sabedoria \
	    -e POSTGRES_USER=sabedoria \
	    -e POSTGRES_DB=sabedoria \
	    -p 0.0.0.0:5432:5432 \
	    -d postgres:15

tests: docker-pg-start

	pip install flit
	pip install -e .
	pip install .[test]
	flask drop-tables
	flask create-tables
	python -m unittest discover -s tests -vvv
	flask drop-tables
	pip uninstall sabedoria -y
