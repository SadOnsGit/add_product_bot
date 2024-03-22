from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Добавить курс', callback_data='add.course')
    ]
])