import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, types
from routers.router_add_product import start_router
from callbacks.cb_main import addproduct_router

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(addproduct_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
asyncio.run(main())