
from sqlalchemy import Column, Integer, String, DateTime, func
from database.base import Base
from sqlalchemy.orm import relationship 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    createDate = Column(DateTime(timezone = True), nullable=False, default=func.now())
    
    tasks = relationship("Task", order_by = "Task.createDate", back_populates="user", cascade = "all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', createDate = '{self.createDate}')>"

