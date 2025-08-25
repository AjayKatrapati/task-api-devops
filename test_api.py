import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Ensures in-memory, isolated DB for tests
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()      # <-- This resets all tables and deletes old test data
            db.create_all()    # <-- This recreates table schema
        yield client
