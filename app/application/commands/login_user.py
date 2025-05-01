from werkzeug.security import check_password_hash
import jwt
import datetime
from app.domain.interfaces import UserRepository

SECRET_KEY = "your_secret_key"

class LoginUserCommand:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class LoginUserHandler:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def handle(self, command: LoginUserCommand):
        user = self.repository.get_by_username(command.username)
        if not user or not check_password_hash(user.password_hash, command.password):
            raise ValueError("Invalid username or password")
        token = jwt.encode({
            "username": user.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm="HS256")
        return token