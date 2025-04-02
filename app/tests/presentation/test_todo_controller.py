import pytest
from unittest.mock import patch, MagicMock
from flask import Flask

from app.presentation.controllers import todo_controller

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(todo_controller, url_prefix='/api')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_todo_by_id_success(client):
    # Arrange
    todo_id = 1
    mock_todo = MagicMock(id=todo_id, title="Test Todo", description="Test Description", completed=False)
    with patch('todo_controller.mediator.send', return_value=mock_todo) as mock_send:
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
    with patch('todo_controller.mediator.send', return_value=None) as mock_send:
        # Act
        response = client.get(f'/api/todos/{todo_id}')
        
        # Assert
        assert response.status_code == 404
        assert response.json == {"error": "Todo not found"}
        mock_send.assert_called_once()