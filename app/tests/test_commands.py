from app.core.commands.create_todo import CreateTodoCommand
from app.core.commands.update_todo import UpdateTodoCommand
from app.domain.models import Todo
from app.infrastructure.repositories import TodoRepository

class TestCreateTodoCommand:
    def test_execute_creates_todo(self):
        repository = TodoRepository()
        command = CreateTodoCommand(repository)
        todo_data = {"title": "Test Todo", "description": "Test Description"}
        
        todo = command.execute(todo_data)
        
        assert todo.id is not None
        assert todo.title == todo_data["title"]
        assert todo.description == todo_data["description"]
        assert todo.completed is False

class TestUpdateTodoCommand:
    def test_execute_updates_todo(self):
        repository = TodoRepository()
        command = UpdateTodoCommand(repository)
        todo = Todo(id=1, title="Old Title", description="Old Description", completed=False)
        repository.add(todo)
        
        updated_data = {"title": "Updated Title", "description": "Updated Description"}
        command.execute(todo.id, updated_data)
        
        updated_todo = repository.get(todo.id)
        
        assert updated_todo.title == updated_data["title"]
        assert updated_todo.description == updated_data["description"]