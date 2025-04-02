from flask import Blueprint, request, jsonify
from app.application.commands.delete_todo import DeleteTodoCommand, DeleteTodoHandler
from app.application.mediator import Mediator
from app.application.commands.create_todo import CreateTodoCommand, CreateTodoHandler
from app.application.commands.update_todo import UpdateTodoCommand, UpdateTodoHandler
from app.application.queries.get_todo import GetTodoHandler, GetTodoQuery
from app.application.queries.get_todos import GetTodosQuery, GetTodosHandler
from app.infrastructure.todo_repository import InMemoryTodoRepository

todo_controller = Blueprint('todo_controller', __name__)

# Initialize repository and mediator
repository = InMemoryTodoRepository()
mediator = Mediator()

# Register handlers
mediator.register(CreateTodoCommand, CreateTodoHandler(repository))
mediator.register(GetTodosQuery, GetTodosHandler(repository))
mediator.register(UpdateTodoCommand, UpdateTodoHandler(repository))
mediator.register(DeleteTodoCommand, DeleteTodoHandler(repository))
mediator.register(GetTodoQuery, GetTodoHandler(repository))

@todo_controller.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    command = CreateTodoCommand(title=data['title'], description=data.get('description'))
    todo = mediator.send(command)
    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    }), 201

@todo_controller.route('/todos', methods=['GET'])
def get_todos():
    query = GetTodosQuery()
    todos = mediator.send(query)
    return jsonify([{
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    } for todo in todos]), 200

@todo_controller.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    # Use a query to fetch the todo by ID
    query = GetTodoQuery(todo_id=todo_id)
    todo = mediator.send(query)
    print("todo", todo)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed
    }), 200

@todo_controller.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    # Parse request data
    data = request.json
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Use a command to update the todo
    command = UpdateTodoCommand(todo_id=todo_id, title=data['title'], description=data['description'])
    try:
        updated_todo = mediator.send(command)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

    return jsonify({
        "id": updated_todo.id,
        "title": updated_todo.title,
        "description": updated_todo.description,
        "completed": updated_todo.completed
    }), 200

@todo_controller.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    command = DeleteTodoCommand(todo_id=todo_id)
    try:
        mediator.send(command)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    return '', 204