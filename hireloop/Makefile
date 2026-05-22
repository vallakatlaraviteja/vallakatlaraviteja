.PHONY: up down logs migrate seed test lint fmt typecheck shell-api shell-db

up:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f --tail=200

migrate:
	docker compose exec api alembic upgrade head

makemigration:
	docker compose exec api alembic revision --autogenerate -m "$(m)"

seed:
	docker compose exec api python -m ops.seed

test:
	docker compose exec api pytest -v

lint:
	docker compose exec api ruff check .
	docker compose exec api ruff format --check .

fmt:
	docker compose exec api ruff check --fix .
	docker compose exec api ruff format .

typecheck:
	docker compose exec api mypy app

shell-api:
	docker compose exec api bash

shell-db:
	docker compose exec postgres psql -U hireloop -d hireloop
