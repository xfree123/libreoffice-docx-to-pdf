from flask import Flask
from .routes import convert_bp
from .logging_config import setup_logging

def create_app():
    setup_logging()  

    app = Flask(__name__)
    app.register_blueprint(convert_bp)

    @app.route("/health")
    def health():
        return "OK", 200

    return app
