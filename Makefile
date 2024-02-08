.PHONY:
.SILENT:

run:
	venv/bin/python main.py

gen:
	alembic revision -m "$(name)" --autogenerate

migrate:
	alembic upgrade head