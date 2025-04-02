from app.domain.interfaces import TodoRepository

class GetTodosQuery:
    pass

class GetTodosHandler:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def handle(self, query: GetTodosQuery):
        return self.repository.list_all()