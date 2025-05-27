from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_root_node():
    response = client.post("/api/tree", json={"label": "root"})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] == "root"
    assert data["parent_id"] is None

def test_add_child_node():
    # create root
    client.post("/api/tree", json={"label": "root"})
    # add child
    response = client.post("/api/tree", json={"label": "child", "parentId": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["label"] == "child"
    assert data["parent_id"] == 1

def test_get_tree_structure():
    response = client.get("/api/tree")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["label"] == "root"