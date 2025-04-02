# Todo API

This is a simple Todo API built using Python, adhering to the Clean Architecture principles, and implementing the Mediator and CQRS patterns.

## Project Structure

```
todo-api/
├── app/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities.py
│   │   └── interfaces.py
│   ├── application/
│   │   ├── __init__.py
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   ├── create_todo.py
│   │   │   ├── update_todo.py
│   │   │   ├── delete_todo.py
│   │   ├── queries/
│   │   │   ├── __init__.py
│   │   │   ├── get_todos.py
│   │   │   └── get_todo.py
│   │   └── mediator.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── todo_repository.py
│   ├── presentation/
│   │   ├── __init__.py
│   │   ├── controllers/
│   │   │   ├── __init__.py
│   │   │   └── todo_controller.py
│   │   ├── error_handler.py
│   │   └── routes.py
│   ├── main.py
│   └── tests/
│       ├── __init__.py
│       ├── test_commands.py
│       ├── test_queries.py
│       └── test_routes.py
├── apitest/
│   └── todo.http
├── requirements.txt
└── README.md
```

## Features

- **CRUD Operations**: Create, update, delete, and retrieve todo items.
- **Clean Architecture**: Separation of concerns with domain, application, infrastructure, and presentation layers.
- **Mediator Pattern**: Centralized handling of commands and queries.
- **CQRS Principles**: Separate models for reading and writing data.
- **In-Memory Repository**: A simple in-memory implementation for managing todos.
- **Global Error Handling**: Centralized error handling for consistent API responses.

## Tech Stack

The following technologies and libraries are used in this project:

- **Python**: The core programming language used for the application.
- **Flask**: A lightweight WSGI web application framework for building the API.
- **FastAPI** (optional): Some parts of the project (e.g., `routes.py`) demonstrate usage with FastAPI.
- **Pytest**: A testing framework for writing and running unit tests.
- **SQLAlchemy** (commented out): A database toolkit and ORM (optional, for future database integration).
- **In-Memory Repository**: A simple in-memory implementation for managing todos.
- **CQRS and Mediator Patterns**: Architectural patterns for separating read and write operations and centralizing command/query handling.

## API Endpoints

- `POST /api/todos`: Create a new todo item.
- `GET /api/todos`: Retrieve all todo items.
- `GET /api/todos/{id}`: Retrieve a specific todo item by ID.
- `PUT /api/todos/{id}`: Update an existing todo item by ID.
- `DELETE /api/todos/{id}`: Delete a todo item by ID.

## Error Handling

The application includes global error handling to ensure consistent responses:
- **400 Bad Request**: For invalid input or domain-specific errors (e.g., `ValueError`).
- **500 Internal Server Error**: For unexpected errors.

Error handling is implemented in `app/presentation/error_handler.py` and registered in `main.py`.

## Testing

To run the tests, use:
```
pytest app/tests
```

## How to Use

1. Clone the repository:
   ```
   git clone <repository-url>
   cd todo-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app/main.py
   ```

4. Use the `apitest/todo.http` file with the REST Client extension in VS Code to test the API.

## License

This project is licensed under the MIT License.