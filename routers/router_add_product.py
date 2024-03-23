from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards.mkp_main import markup_main


start_router = Router()

@start_router.message(Command('start'))
async def start_message(msg: types.Message):
    if msg.from_user.id == 1112323335:
        await msg.answer('<b>Здравствуйте! Хотите добавить курс?</b>', 
                         parse_mode='html', reply_markup=markup_main)
    else:
        await msg.answer('Нет доступа')