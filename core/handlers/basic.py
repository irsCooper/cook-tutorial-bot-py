from aiogram import Bot
from aiogram.types import Message

from core.keyboards.replay import menu_keyboard
from core.utils.text import helloUser


async def get_start(message: Message):
    await message.answer(helloUser(message.from_user.first_name), reply_markup=menu_keyboard)
    # await message.reply(f'Hello {message.from_user.first_name}') #ansver from user message

async def view_recept(message: Message):
    await message.answer()

