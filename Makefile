update: docker-down docker-pull docker-build docker-up
up: docker-up
down: docker-down
restart: down up
db: docker-db-make docker-db-migrate

docker-up:
	docker-compose up -d
docker-down:
	docker-compose down
docker-pull:
	git pull origin master
docker-build:
	docker-compose build
docker-db-make:
	docker-compose exec web python manage.py makemigrations
docker-db-migrate:
	docker-compose exec web python manage.py migrate



