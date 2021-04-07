setup:
	python3 -m venv ~/.demo

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest tests/*.py


lint:
	pylint --disable=R,C,W0702,W0703 app.py

all: install lint test
