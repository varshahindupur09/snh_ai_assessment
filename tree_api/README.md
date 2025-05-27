
# 🌳 Tree API

A production-ready HTTP API built using **FastAPI** for managing tree-like hierarchical data structures. The API supports creation of nodes with parent-child relationships and retrieves the entire tree in a nested format. Data is persisted using **SQLite**.

---

## 📦 Features

- ✅ Create tree nodes with parent-child relationships (`POST /api/tree`)
- ✅ Retrieve the full tree as a nested JSON (`GET /api/tree`)
- ✅ Persistent storage with SQLite
- ✅ Simple `curl`-based usage
- ✅ Clean project structure ready for deployment or extension

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone https://github.com/your-username/tree-api.git
cd tree-api
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the server

```
python -m uvicorn app.main:app --reload
```

The server will start at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

API documentation will be available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Add Nodes via Terminal

### Create root node

```
curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "root"}'
```

### Add bear under root

```
curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "bear", "parentId": 1}'
```

### Add cat under bear

```
curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "cat", "parentId": 2}'
```

### Add frog under root

```
curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "frog", "parentId": 1}'
```

### Add "cat’s child" under cat

```
curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "cat’s child", "parentId": 3}'
```

---

## 📥 Get the Tree Structure

```
curl http://127.0.0.1:8000/api/tree
```

### Example Response:

```
[
  {
    "id": 1,
    "label": "root",
    "children": [
      {
        "id": 2,
        "label": "bear",
        "children": [
          {
            "id": 3,
            "label": "cat",
            "children": [
              {
                "id": 5,
                "label": "cat’s child",
                "children": []
              }
            ]
          }
        ]
      },
      {
        "id": 4,
        "label": "frog",
        "children": []
      }
    ]
  }
]
```

---

## 📁 Project Structure

```
tree-api/
├── app/
│   ├── main.py         # FastAPI application
│   ├── crud.py         # Business logic for DB interaction
│   ├── models.py       # ORM models using SQLModel
│   ├── db.py           # DB connection setup
├── tests/
│   └── test_tree.py    # Pytest-based test cases
├── requirements.txt    # Python dependencies
├── README.md           # Project instructions


---

## ✅ Testing 

If you want to run automated tests:

```
cd tree_api
cd app
pytest
```