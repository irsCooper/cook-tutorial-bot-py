from aiogram.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup
from aiogram_dialog.widgets.text import Const

from app.data.user import get_user

from sqlalchemy.orm import sessionmaker


class State_User_Recepys(StatesGroup):
    menu = State() # выбор
    view_resepys = State() # просмотр
    dell_one_resept = State() # удаление
    
    

