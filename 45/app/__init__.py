# app/__init__.py
from flask import Flask
from flask_wtf import CSRFProtect
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    csrf = CSRFProtect(app)
    
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
