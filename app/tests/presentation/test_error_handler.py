import pytest
from flask import Flask
from app.presentation.error_handler import handle_exceptions

@pytest.fixture
def app():
    app = Flask(__name__)
    handle_exceptions(app)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_handle_value_error(client):
    # Simulate a route that raises a ValueError
    @client.application.route('/value-error')
    def value_error_route():
        raise ValueError("This is a test ValueError")

    # Act
    response = client.get('/value-error')

    # Assert
    assert response.status_code == 400
    assert response.json == {"error": "This is a test ValueError"}

def test_handle_generic_exception(client):
    # Simulate a route that raises a generic Exception
    @client.application.route('/generic-error')
    def generic_error_route():
        raise Exception("This is a test Exception")

    # Act
    response = client.get('/generic-error')

    # Assert
    assert response.status_code == 500
    assert response.json == {"error": "An unexpected error occurred"}