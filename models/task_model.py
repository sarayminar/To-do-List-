# models/task_model.py

from sqlalchemy import Column, Integer, String, Boolean
from database.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(Boolean(), nullable=False)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', description='{self.description}', status = '{self.status}')>"
