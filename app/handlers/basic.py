from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from app.keyboards.replay import menu_keyboard
from app.utils.text import helloUser

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(helloUser(message.from_user.first_name), reply_markup=menu_keyboard)
    # await message.reply(f'Hello {message.from_user.first_name}') #ansver from user message


@router.message(F.text == 'Смотреть рецепты') 
async def view_recept_handler(message: Message):
    await message.answer('text')

