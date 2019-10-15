.PHONY: build upload

build:
	python setup.py sdist

upload:
	twine upload dist/umock-*.tar.gz
