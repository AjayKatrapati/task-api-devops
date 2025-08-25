from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@db:5432/postgres"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from . import models  # Make sure models are imported before db.create_all()

    # Add print statements to verify table creation
    with app.app_context():
        print(">>> Running db.create_all()...")   # For debugging
        db.create_all()
        print(">>> db.create_all() completed.")   # For debugging

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
