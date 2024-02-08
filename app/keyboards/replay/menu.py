from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# встроенная 
menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Смотреть рецепты'
        )
    ],
    [
        KeyboardButton(
            text='Добавить'
        ),
        KeyboardButton(
            text='Мои рецепты'
        ),
        KeyboardButton(
            text='Избранное'
        )
    ]
], resize_keyboard=True, input_field_placeholder='Нажми на кнопку 👇')
# one_time_keyboard - появиться на один раз - false - останется на долго
# input_field_placeholder - подсказка в строке ввода сообщения
# selective -если бот в группе то клавиатура появиться только у одного
