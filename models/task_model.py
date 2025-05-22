# models/task_model.py

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func
from database.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(Boolean(), nullable=False)
    # createDate = Column(TIMESTAMP(), nullable=False, default=func.now())
    # lastEditDate = Column(TIMESTAMP(), nullable=True, default=func.now(), onupdate=func.now())
    user = Column(String(50), nullable=False)
    category = Column(String(25), nullable=True)
    priority = Column(String(25), nullable=False)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', description='{self.description}', status = '{self.status}', createDate = '{self.createDate}', lastEditDate = '{self.lastEditDate}', user = '{self.user}', category = '{self.category}', priority = '{self.priority}')>"
