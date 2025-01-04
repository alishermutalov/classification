import asyncio
import logging
import sys

#aiogram package'lari
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from loader import dp, bot
import handlers, data




async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())