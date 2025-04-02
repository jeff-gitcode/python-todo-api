from app.domain.interfaces import TodoRepository

class GetTodoQuery:
    def __init__(self, todo_id: int):
        self.todo_id = todo_id

class GetTodoHandler:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def handle(self, query: GetTodoQuery):
        todo = self.repository.get(query.todo_id)
        if not todo:
            raise ValueError("Todo not found")
        return todo