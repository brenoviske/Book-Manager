from src.database.config import Base
from sqlalchemy import Column , Integer , String , ForeignKey , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Book(Base):

        __tablename__ = "books"

        id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
        name = Column(String(200), nullable=False, index = True)
        genre = Column(String(200), nullable = False, index = True)
        description = Column(String(512), nullable=False , index=True )
        created_at = Column(DateTime, nullable = False, default=datetime.utcnow())
        user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
        user = relationship('User', back_populates = 'user', cascade = 'all, delete-orphan')

        def to_dict(self):

            return {
                'id' : self.id,
                'name' : self.name,
                'genre' : self.genre,
                'description' : self.description,
                'created_at' : self.created_at,
                'user_id' : self.user_id


            }