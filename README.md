# Tasks API - Docker Implementation Test

This project demonstrates a Django REST API implementation with Docker, showcasing best practices for containerization and deployment configuration.

## Project Structure

```
tasks_api/
├── deploy/                  # Deployment configurations
│   ├── postgres/           # PostgreSQL service
│   │   ├── Dockerfile     # PostgreSQL container configuration
│   │   └── init.sql       # Database initialization script
│   └── server/            # API server service
│       └── Dockerfile     # Server container configuration
├── docker-compose.yaml     # Docker services orchestration
├── requirements.txt        # Python dependencies
└── ... (other project files)
```

## Features

- Django REST Framework API
- PostgreSQL Database
- Docker containerization
- Health checks and container orchestration
- Clean separation of deployment configurations

## Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Docker and Docker Compose (for containerized setup)

## Quick Start with Docker

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd tasks_api
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. The API will be available at:
   ```
   http://localhost:8000
   ```

## Manual Setup (Without Docker)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create PostgreSQL database:
   ```sql
   createdb basic_api
   ```

4. Set up environment variables:
   ```bash
   export DEBUG=1
   export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/basic_api
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Development

- The Docker setup includes hot-reload for development
- Database data is persisted in a Docker volume
- PostgreSQL is accessible on port 5432
- The API server runs on port 8000

## Environment Variables

- `DEBUG`: Enable debug mode (default: 1)
- `DATABASE_URL`: PostgreSQL connection URL
- `POSTGRES_USER`: Database user (default: postgres)
- `POSTGRES_PASSWORD`: Database password (default: postgres)

## Docker Commands

- Start services:
  ```bash
  docker-compose up
  ```

- Rebuild and start services:
  ```bash
  docker-compose up --build
  ```

- Stop services:
  ```bash
  docker-compose down
  ```

- View logs:
  ```bash
  docker-compose logs -f
  ```

## Notes

- The Docker setup includes health checks to ensure the database is ready before starting the API
- Database initialization is handled through the `init.sql` script
- The project uses a multi-stage Docker setup with separate configurations for the database and API server 