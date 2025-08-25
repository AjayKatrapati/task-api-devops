import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_task(client):
    response = client.post("/tasks", json={"title": "Test task", "description": "pytest demo"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test task"
    assert data["description"] == "pytest demo"
    assert data["done"] is False

    # Check task is returned in task list
    response = client.get("/tasks")
    tasks = response.get_json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test task"
