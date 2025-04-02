import pytest
from app.application.mediator import Mediator

class MockHandler:
    def handle(self, request):
        return f"Handled {request}"

class MockRequest:
    pass

class AnotherMockRequest:
    pass

@pytest.fixture
def mediator():
    return Mediator()

def test_register_handler(mediator):
    # Arrange
    handler = MockHandler()

    # Act
    mediator.register(MockRequest, handler)

    # Assert
    assert MockRequest in mediator._handlers
    assert mediator._handlers[MockRequest] == handler

def test_register_multiple_handlers(mediator):
    # Arrange
    handler1 = MockHandler()
    handler2 = MockHandler()

    # Act
    mediator.register(MockRequest, handler1)
    mediator.register(AnotherMockRequest, handler2)

    # Assert
    assert MockRequest in mediator._handlers
    assert AnotherMockRequest in mediator._handlers
    assert mediator._handlers[MockRequest] == handler1
    assert mediator._handlers[AnotherMockRequest] == handler2

def test_register_overwrite_handler(mediator):
    # Arrange
    handler1 = MockHandler()
    handler2 = MockHandler()

    # Act
    mediator.register(MockRequest, handler1)
    mediator.register(MockRequest, handler2)  # Overwrite the handler for MockRequest

    # Assert
    assert MockRequest in mediator._handlers
    assert mediator._handlers[MockRequest] == handler2  # Ensure the handler was overwritten

def test_register_invalid_handler(mediator):
    # Arrange
    invalid_handler = None  # Invalid handler

    # Act & Assert
    with pytest.raises(TypeError):
        mediator.register(MockRequest, invalid_handler)