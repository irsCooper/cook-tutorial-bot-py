from app.data.base import BaseModel
from sqlalchemy import Column, Integer, Text, ARRAY, BINARY


class Resepy(BaseModel):
    __tablename__ = 'resepy'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    owner_tg_td = Column(Integer, nullable=False)
    category = Column(ARRAY(Text), nullable=False)
    name = Column(Text, nullable=False)
    cooking = Column(ARRAY(Text), nullable=False)
    photo = Column(ARRAY(BINARY))
    likes = Column(Integer, nullable=False, default=0)
    
    def __str__(self) -> str:
        return f"<Resepy:{self.id}, owner:{self.owner_tg_td}, name:{self.name}>"