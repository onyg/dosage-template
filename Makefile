.PHONY: install-dev test coverage lint clean

install-dev:
	pip install -r ./tests/requirements.txt

test:
	pytest

all-test: install-dev test