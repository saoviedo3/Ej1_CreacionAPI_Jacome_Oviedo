from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .models import db, Product
from .routes import configure_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    configure_routes(app)
    
    return app

app = create_app()
