# 🎓 Academic Project Management System (DSDB)

A comprehensive backend platform for managing end-of-studies projects, built with Django REST Framework and containerized with Docker. This system streamlines the entire workflow of academic project management, from submission to evaluation.

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0+-green.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Commands](#docker-commands)
- [Database Management](#database-management)
- [Contributing](#contributing)

## 🌟 Overview

The DSDB (Data Systems and Databases) Academic Project Management System is a Django-based REST API backend designed to manage the complete lifecycle of graduation projects. It provides a robust platform for students, supervisors, and administrators to collaborate on academic projects efficiently.

### Key Capabilities

- **Project Management**: Create, track, and manage graduation projects
- **User Management**: Separate roles for students, supervisors, and administrators
- **Workflow Automation**: Streamlined submission and review processes
- **RESTful API**: Clean, well-documented API endpoints
- **Containerized Deployment**: Docker-ready for consistent environments
- **Database-Driven**: Robust MySQL backend with proper relationships

## ✨ Features

### Core Functionality

- 🔐 **Authentication & Authorization**: Role-based access control for different user types
- 📝 **Project Submission**: Students can submit and manage their project proposals
- 👥 **Supervisor Management**: Assign supervisors and track project progress
- 📊 **Project Tracking**: Monitor project status through various stages
- 🔍 **Search & Filter**: Advanced querying capabilities for projects and users
- 📄 **Document Management**: Handle project documentation and submissions
- ⚡ **RESTful API**: Complete API for integration with frontend applications
- 🐳 **Docker Support**: Full containerization with docker-compose

### Technical Features

- **Django ORM**: Efficient database operations and migrations
- **MySQL Integration**: Reliable relational database backend
- **API Documentation**: Auto-generated API documentation
- **CORS Support**: Ready for frontend integration
- **Environment Configuration**: Secure credential management
- **Database Seeding**: Automated data population for testing

## 🛠️ Technology Stack

**Backend Framework**
- Django 4.0+
- Django REST Framework
- Python 3.9+

**Database**
- MySQL 8.0
- Django ORM for data modeling

**Containerization & Deployment**
- Docker
- Docker Compose
- Waitress WSGI Server

**Development Tools**
- Pipenv for dependency management
- Git for version control

## 📁 Project Structure

```
DS_DB_Backend_3rd_YearPROJECT/
├── core/                    # Core app with shared utilities
│   ├── models.py           # Core database models
│   ├── views.py            # Core API views
│   └── serializers.py      # Data serialization
├── dsdb/                    # Main Django project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI application
├── project/                 # Project management app
│   ├── models.py           # Project-related models
│   ├── views.py            # Project API views
│   ├── serializers.py      # Project serializers
│   └── urls.py             # Project URLs
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Multi-container setup
├── docker-entrypoint.sh    # Container initialization script
├── wait-for-it.sh          # Database readiness check
├── requirements.txt        # Python dependencies
├── Pipfile                 # Pipenv configuration
├── manage.py               # Django management script
└── .gitignore              # Git ignore rules
```

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Docker Desktop** (latest version)
  - Includes both Docker Engine and Docker Compose
  - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Verify Installation

Check if Docker is properly installed:

```bash
# Check Docker version
docker --version
# Expected output: Docker version 20.10.21 or higher

# Check Docker Compose version
docker-compose --version
# Expected output: Docker Compose version v2.13.0 or higher
```

## 🚀 Installation

### 1. Clone the Repository

**Important**: Use the following command to avoid line ending issues:

```bash
git clone https://github.com/Ibr4h3m-k4m/DS_DB_Backend_3rd_YearPROJECT.git --config core.autocrlf=input
cd DS_DB_Backend_3rd_YearPROJECT
```

### 2. Build and Run with Docker

Start the application using Docker Compose:

```bash
docker-compose up -d --build
```

**Note**: First-time setup may take 5-15 minutes as Docker downloads and builds the necessary images.

### 3. Verify Services are Running

```bash
docker-compose ps
```

You should see two services running:
- `web` (Django application)
- `db` (MySQL database)

## 💻 Usage

### Accessing the Application

Once the containers are running:

- **API Base URL**: `http://localhost:8000/`
- **Admin Interface**: `http://localhost:8000/admin/`
- **API Documentation**: `http://localhost:8000/api/docs/` (if configured)

### Creating a Superuser

```bash
docker-compose run web python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Running Migrations

```bash
# Create migrations
docker-compose run web python manage.py makemigrations

# Apply migrations
docker-compose run web python manage.py migrate
```

## 🔌 API Endpoints

### Authentication Endpoints

```http
POST /api/auth/login/          # User login
POST /api/auth/logout/         # User logout
POST /api/auth/register/       # User registration
```

### Project Management Endpoints

```http
GET    /api/projects/          # List all projects
POST   /api/projects/          # Create new project
GET    /api/projects/{id}/     # Get project details
PUT    /api/projects/{id}/     # Update project
DELETE /api/projects/{id}/     # Delete project
```

### User Management Endpoints

```http
GET    /api/users/             # List users
GET    /api/users/{id}/        # Get user details
PUT    /api/users/{id}/        # Update user
```

### Supervisor Endpoints

```http
GET    /api/supervisors/       # List supervisors
POST   /api/projects/{id}/assign-supervisor/  # Assign supervisor
```

**Note**: Refer to `logincredentials.txt` for test user credentials.

## 🐳 Docker Commands

### Starting the Application

```bash
# Start in detached mode
docker-compose up -d

# Start with build
docker-compose up -d --build

# View logs
docker-compose logs -f
```

### Stopping the Application

```bash
# Stop containers
docker-compose stop

# Stop and remove containers
docker-compose down

# Stop and remove containers + volumes
docker-compose down -v
```

### Running Django Commands

```bash
# General format
docker-compose run web python manage.py <command>

# Examples
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose run web python manage.py collectstatic
```

### Accessing Container Shell

```bash
# Access web container bash
docker-compose exec web bash

# Access MySQL shell
docker-compose exec db mysql -u root -p
```

## 💾 Database Management

### Database Configuration

The MySQL database is accessible on:
- **Host**: `localhost`
- **Port**: `3366` (mapped from container port 3306)
- **Database**: `dsdb`
- **Username**: `root`
- **Password**: (specified in docker-compose.yml)

### Connecting with DataGrip or Similar Tools

1. Add a new MySQL datasource
2. Configure connection:
   - Host: `localhost`
   - Port: `3366`
   - Database: `dsdb`
   - User: `root`
   - Password: (from docker-compose.yml)
3. Install Docker plugin for better integration

### Database Backup

```bash
# Backup database
docker-compose exec db mysqldump -u root -p dsdb > backup.sql

# Restore database
docker-compose exec -T db mysql -u root -p dsdb < backup.sql
```

## 🧪 Testing

```bash
# Run all tests
docker-compose run web python manage.py test

# Run specific test module
docker-compose run web python manage.py test core.tests

# Run with coverage
docker-compose run web coverage run --source='.' manage.py test
docker-compose run web coverage report
```

## 📦 Dependencies

Main Python packages (see `requirements.txt` for complete list):

```
Django>=4.0
djangorestframework
mysqlclient
django-cors-headers
waitress
python-dotenv
```

## ⚙️ Environment Variables

Create a `.env` file in the project root (not tracked in git):

```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DB_NAME=dsdb
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=db
DB_PORT=3306

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 🐛 Troubleshooting

### Common Issues

**Issue**: Docker containers won't start
```bash
# Solution: Check if ports are already in use
docker-compose down
docker-compose up -d --force-recreate
```

**Issue**: Database connection errors
```bash
# Solution: Wait for database to be ready
docker-compose logs db
# Check if MySQL is fully initialized
```

**Issue**: Permission errors on Linux
```bash
# Solution: Fix file permissions
sudo chown -R $USER:$USER .
```

**Issue**: Changes not reflecting
```bash
# Solution: Rebuild containers
docker-compose down
docker-compose up -d --build
```

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker Documentation](https://docs.docker.com/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ibrahim Kamraoui**

- GitHub: [@Ibr4h3m-k4m](https://github.com/Ibr4h3m-k4m)
- LinkedIn: [Ibrahim Kamraoui](https://linkedin.com/in/ibrahim-kamraoui-b25721248)
- Email: brahim.kamraoui@gmail.com

## 🙏 Acknowledgments

- Built as part of 3rd year academic project at ESI
- Thanks to all team members and supervisors
- Django and DRF communities for excellent documentation

## 📝 Project Status

**Status**: Completed ✅

This project was developed as part of the academic curriculum and demonstrates:
- Full-stack backend development capabilities
- RESTful API design principles
- Docker containerization skills
- Database design and management
- Team collaboration and project management

---

**Note**: This project is for educational purposes. For production deployment, ensure proper security measures, environment variable management, and performance optimization.

## 🔗 Related Projects

- [Weather API Project](https://github.com/Ibr4h3m-k4m/Weather-open-meteo-API-Project)
- [FastAPI Learning Roadmap](https://github.com/Ibr4h3m-k4m/FastApiRoadMapWithGpt)

---

Made with ❤️ for academic excellence
