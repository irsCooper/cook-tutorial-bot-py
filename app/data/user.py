from app.data.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, ForeignKey


class User(BaseModel):
    __tablename__ = 'users'
    
    tg_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    subscribe = Column(Boolean, default=False)
    
    def __str__(self) -> str:
        return f"<User:{self.tg_id}>"


# class User_Likes(BaseModel):
#     __tablename__ = 'user_likes'

#     owner_tg_id = Column(Integer, ForeignKey("users.tg_id"))
#     user_likes_resepy_id_fkey = Column(Integer, ForeignKey("resepy.id"))
    
#     def __str__(self) -> str:
#         return f"<User_Likes:{self.owner_tg_id}>"