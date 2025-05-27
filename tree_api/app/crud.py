from sqlalchemy.orm import Session
from .models import TreeNode

def create_node(db: Session, label: str, parent_id: int | None = None):
    node = TreeNode(label=label, parent_id=parent_id)
    db.add(node)
    db.commit()
    db.refresh(node)
    return node

def get_tree(db: Session):
    nodes = db.query(TreeNode).all()
    id_map = {node.id: {"id":node.id, "label":node.label, "children": [] } for node in nodes}
    root_nodes = []
    for node in nodes:
        if node.parent_id:
            parent = id_map[node.parent_id]
            parent["children"].append(id_map[node.id])
        else:
            root_nodes.append(id_map[node.id])
    return root_nodes
