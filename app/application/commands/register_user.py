from werkzeug.security import generate_password_hash
from app.domain.entities import User
from app.domain.interfaces import UserRepository

class RegisterUserCommand:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class RegisterUserHandler:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def handle(self, command: RegisterUserCommand):
        if self.repository.get_by_username(command.username):
            raise ValueError("User already exists")
        password_hash = generate_password_hash(command.password)
        user = User(id=None, username=command.username, password_hash=password_hash)
        return self.repository.add(user)