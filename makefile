default: generate-lib


generate-lib:
	gqlpycgen generate -r http://localhost:4000/graphql -o honeycomb/models.py -p true
