from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from .models import SQLModel, TreeNode
from .db import engine, get_session
from .crud import create_node, get_tree

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/api/tree")
def read_tree(session: Session = Depends(get_session)):
    return get_tree(session)

@app.post("/api/tree")
def add_node(data: dict, session: Session = Depends(get_session)):
    label = data.get("label")
    parent_id = data.get("parentId")
    if not label:
        raise HTTPException(status_code=400, detail="Label is required")
    return create_node(session, label, parent_id)
