from typing import Optional
from app.domain.entities import User
from app.domain.interfaces import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []
        self.counter = 1

    def add(self, user: User) -> User:
        user.id = self.counter
        self.counter += 1
        self.users.append(user)
        return user

    def get_by_username(self, username: str) -> Optional[User]:
        return next((user for user in self.users if user.username == username), None)