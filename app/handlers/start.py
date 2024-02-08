from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext


from aiogram_dialog import Dialog

from app.keyboards.replay.menu import menu_keyboard
from app.utils.text import msg_start

from app.data.user import get_user

from sqlalchemy.orm import sessionmaker

router: Router = Router()

@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(msg_start(message.from_user.first_name), reply_markup=menu_keyboard)
    # await message.reply(f'Hello {message.from_user.first_name}') #ansver from user message


    


            