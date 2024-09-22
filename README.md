# Project Management App - Backend

This is the Flask backend for the Project Management App. The backend provides a REST API that allows users to register, log in, and manage projects and tasks. It uses PostgreSQL for data persistence and JSON Web Tokens (JWT) for user authentication.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Folder Structure](#folder-structure)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This Flask API provides users the ability to:
- Register and log in with authentication via JWT tokens.
- Create, read, update, and delete projects.
- Manage tasks associated with projects.

The backend uses Flask for the web framework and PostgreSQL for database storage.

## Technologies

The backend is built with the following technologies:
- Flask: Lightweight Python web framework.
- Flask-JWT-Extended: For JWT-based authentication.
- SQLAlchemy: ORM for database interaction.
- PostgreSQL: Relational database used to store data.
- Flask-Migrate: Database migrations for SQLAlchemy models.

## Features

- User Authentication: Register and login with JWT-based authentication.
- Project Management: Create, view, update, and delete projects.
- Task Management: Add tasks to projects, view all tasks, update, and delete tasks.

## Prerequisites

Before running this project, ensure you have the following installed:
- Python 3.8+
- PostgreSQL (ensure the service is running and accessible)
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/themidix/project-management-py-api.git
   ```

2. Navigate to the project directory:
   ```
   cd project-management-backend
   ```

3. Create a virtual environment and activate it:
   ```
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the PostgreSQL database:
   - Create a PostgreSQL database:
     ```
     CREATE DATABASE project_management;
     ```
   - Configure your database connection in the `config.py` file:
     ```python
     SQLALCHEMY_DATABASE_URI = 'postgresql://your_username:your_password@localhost/project_management'
     ```

6. Apply the database migrations:
   ```
   flask db upgrade
   ```

## Running the Application

1. Set the Flask application environment variable:
   ```
   export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
   ```

2. Run the Flask development server:
   ```
   flask run
   ```

This will start the backend API at `http://localhost:5000`.

## API Endpoints

Here's a list of the available API endpoints:

### Authentication

- `POST /auth/register`: Register a new user.
  - Request body:
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```

- `POST /auth/login`: Log in to get a JWT token.
  - Request body:
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
  - Response:
    ```json
    {
      "access_token": "your_jwt_token"
    }
    ```

### Projects

- `GET /projects`: Get all projects for the logged-in user.
- `POST /projects`: Create a new project.
  - Request body:
    ```json
    {
      "name": "Project Name",
      "description": "Project Description"
    }
    ```
- `GET /projects/<id>`: Get details of a specific project.
- `PUT /projects/<id>`: Update an existing project.
  - Request body:
    ```json
    {
      "name": "Updated Name",
      "description": "Updated Description"
    }
    ```
- `DELETE /projects/<id>`: Delete a project.

### Tasks

- `GET /tasks/<project_id>`: Get all tasks for a specific project.
- `POST /tasks/<project_id>`: Add a new task to a project.
  - Request body:
    ```json
    {
      "name": "Task Name",
      "description": "Task Description"
    }
    ```
- `PUT /tasks/<project_id>/<task_id>`: Update an existing task.
  - Request body:
    ```json
    {
      "name": "Updated Task Name",
      "description": "Updated Task Description"
    }
    ```
- `DELETE /tasks/<project_id>/<task_id>`: Delete a task from a project.

## Folder Structure

```
project-management-backend/
│
├── app.py           # Flask application setup
├── config.py        # Configuration file for database and app settings
├── models.py        # SQLAlchemy models for User, Project, and Task
├── routes.py        # API route definitions
├── repository.py    # Repository layer to handle DB operations
├── services.py      # Service layer for business logic
├── migrations/      # Database migration files
├── .venv/           # Virtual environment
└── README.md        # This file
```

## Database Schema

### Users Table:
| Column   | Type    | Description       |
|----------|---------|-------------------|
| id       | Integer | Primary key       |
| email    | String  | User's email      |
| password | String  | Hashed password   |

### Projects Table:
| Column      | Type    | Description              |
|-------------|---------|--------------------------|
| id          | Integer | Primary key              |
| name        | String  | Project name             |
| description | Text    | Project description      |
| user_id     | Integer | Foreign key to users     |

### Tasks Table:
| Column      | Type    | Description              |
|-------------|---------|--------------------------|
| id          | Integer | Primary key              |
| name        | String  | Task name                |
| description | Text    | Task description         |
| project_id  | Integer | Foreign key to projects  |

## Testing

To run the tests:

1. Set up a test database in PostgreSQL.
2. Write your test cases using pytest or another testing framework of your choice.
3. Run the tests with:
   ```
   pytest
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.