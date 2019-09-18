default: generate-lib


generate-lib:
	gqlpycgen generate -r http://localhost:4000/graphql -o honeycomb/models.py -p true

generate-lib-prod:
	@gqlpycgen generate -r https://honeycomb.api.wildflower-tech.org/graphql -o honeycomb/models.py -p true --accesstoken $$(node ../honeycomb/auth.js)

publish:
	python3 setup.py sdist
	python3 -m twine upload dist/*
