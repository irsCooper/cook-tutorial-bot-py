from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart

from app.handlers import basic
from app.utils.comands import set_comands
from app.settings import settings

from app.data.base import BaseModel
from app.data.engine import create_async_engine, get_sesson_maker, procced_schemas
from sqlalchemy.engine import URL

import asyncio
import logging


async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.token, parse_mode='HTML')
    dp = Dispatcher() 

    dp.include_routers(
        basic.router
    )

    # команды которые отображаются в кнопке меню
    await set_comands(bot)
    
    async_engine = create_async_engine(
        URL.create(
            settings.db.mode,
            settings.db.user,
            settings.db.password,
            settings.db.host,
            settings.db.port,
            settings.db.db_name,
        )
    )
    
    # session_maker = get_sesson_maker(async_engine)
    await procced_schemas(async_engine, BaseModel.metadata)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()





# async def admin_info_start_bot(bot: Bot):
#     await bot.send_message(settings.bots.admin_id, "Bot Started")


# async def admin_info_stop_bot(bot: Bot):
#     await bot.send_message(settings.bots.admin_id, "Bot Stoped")


if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.error(msg='exit')
