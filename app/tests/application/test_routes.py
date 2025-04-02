# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)

# def test_create_todo():
#     response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description"})
#     assert response.status_code == 201
#     assert response.json()["title"] == "Test Todo"

# def test_get_todo():
#     response = client.get("/todos/1")
#     assert response.status_code == 200
#     assert "title" in response.json()

# def test_update_todo():
#     response = client.put("/todos/1", json={"title": "Updated Todo", "description": "Updated Description"})
#     assert response.status_code == 200
#     assert response.json()["title"] == "Updated Todo"

# def test_delete_todo():
#     response = client.delete("/todos/1")
#     assert response.status_code == 204

# def test_get_nonexistent_todo():
#     response = client.get("/todos/999")
#     assert response.status_code == 404