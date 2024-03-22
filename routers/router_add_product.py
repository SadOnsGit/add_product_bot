from aiogram import Router, types, F
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command('start'))
async def start_message(msg: types.Message):
    if msg.from_user.id == 1112323335:
        await msg.answer('<b>Здравствуйте! Хотите добавить курс?</b>', 
                         parse_mode='html')