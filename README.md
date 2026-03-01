# Task Management API

A simple **REST API** for managing tasks with **JWT authentication** using Django REST Framework.

## Features
- User registration and login (JWT)
- Create, read, update, and delete tasks
- Each task is linked to a specific user
- Protected endpoints for authenticated users only

## Technologies
- Python 3.11
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (default)

## API Endpoints

### Public
- `POST /api/users/register/` – Register a new user
- `POST /api/login/` – Login and receive JWT tokens

### Protected (Auth Required)
- `POST /api/tasks/` – Create a task
- `GET /api/tasks/` – List your tasks
- `PUT /api/tasks/<id>/` – Update a task
- `DELETE /api/tasks/<id>/` – Delete a task

> Include JWT access token in headers:  

## Models
**User** (Django default)  
**Task** – title, description, completed, user (FK)

## Setup
1. Clone repository  
2. Activate virtual environment: `source venv/bin/activate`  
3. Install dependencies: `pip install -r requirements.txt`  
4. Run migrations: `python manage.py migrate`  
5. Start server: `python manage.py runserver`  

## License
MIT License