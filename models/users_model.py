
from sqlalchemy import Column, Integer, String, DateTime, func
from database.db import Base
from sqlalchemy.orm import relationship 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    createDate = Column(DateTime(timezone = True), nullable=False, default=func.now())
    
    tasks = relationship("Task", backref = "user_rel", order_by = "Task.createDate")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', password='{self.password}', createDate = '{self.createDate}')>"

