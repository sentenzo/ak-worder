include .env
export

WEB_APP_DIR = ./$(PROJ_NAME)
WEB_APP_IMG_NAME = $(PROJ_LOWER_NAME)/$(WEB_APP_LOWER_NAME)

define ALEMBIC_MIGRATE
	poetry run alembic upgrade head
endef

init:
	poetry install

docker-build:
	poetry export --without-hashes -f requirements.txt --output $(WEB_APP_DIR)/requirements.txt
	docker build -f $(WEB_APP_DIR)/Dockerfile -t $(WEB_APP_IMG_NAME) --build-arg PROJ_NAME=$(PROJ_NAME) ./$(WEB_APP_DIR)
	

docker-up:
	docker-compose up -d db 
	$(ALEMBIC_MIGRATE)
	docker-compose up -d app

docker-down:
	docker-compose down --remove-orphans

docker-dbu: docker-down docker-build docker-up

docker-cleanup:
	docker rmi $(WEB_APP_IMG_NAME)
	docker image prune --force

docker-logs:
	docker-compose logs -f

run:
	docker-compose up -d db
	$(ALEMBIC_MIGRATE)
	poetry run uvicorn --reload --port 8000 $(PROJ_NAME):app

test:
	docker-compose up -d db
	poetry run pytest

linting:
	poetry run isort $(PROJ_NAME) tests
	poetry run black $(PROJ_NAME) tests
	poetry run pylint $(PROJ_NAME)