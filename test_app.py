import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Reset state between tests
        import app as app_module
        app_module.todos.clear()
        app_module.next_id = 1
        yield client


def test_list_todos_empty(client):
    resp = client.get("/todos")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_todo(client):
    resp = client.post("/todos", json={"title": "Buy groceries"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "Buy groceries"
    assert data["done"] is False
    assert data["id"] == 1


def test_create_todo_missing_title(client):
    resp = client.post("/todos", json={})
    assert resp.status_code == 400


def test_get_todo(client):
    client.post("/todos", json={"title": "Walk the dog"})
    resp = client.get("/todos/1")
    assert resp.status_code == 200
    assert resp.get_json()["title"] == "Walk the dog"


def test_get_todo_not_found(client):
    resp = client.get("/todos/999")
    assert resp.status_code == 404


def test_update_todo(client):
    client.post("/todos", json={"title": "Clean house"})
    resp = client.patch("/todos/1", json={"done": True})
    assert resp.status_code == 200
    assert resp.get_json()["done"] is True


def test_delete_todo(client):
    client.post("/todos", json={"title": "Delete me"})
    resp = client.delete("/todos/1")
    assert resp.status_code == 204

    resp = client.get("/todos/1")
    assert resp.status_code == 404


def test_list_todos(client):
    client.post("/todos", json={"title": "First"})
    client.post("/todos", json={"title": "Second"})
    resp = client.get("/todos")
    assert len(resp.get_json()) == 2
