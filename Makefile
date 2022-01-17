python:=python3

.PHONY: clean venv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

venv:
	$(python) -m venv --prompt '|> polls <| ' env
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	@echo
	@echo "venv Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	@PYTHONPATH=PYTHONPATH:$$(pwd)/polls $(python) -m unittest \
		-v \
		$(arg)


docker: clean
	sudo docker build -t polls:latest .


start-docker:
	sudo docker run -it --mount=type=bind,source=$$(pwd),target=/src --rm -p 8000:8000 polls:latest

dist: clean
	rm -rf dist/*
	$(python) setup.py sdist
	$(python) setup.py bdist_wheel

dist-upload:
	twine upload dist/*
