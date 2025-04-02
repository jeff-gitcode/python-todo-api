import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from app.presentation.controllers.todo_controller import todo_controller

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(todo_controller, url_prefix='/api')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_todo_success(client):
    # Arrange
    todo_data = {"title": "Test Todo", "description": "This is a test todo"}
    mock_todo = MagicMock(id=1, title="Test Todo", description="This is a test todo", completed=False)
    with patch('app.presentation.controllers.todo_controller.mediator.send', return_value=mock_todo) as mock_send:
        # Act
        response = client.post('/api/todos', json=todo_data)

        # Assert
        assert response.status_code == 201
        assert response.json == {
            "id": 1,
            "title": "Test Todo",
            "description": "This is a test todo",
            "completed": False
        }
        mock_send.assert_called_once()

def test_get_todos_success(client):
    # Arrange
    mock_todos = [
        MagicMock(id=1, title="Test Todo 1", description="Description 1", completed=False),
        MagicMock(id=2, title="Test Todo 2", description="Description 2", completed=True)
    ]
    with patch('app.presentation.controllers.todo_controller.mediator.send', return_value=mock_todos) as mock_send:
        # Act
        response = client.get('/api/todos')

        # Assert
        assert response.status_code == 200
        assert response.json == [
            {"id": 1, "title": "Test Todo 1", "description": "Description 1", "completed": False},
            {"id": 2, "title": "Test Todo 2", "description": "Description 2", "completed": True}
        ]
        mock_send.assert_called_once()

def test_get_todo_by_id_success(client):
    # Arrange
    todo_id = 1
    mock_todo = MagicMock(id=todo_id, title="Test Todo", description="Test Description", completed=False)
    with patch('app.presentation.controllers.todo_controller.mediator.send', return_value=mock_todo) as mock_send:
        # Act
        response = client.get(f'/api/todos/{todo_id}')

        # Assert
        assert response.status_code == 200
        assert response.json == {
            "id": todo_id,
            "title": "Test Todo",
            "description": "Test Description",
            "completed": False
        }
        mock_send.assert_called_once()

def test_get_todo_by_id_not_found(client):
    # Arrange
    todo_id = 999
    with patch('app.presentation.controllers.todo_controller.mediator.send', return_value=None) as mock_send:
        # Act
        response = client.get(f'/api/todos/{todo_id}')

        # Assert
        assert response.status_code == 404
        assert response.json == {"error": "Todo not found"}
        mock_send.assert_called_once()

def test_update_todo_success(client):
    # Arrange
    todo_id = 1
    update_data = {"title": "Updated Todo", "description": "Updated description"}
    mock_updated_todo = MagicMock(id=todo_id, title="Updated Todo", description="Updated description", completed=False)
    with patch('app.presentation.controllers.todo_controller.mediator.send', return_value=mock_updated_todo) as mock_send:
        # Act
        response = client.put(f'/api/todos/{todo_id}', json=update_data)

        # Assert
        assert response.status_code == 200
        assert response.json == {
            "id": todo_id,
            "title": "Updated Todo",
            "description": "Updated description",
            "completed": False
        }
        mock_send.assert_called_once()

def test_update_todo_not_found(client):
    # Arrange
    todo_id = 999
    update_data = {"title": "Updated Todo", "description": "Updated description"}
    with patch('app.presentation.controllers.todo_controller.mediator.send', side_effect=ValueError("Todo not found")) as mock_send:
        # Act
        response = client.put(f'/api/todos/{todo_id}', json=update_data)

        # Assert
        assert response.status_code == 404
        assert response.json == {"error": "Todo not found"}
        mock_send.assert_called_once()

def test_delete_todo_success(client):
    # Arrange
    todo_id = 1
    with patch('app.presentation.controllers.todo_controller.mediator.send', return_value=None) as mock_send:
        # Act
        response = client.delete(f'/api/todos/{todo_id}')

        # Assert
        assert response.status_code == 204
        assert response.data == b''
        mock_send.assert_called_once()

def test_delete_todo_not_found(client):
    # Arrange
    todo_id = 999
    with patch('app.presentation.controllers.todo_controller.mediator.send', side_effect=ValueError("Todo not found")) as mock_send:
        # Act
        response = client.delete(f'/api/todos/{todo_id}')

        # Assert
        assert response.status_code == 404
        assert response.json == {"error": "Todo not found"}
        mock_send.assert_called_once()