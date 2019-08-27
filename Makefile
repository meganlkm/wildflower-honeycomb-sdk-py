default: generate-lib


generate-lib:
	gqlpycgen generate -r http://localhost:4000/graphql -o honeycomb/models.py -p true

publish:
	python3 setup.py sdist
	python3 -m twine upload dist/*

install:
	pip install -e git+https://github.com/WildflowerSchools/graphql-python-client-generator.git#egg=gqlpycgen
	pip install -e .
