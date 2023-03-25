.PHONY: gen_openapi make_migration

makemigrations:
	poetry run python manage.py makemigrations src

gen_openapi:
	poetry run python manage.py generateschema --file ../openapi-schema.yml --title "AmazonみたいなECサイト"