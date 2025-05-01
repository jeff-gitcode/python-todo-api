from typing import List, Optional
from app.domain.entities import Todo

class TodoRepository:
    def add(self, todo: Todo) -> Todo:
        raise NotImplementedError

    def get(self, todo_id: int) -> Optional[Todo]:
        raise NotImplementedError

    def list_all(self) -> List[Todo]:
        raise NotImplementedError

    def update(self, todo: Todo) -> Optional[Todo]:
        raise NotImplementedError

    def delete(self, todo_id: int) -> bool:
        raise NotImplementedError

from typing import Optional
from app.domain.entities import User

class UserRepository:
    def add(self, user: User) -> User:
        raise NotImplementedError

    def get_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError    