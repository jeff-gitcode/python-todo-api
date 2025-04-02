from app.domain.entities import Todo
from app.domain.interfaces import TodoRepository

class CreateTodoCommand:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

class CreateTodoHandler:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def handle(self, command: CreateTodoCommand):
        todo = Todo(id=None, title=command.title, description=command.description)
        return self.repository.add(todo)