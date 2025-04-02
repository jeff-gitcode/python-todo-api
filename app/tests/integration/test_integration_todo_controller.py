import pytest
from app.main import apps  # Import the Flask app from your main module


@pytest.fixture
def client():
    # Use Flask's test client for integration testing
    with apps.test_client() as client:
        yield client


def test_create_todo_integration(client):
    # Arrange
    todo_data = {"title": "Integration Test Todo", "description": "This is an integration test todo"}

    # Act
    response = client.post('/api/todos', json=todo_data)

    # Assert
    assert response.status_code == 201
    assert response.json["title"] == "Integration Test Todo"
    assert response.json["description"] == "This is an integration test todo"
    assert response.json["completed"] is False


def test_get_todos_integration(client):
    # Act
    response = client.get('/api/todos')

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_todo_by_id_integration(client):
    # Arrange
    todo_data = {"title": "Integration Test Todo", "description": "This is an integration test todo"}
    create_response = client.post('/api/todos', json=todo_data)
    todo_id = create_response.json["id"]

    # Act
    response = client.get(f'/api/todos/{todo_id}')

    # Assert
    assert response.status_code == 200
    assert response.json["id"] == todo_id
    assert response.json["title"] == "Integration Test Todo"
    assert response.json["description"] == "This is an integration test todo"


def test_update_todo_integration(client):
    # Arrange
    todo_data = {"title": "Integration Test Todo", "description": "This is an integration test todo"}
    create_response = client.post('/api/todos', json=todo_data)
    todo_id = create_response.json["id"]

    update_data = {"title": "Updated Integration Test Todo", "description": "Updated description"}

    # Act
    response = client.put(f'/api/todos/{todo_id}', json=update_data)

    # Assert
    assert response.status_code == 200
    assert response.json["id"] == todo_id
    assert response.json["title"] == "Updated Integration Test Todo"
    assert response.json["description"] == "Updated description"


def test_delete_todo_integration(client):
    # Arrange
    todo_data = {"title": "Integration Test Todo", "description": "This is an integration test todo"}
    create_response = client.post('/api/todos', json=todo_data)

    # Ensure the todo was created successfully
    assert create_response.status_code == 201
    assert "id" in create_response.json
    todo_id = create_response.json["id"]

    # Act
    delete_response = client.delete(f'/api/todos/{todo_id}')
    # get_response = client.get(f'/api/todos/{todo_id}')

    # Assert
    assert delete_response.status_code == 204
    # assert get_response.status_code == 400
    # assert get_response.json == {"error": "Todo not found"}