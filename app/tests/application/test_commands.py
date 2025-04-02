import pytest
from app.application.commands.delete_todo import DeleteTodoCommand, DeleteTodoHandler
from app.infrastructure.todo_repository import InMemoryTodoRepository
from app.application.commands.create_todo import CreateTodoCommand, CreateTodoHandler
from app.application.commands.update_todo import UpdateTodoCommand, UpdateTodoHandler
from app.domain.entities import Todo

@pytest.fixture
def todo_repository():
    # Initialize an in-memory repository with some test data
    repository = InMemoryTodoRepository()
    repository.add(Todo(id=1, title="Test Todo 1", description="Description 1", completed=False))
    repository.add(Todo(id=2, title="Test Todo 2", description="Description 2", completed=True))
    return repository

def test_create_todo_command(todo_repository):
    # Arrange
    handler = CreateTodoHandler(todo_repository)
    command = CreateTodoCommand(title="New Todo", description="New Description")

    # Act
    created_todo = handler.handle(command)

    # Assert
    assert created_todo.id == 3  # Next ID in the repository
    assert created_todo.title == "New Todo"
    assert created_todo.description == "New Description"
    assert len(todo_repository.list_all()) == 3

def test_update_todo_command(todo_repository):
    # Arrange
    handler = UpdateTodoHandler(todo_repository)
    command = UpdateTodoCommand(todo_id=1, title="Updated Title", description="Updated Description")

    # Act
    updated_todo = handler.handle(command)

    # Assert
    assert updated_todo.id == 1
    assert updated_todo.title == "Updated Title"
    assert updated_todo.description == "Updated Description"
    assert len(todo_repository.list_all()) == 2
    
def test_delete_todo_command(todo_repository):
    # Arrange
    handler = DeleteTodoHandler(todo_repository)
    command = DeleteTodoCommand(todo_id=1)

    # Act
    deleted = handler.handle(command)

    # Assert
    assert deleted is True
    assert len(todo_repository.list_all()) == 1
    assert todo_repository.get(1) is None
    assert todo_repository.get(2) is not None
    assert todo_repository.get(2).id == 2
    assert todo_repository.get(2).title == "Test Todo 2"
    assert todo_repository.get(2).description == "Description 2"
    assert todo_repository.get(2).completed is True
    