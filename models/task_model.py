# models/task_model.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from database.db import Base
from models.users_model import User
from sqlalchemy.orm import relationship 

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(Boolean(), nullable=False)
    createDate = Column(DateTime(timezone = True), nullable=False, default=func.now())
    lastEditDate = Column(DateTime(timezone = True), nullable=True, default=func.now(), onupdate=func.now())
    # user = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable=False, index = True)
    category = Column(String(25), nullable=True)
    priority = Column(String(25), nullable=False)

    user = relationship("User")

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', description='{self.description}', status = '{self.status}', createDate = '{self.createDate}', lastEditDate = '{self.lastEditDate}', user_id = '{self.user_id}', category = '{self.category}', priority = '{self.priority}')>"

