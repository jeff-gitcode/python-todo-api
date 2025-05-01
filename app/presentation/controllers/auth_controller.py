from flask import Blueprint, request, jsonify
from app.application.commands.register_user import RegisterUserCommand, RegisterUserHandler
from app.application.commands.login_user import LoginUserCommand, LoginUserHandler
from app.infrastructure.user_repository import InMemoryUserRepository
from app.application.mediator import Mediator

auth_controller = Blueprint('auth_controller', __name__)

# Initialize repository and mediator
user_repository = InMemoryUserRepository()
mediator = Mediator()

# Register handlers
mediator.register(RegisterUserCommand, RegisterUserHandler(user_repository))
mediator.register(LoginUserCommand, LoginUserHandler(user_repository))

@auth_controller.route('/auth/register', methods=['POST'])
def register_user():
    """
    Register a new user
    ---
    tags:
      - Auth
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: "newuser"
            password:
              type: string
              example: "newpassword123"
    responses:
      201:
        description: User registered successfully
      400:
        description: User already exists
    """
    data = request.json
    command = RegisterUserCommand(username=data['username'], password=data['password'])
    try:
        user = mediator.send(command)
        return jsonify({"id": user.id, "username": user.username}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auth_controller.route('/auth/login', methods=['POST'])
def login_user():
    """
    Login a user
    ---
    tags:
      - Auth
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: "newuser"
            password:
              type: string
              example: "newpassword123"
    responses:
      200:
        description: Login successful
        schema:
          type: object
          properties:
            token:
              type: string
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      401:
        description: Invalid credentials
    """
    data = request.json
    command = LoginUserCommand(username=data['username'], password=data['password'])
    try:
        token = mediator.send(command)
        return jsonify({"token": token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401