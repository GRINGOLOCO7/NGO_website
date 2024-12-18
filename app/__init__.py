from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes
    from .routes import main

    # Register routes
    app.register_blueprint(main)

    return app
