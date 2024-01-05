from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart

from core.handlers.basic import get_start
from core.utils.comands import set_comands
from core.settings import settings

from asyncio import run
import logging


async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.token, parse_mode='HTML')

    dp = Dispatcher() 


    # dp.startup.register(admin_info_start_bot)
    # dp.shutdown.register(admin_info_stop_bot)
    dp.message.register(get_start, CommandStart)
    # dp.message.register(, F.text == 'Смотреть рецепты')
    # dp.message.register(, F.text == 'Добавить')
    # dp.message.register(, F.text == 'Мои рецепты')
    # dp.message.register(, F.text == 'Избранное')


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
    run(start())
