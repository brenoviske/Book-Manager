from src.database.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True , autoincrement=True,nullable=False)
    email = Column(String(200), nullable=False, index=True)
    username = Column(String(200), nullable=False, index=True)
    password_hash = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.now() , nullable=False)

    books = relationship("Book",back_populates="user", cascade="all, delete-orphan")

    def to_dict(self):

        return {
            'id':self.id,
            'email':self.email,
            'username':self.username,
            'created_at':self.created_at,

        }

