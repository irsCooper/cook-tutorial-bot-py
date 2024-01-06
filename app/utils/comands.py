from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_comands(bot: Bot):
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