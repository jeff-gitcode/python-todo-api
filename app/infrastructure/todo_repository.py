from typing import List, Optional
from app.domain.entities import Todo
from app.domain.interfaces import TodoRepository

class InMemoryTodoRepository(TodoRepository):
    def __init__(self):
        self.todos = []
        self.counter = 1

    def add(self, todo: Todo) -> Todo:
        todo.id = self.counter
        self.counter += 1
        self.todos.append(todo)
        return todo

    def get(self, todo_id: int) -> Optional[Todo]:
        return next((todo for todo in self.todos if todo.id == todo_id), None)

    def list_all(self) -> List[Todo]:
        return self.todos

    def update(self, todo: Todo) -> Optional[Todo]:
        for i, t in enumerate(self.todos):
            if t.id == todo.id:
                self.todos[i] = todo
                return todo
        return None

    def delete(self, todo_id: int) -> bool:
        todo = self.get(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False