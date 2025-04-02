import sys
import os
from flask import Flask
from flasgger import Swagger

# Dynamically add the project root directory to sys.path
routePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print("routePath: ", routePath)
sys.path.append(routePath)

from app.presentation.error_handler import handle_exceptions
from app.presentation.controllers.todo_controller import todo_controller

apps = Flask(__name__)
apps.register_blueprint(todo_controller, url_prefix='/api')

# Register global error handlers
handle_exceptions(apps)

# Initialize Swagger
swagger = Swagger(apps)

if __name__ == '__main__':
    apps.run(debug=True)