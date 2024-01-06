from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart

from app.handlers import basic
from app.utils.comands import set_comands
from app.settings import settings

import asyncio
import logging


async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.token, parse_mode='HTML')

    dp = Dispatcher() 

    dp.include_routers(
        basic.router
    )

    await set_comands(bot)

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
