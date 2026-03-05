
include .env 
export

WEB_SERVICE_NAME=web
DB_SERVICE_NAME=db

build:
	@echo "🔨 Building Docker images..."
	docker-compose build --no-cache

up:
	@echo "🚀 Starting services..."
	docker-compose up -d

down:
	@echo "🛑 Stopping services..."
	docker-compose down

d-v:
	@echo "🗑️  Stopping services and removing volumes..."
	docker-compose down -v

logs:
	@echo "📖 Showing logs..."
	docker-compose logs -f

logs-service:
	@echo "📖 Showing $(WEB_SERVICE_NAME) service logs..."
	docker-compose logs -f $(WEB_SERVICE_NAME)

ps:
	@echo "📋 Showing running services..."
	docker-compose ps

bash:
	@echo "💻 Entering bash shell in $(WEB_SERVICE_NAME)..."
	docker-compose exec $(WEB_SERVICE_NAME) bash

makemigrations:
	@echo "🔄 Creating migrations..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py makemigrations

migrate:
	@echo "📊 Running migrations..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py migrate

createsuperuser:
	@echo "👤 Creating superuser..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py createsuperuser

collectstatic:
	@echo "📦 Collecting static files..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py collectstatic --noinput

test:
	@echo "✅ Running tests..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py test

test-show-failed-tests:
	@echo "✅ Running tests and showing failed ones..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py test --failfast


startapp:
	@echo "📂 Creating app: $(name)..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py startapp $(name)

shell:
	@echo "💻 Entering Django shell..."
	docker-compose exec $(WEB_SERVICE_NAME) python manage.py shell

orm-accounts:
	@echo "🗄️  Running accounts ORM test script..."
	docker-compose exec -T $(WEB_SERVICE_NAME) python -u manage.py shell < ./app/core_app/scripts/accounts_orm.py

database-shell:
	@echo "🗄️  Connecting to database..."
	docker-compose exec $(DB_SERVICE_NAME) psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

remove-ntw:
	@echo "🧹 Removing containers and network..."
	docker-compose down --remove-orphans

see-all:
	@echo "📋 Showing all containers..."
	docker-compose ps -a

all-volumes:
	@echo "💾 Listing all volumes..."
	docker volume ls




