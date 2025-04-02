import pytest
from app.domain.entities import Todo
from app.infrastructure.todo_repository import InMemoryTodoRepository

@pytest.fixture
def todo_repository():
    # Initialize an in-memory repository with some test data
    repository = InMemoryTodoRepository()
    repository.add(Todo(id=1, title="Test Todo 1", description="Description 1", completed=False))
    repository.add(Todo(id=2, title="Test Todo 2", description="Description 2", completed=True))
    return repository

def test_add_todo(todo_repository):
    # Arrange
    new_todo = Todo(id=None, title="New Todo", description="New Description", completed=False)

    # Act
    added_todo = todo_repository.add(new_todo)

    # Assert
    assert added_todo.id == 3  # Next ID in the repository
    assert added_todo.title == "New Todo"
    assert added_todo.description == "New Description"
    assert added_todo.completed is False
    assert len(todo_repository.list_all()) == 3

def test_get_todo_by_id(todo_repository):
    # Act
    todo = todo_repository.get(1)

    # Assert
    assert todo is not None
    assert todo.id == 1
    assert todo.title == "Test Todo 1"
    assert todo.description == "Description 1"
    assert todo.completed is False

def test_get_todo_by_id_not_found(todo_repository):
    # Act
    todo = todo_repository.get(999)

    # Assert
    assert todo is None

def test_list_all_todos(todo_repository):
    # Act
    todos = todo_repository.list_all()

    # Assert
    assert len(todos) == 2
    assert todos[0].id == 1
    assert todos[1].id == 2

def test_update_todo_success(todo_repository):
    # Arrange
    updated_todo = Todo(id=1, title="Updated Title", description="Updated Description", completed=True)

    # Act
    result = todo_repository.update(updated_todo)

    # Assert
    assert result is not None
    assert result.id == 1
    assert result.title == "Updated Title"
    assert result.description == "Updated Description"
    assert result.completed is True

def test_update_todo_not_found(todo_repository):
    # Arrange
    updated_todo = Todo(id=999, title="Nonexistent Todo", description="Does not exist", completed=False)

    # Act
    result = todo_repository.update(updated_todo)

    # Assert
    assert result is None

def test_delete_todo_success(todo_repository):
    # Act
    result = todo_repository.delete(1)

    # Assert
    assert result is True
    assert len(todo_repository.list_all()) == 1
    assert todo_repository.get(1) is None

def test_delete_todo_not_found(todo_repository):
    # Act
    result = todo_repository.delete(999)

    # Assert
    assert result is False
    assert len(todo_repository.list_all()) == 2