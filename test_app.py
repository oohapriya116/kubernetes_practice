
from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "To-Do Application"
    assert len(response.json["tasks"]) == 2

def test_add_task():
    client = app.test_client()
    response = client.post(
        "/tasks",
        json={"task": "Prepare Kubernetes assignment"}
    )
    assert response.status_code == 201
    assert response.json["task"] == "Prepare Kubernetes assignment"

def test_add_empty_task():
    client = app.test_client()
    response = client.post("/tasks", json={"task": ""})
    assert response.status_code == 400

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
