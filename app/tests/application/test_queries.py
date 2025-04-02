import pytest
from app.infrastructure.todo_repository import InMemoryTodoRepository
from app.application.queries.get_todos import GetTodosQuery, GetTodosHandler
from app.application.queries.get_todo import GetTodoQuery, GetTodoHandler
from app.domain.entities import Todo

@pytest.fixture
def todo_repository():
    # Initialize an in-memory repository with some test data
    repository = InMemoryTodoRepository()
    repository.add(Todo(id=1, title="Test Todo 1", description="Description 1", completed=False))
    repository.add(Todo(id=2, title="Test Todo 2", description="Description 2", completed=True))
    return repository

def test_get_todos(todo_repository):
    # Arrange
    query = GetTodosQuery()
    handler = GetTodosHandler(todo_repository)

    # Act
    todos = handler.handle(query)

    # Assert
    assert len(todos) == 2
    assert todos[0].title == "Test Todo 1"
    assert todos[1].completed is True

def test_get_todo_by_id(todo_repository):
    # Arrange
    query = GetTodoQuery(1)
    handler = GetTodoHandler(todo_repository)

    # Act
    todo = handler.handle(query)

    # Assert
    assert todo is not None
    assert todo.id == 1
    assert todo.title == "Test Todo 1"