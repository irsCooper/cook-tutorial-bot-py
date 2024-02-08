import asyncio
import calendar
import logging
import os.path
from operator import itemgetter

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import (
    PrevPage, Row, ScrollingGroup, StubScroll, SwitchTo,
)
from aiogram_dialog.widgets.text import Const, Format, ScrollingText, List


class DialogSG(StatesGroup):
    MAIN = State()
    PAGERS = State()
    STUB = State()



async def product_getter(**_kwargs):
    return {
        "products": [(f"Product {i}", i) for i in range(1, 30)],
    }


async def paging_getter(dialog_manager: DialogManager, **_kwargs):
    current_page = await dialog_manager.find("stub_scroll").get_page()
    return {
        "pages": 7,
        "current_page": current_page + 1,
        "day": calendar.day_name[current_page],
    }


MAIN_MENU_BTN = SwitchTo(Const("Main menu"), id="main", state=DialogSG.MAIN)

dialog = Dialog(
    Window(
        Const("Scrolling variant demo. Please, select an option:"),
        SwitchTo(Const("Pager options"), id="pagers", state=DialogSG.PAGERS),
        SwitchTo(Const("Stub: getter-based"), id="stub", state=DialogSG.STUB),
        state=DialogSG.MAIN,
    ),
    
    
    
    
    
    Window(
        Const("Scrolling group with external paging controls"),
        ScrollingGroup(
            # тут можно сделать выбор категорий
            Multiselect(
                Format("✓ {item[0]}"),
                Format("{item[0]}"),
                id="ms",
                items="products",
                item_id_getter=itemgetter(1),
            ),
            width=1,
            height=5,
            hide_pager=True,
            id="scroll_no_pager",
        ),
        # пролистывание
        Row(
            PrevPage(
                scroll="scroll_no_pager",
            ),
            CurrentPage(
                scroll="scroll_no_pager", text=Format("{current_page1}"),
            ),
            NextPage(
                scroll="scroll_no_pager",
            ),
        ),
        Row(
            MAIN_MENU_BTN,
        ),
        getter=product_getter,
        state=DialogSG.PAGERS,
    ),
    
    
    
    
    
    
    Window(
        Const("Stub Scroll. Getter is used to paginate\n"),
        Format("You are at page {current_page} of {pages}"),
        Format("Day by number is {day}"),
        StubScroll(id="stub_scroll", pages="pages"),
        NumberedPager(
            scroll="stub_scroll",
        ),
        MAIN_MENU_BTN,
        state=DialogSG.STUB,
        getter=paging_getter,
    ),
)




async def start(message: Message, query: CallbackQuery, dialog_manager: DialogManager):
    # it is important to reset stack because user wants to restart everything
    await dialog_manager.start(DialogSG.MAIN, mode=StartMode.RESET_STACK)
    query.data["ms"]


async def main():
    # real main
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token="6655761053:AAG00-oOS9OlFMIuWIhl3UpjeqgOKqDphKQ")

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.message.register(start, CommandStart())
    dp.include_router(dialog)
    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())













# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command, CommandStart

# from app.handlers.start import router as start_router
# from app.utils.menu_comands import set_comands
# from app.utils.logging import create_logger, DEBUG, LOGER
# from app.middlewares.register_check import RegisterCheck
# from app.settings import settings

# from app.data.base import BaseModel
# from app.data.engine import create_async_engine, get_sesson_maker

# from sqlalchemy.engine import URL

# import asyncio
# import logging


# async def start():
    
#     await create_logger(DEBUG)
    
#     bot = Bot(token=settings.bots.token, parse_mode='HTML')
#     dp = Dispatcher() 
    
#     dp.message.middleware(RegisterCheck())
#     dp.callback_query.middleware(RegisterCheck())

#     dp.include_routers(
#         start_router
#     )

#     # команды которые отображаются в кнопке меню
#     await set_comands(bot)
    
#     async_engine = create_async_engine(
#         URL.create(
#             settings.db.mode,
#             settings.db.user,
#             settings.db.password,
#             settings.db.host,
#             settings.db.port,
#             settings.db.db_name,
#         )
#     )
    
#     session_maker = get_sesson_maker(async_engine)


#     try:
#         await dp.start_polling(bot, session_maker=session_maker, bott=bot)
#     finally:
#         await bot.session.close()





# # async def admin_info_start_bot(bot: Bot):
# #     await bot.send_message(settings.bots.admin_id, "Bot Started")


# # async def admin_info_stop_bot(bot: Bot):
# #     await bot.send_message(settings.bots.admin_id, "Bot Stoped")


# if __name__ == '__main__':
#     try:
#         asyncio.run(start())
#     except KeyboardInterrupt:
#         logging.error(msg='exit')
