from aiogram.types import Message, CallbackQuery
from aiogram import BaseMiddleware, Bot

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import ScalarResult
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from typing import Callable, Dict, Any, Awaitable

from app.data.user import User
from app.settings import settings


class RegisterCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        session_maker: sessionmaker = data['session_maker']
        bot: Bot = data['bott']
        async with session_maker() as session:
            async with session.begin():
                result = await session.execute(select(User).where(User.tg_id == event.from_user.id))
                user = result.one_or_none()
                
                if user is not None:
                    await bot.send_message(
                        chat_id=settings.bots.admin_id,
                        text=f'Новый пользователь! id: {event.from_user.id}, name: {event.from_user.first_name}', 
                    )
                    pass
                else:
                    user = User(
                        tg_id=event.from_user.id,
                        subscribe=False
                    )
                    await session.merge(user)
                    
                    await bot.send_message(
                        chat_id=settings.bots.admin_id,
                        text=f'id: {event.from_user.id}, name: {event.from_user.first_name}', 
                    )
                    
                    # оставлю на будущее как подсказку, если сообщение | если нажали на кнопку
                        # if isinstance(event, Message):
                    
                    
                
        return await handler(event, data)
        
    