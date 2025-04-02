from flask import jsonify

def handle_exceptions(app):
    @app.errorhandler(ValueError)
    def handle_value_error(e):
        return jsonify({"error": str(e)}), 400

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return jsonify({"error": "An unexpected error occurred"}), 500