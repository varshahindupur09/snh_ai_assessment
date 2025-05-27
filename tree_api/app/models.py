from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class TreeNode(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   label: str
   parent_id: Optional[int] = Field(default=None, foreign_key="treenode.id")
   children: List["TreeNode"] = Relationship(back_populates="parent")
   parent: Optional["TreeNode"] = Relationship(back_populates="children", sa_relationship_kwargs={"remote_side": "TreeNode.id"})