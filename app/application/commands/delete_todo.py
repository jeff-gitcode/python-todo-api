from app.domain.interfaces import TodoRepository

class DeleteTodoCommand:
    def __init__(self, todo_id: int):
        self.todo_id = todo_id

class DeleteTodoHandler:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def handle(self, command: DeleteTodoCommand):
        success = self.repository.delete(command.todo_id)
        if not success:
            raise ValueError("Todo not found")
        return success