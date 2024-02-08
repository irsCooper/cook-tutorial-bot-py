from app.data.base import BaseModel

from sqlalchemy import Column, Integer, Text, ARRAY, BINARY, ForeignKey
from sqlalchemy.orm import relationship


class Resepy(BaseModel):
    __tablename__ = 'resepy'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    owner_tg_id = Column(Integer, ForeignKey("users.tg_id"), nullable=False)
    category = Column(ARRAY(Text), nullable=False)
    name = Column(Text, nullable=False)
    cooking = Column(ARRAY(Text), nullable=False)
    photo = Column(ARRAY(BINARY))
    likes = Column(Integer, nullable=False, default=0)
    
    owner = relationship('User', backref='resepys', lazy=False)
    
    
    def __str__(self) -> str:
        return f"<Resepy:{self.id}, owner:{self.owner_tg_id}, name:{self.name}>"
    
    def __repr__(self):
        return self.__str__()