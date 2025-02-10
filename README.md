# Tasks API - Docker Implementation Test

This project demonstrates a Django REST API implementation with Docker, showcasing best practices for containerization and deployment configuration.

## Project Structure

```
tasks_api/
├── api/                    # API application
│   ├── views.py           # API endpoints
│   ├── models.py          # Data models
│   ├── serializers.py     # Data serializers
│   └── urls.py            # API routing
├── backend/               # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py           # Project URL routing
│   └── wsgi.py           # WSGI configuration
├── deploy/                # Deployment configurations
│   ├── postgres/         # PostgreSQL service
│   │   ├── Dockerfile    # PostgreSQL container configuration
│   │   └── init.sql      # Database initialization script
│   └── server/           # API server service
│       └── Dockerfile    # Server container configuration
├── docker-compose.yaml    # Docker services orchestration
├── Makefile              # Development automation
├── .env                  # Environment variables (not in version control)
├── .env.example          # Environment variables template
├── requirements.txt      # Python dependencies
└── manage.py            # Django management script
```

## Features

- RESTful API endpoints for task management
- Django REST Framework with browsable API interface
- PostgreSQL Database for data persistence
- Docker containerization with multi-stage builds
- Health checks and container orchestration
- Environment-based configuration
- Comprehensive API documentation
- Test coverage for API endpoints

## Prerequisites

- Python 3.12+
- PostgreSQL 15+
- Docker 24.0+ and Docker Compose V2
- Make (optional, for using Makefile commands)

## Quick Start with Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/oragazzo/tasks_api.git
   cd tasks_api
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your desired configuration
   ```

3. Start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```


## Manual Setup (Without Docker)

1. Create a virtual environment:
   ```bash
   # Option 1: Using Conda (Recommended)
   conda create -n tasks_api python=3.12
   conda activate tasks_api

   # Option 2: Using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   # For local development, make sure DATABASE_HOST=localhost
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create PostgreSQL database:
   ```bash
   createdb basic_api
   ```

5. Run migrations and create superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

The project uses a `.env` file for configuration. Copy `.env.example` to `.env` and adjust the values:

```bash
# Django Settings
DEBUG=1
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DATABASE_NAME=basic_api
DATABASE_USER=<DB_USER>
DATABASE_PASSWORD=<DB_PASSWORD>
DATABASE_HOST=db        # Use 'db' for Docker, 'localhost' for local development
DATABASE_PORT=5432

# PostgreSQL Container Settings
POSTGRES_DB=basic_api
POSTGRES_USER=<PG_USER>
POSTGRES_PASSWORD=<PG_PASSWORD>
```

## Development

- The Docker setup includes hot-reload for development
- Database data is persisted in a Docker volume
- PostgreSQL is accessible on port 5432
- The API server runs on port 8000
- Environment variables are loaded from `.env` file

## Docker Commands

Common commands for managing the Docker environment:

```bash
# Start services in development mode
docker-compose up

# Start services in detached mode
docker-compose up -d

# Rebuild and start services
docker-compose up --build

# Stop services
docker-compose down

# Stop services and remove volumes
docker-compose down -v

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f api
```

## Security Notes

- The `.env` file contains sensitive information and is not included in version control
- Default Django admin credentials should be changed in production
- Debug mode should be disabled in production
- Use strong passwords for database and Django admin
- Regular security updates should be applied to all dependencies

## License

This project is licensed under the MIT License - see the LICENSE file for details 