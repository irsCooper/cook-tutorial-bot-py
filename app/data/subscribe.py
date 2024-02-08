from app.data.base import BaseModel
from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey


class Subscribe(BaseModel):
    __tablename__ = 'subscribes'

    owner_tg_id = Column(Integer, ForeignKey("users.tg_id"), unique=True, nullable=False)
    start_date = Column(TIMESTAMP, nullable=False)
    theend_date = Column(TIMESTAMP, nullable=False)
    
    def __str__(self) -> str:
        return f"<Subscribe:{self.owner_tg_id}, start:{self.start_date}>"