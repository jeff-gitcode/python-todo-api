from app.domain.entities import Todo
from app.domain.interfaces import TodoRepository

class UpdateTodoCommand:
    def __init__(self, todo_id: int, title: str, description: str):
        self.todo_id = todo_id
        self.title = title
        self.description = description

class UpdateTodoHandler:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def handle(self, command: UpdateTodoCommand):
        todo = self.repository.get(command.todo_id)
        if not todo:
            raise ValueError("Todo not found")
        todo.update(title=command.title, description=command.description)
        return self.repository.update(todo)