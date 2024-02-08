from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from app.utils.logging import LOGER


async def set_comands(bot: Bot):
    LOGER.debug(msg='set_comands')
    comands = [
        BotCommand(
            command='start',
            description='Начало работы'
        )
        # BotCommand(
        #     command='',
        #     description=''
        # ),
        # BotCommand(
        #     command='',
        #     description=''
        # ),
        # BotCommand(
        #     command='',
        #     description=''
        # ),
        # BotCommand(
        #     command='',
        #     description=''
        # ),
        # BotCommand(
        #     command='',
        #     description=''
        # )
    ]

    await bot.set_my_commands(comands, BotCommandScopeDefault())