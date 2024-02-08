from app.data.base import BaseModel

from sqlalchemy import Column, Integer, Boolean, ForeignKey, select
from sqlalchemy.orm import sessionmaker, selectinload, relationship
from sqlalchemy.exc import ProgrammingError

from redis.asyncio.client import Redis


class User(BaseModel):
    __tablename__ = 'users'
    
    tg_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    subscribe = Column(Boolean, default=False)
    
    resepys = relationship('Resepy', back_populates='owner', lazy=False)
    
    
    def __str__(self) -> str:
        return f"<User:{self.tg_id}>"
    
    def __repr__(self):
        return self.__str__()
 
    
    
async def get_user(tg_id: int, session_maker: sessionmaker) -> User:
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(User)
                    .options(selectinload(User.resepys))
                    .filter(User.tg_id == tg_id)
            )
            return result.scalars().one()
        
        
async def create_user(tg_id: int, session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            user = User(
                tg_id=tg_id,
                subsctibe=False
            )
            
            try:
                session.add(user)
            except ProgrammingError as e:
                # TODO
                pass
            

async def is_user_exist(tg_id: int, session_maker: sessionmaker, redis: Redis) -> bool:
    res = await redis.get(name='is_user_exists:' + str(tg_id))
    if not res:
        async with session_maker() as session:
            async with session.begin():
                sql_res = await session.execute(select(User).where(User.tg_id == tg_id))
                await redis.set(name='is_user_exists:' + str(tg_id), value=1 if sql_res else 0)
                return bool(sql_res)
    else:
        return bool(res)
    

            
    
    
    
    
    
    
    
    
    

class User_Likes(BaseModel):
    __tablename__ = 'user_likes'

    id = Column(Integer, primary_key=True)
    owner_tg_id = Column(Integer, ForeignKey("users.tg_id"))
    user_likes_resepy_id_fkey = Column(Integer, ForeignKey("resepy.id"))
    
    def __str__(self) -> str:
        return f"<User_Likes:{self.owner_tg_id}>"