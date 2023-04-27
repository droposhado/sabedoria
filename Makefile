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
