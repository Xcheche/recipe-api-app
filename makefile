
include .env 
export

build:
	docker-compose build --no-cache
up:
	docker-compose up -d
down:
	docker-compose down
d-v:
	docker-compose down -v	
logs:
	docker-compose logs -f
ps:
	docker-compose ps
bash:
	docker-compose exec app bash
makemigrations:
	docker-compose exec web python manage.py makemigrations		
migrate:
	docker-compose exec web python manage.py migrate
createsuperuser:
	docker-compose exec web python manage.py createsuperuser
collectstatic:
	docker-compose exec web python manage.py collectstatic --noinput
test:
	docker-compose exec web python manage.py test	

startapp:
	docker-compose exec web python manage.py startapp $(name) 

shell:
	docker-compose exec web python manage.py shell
database-shell:
	docker-compose exec db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)		
