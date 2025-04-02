from app.core.queries.get_todo import GetTodoQuery
from app.infrastructure.repositories import TodoRepository
import pytest

@pytest.fixture
def todo_repository():
    return TodoRepository()

@pytest.fixture
def get_todo_query(todo_repository):
    return GetTodoQuery(todo_repository)

def test_execute_returns_todo(get_todo_query):
    # Arrange
    todo_id = 1  # Assuming a todo with this ID exists
    expected_todo = {
        "id": todo_id,
        "title": "Sample Todo",
        "description": "This is a sample todo item.",
        "completed": False
    }
    
    # Act
    result = get_todo_query.execute(todo_id)

    # Assert
    assert result == expected_todo

def test_execute_todo_not_found(get_todo_query):
    # Arrange
    todo_id = 999  # Assuming no todo with this ID exists

    # Act & Assert
    with pytest.raises(ValueError, match="Todo not found"):
        get_todo_query.execute(todo_id)