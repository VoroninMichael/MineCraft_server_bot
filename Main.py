import types
from dotenv import load_dotenv
import os
import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup
from aiogram import Router
from logger_config import setup_logger

from Backup_query import create_backup, clean_old_backup
from Service_qury import restart_minecraft



setup_logger()
# Логирование
logging.basicConfig(level=logging.INFO)

# Инцилизация .env
load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))

# Определяем диспетчера
dp = Dispatcher(bot)

@dp.message_handler(commands=['backup'])
async def handle_backup(message: types.Message):
    """Создает бэкап."""
    create_backup()
    await message.reply("Бэкап создан.")

@dp.message_handler(commands=['restart'])
async def handle_restart(message: types.Message):
    """Перезапускает сервер"""
    restart_minecraft()
    await message.reply("Сервер Minecraft перезапущен.")

# @dp.message_handler(commands=['players'])
# async def handle_players(message: types.Message):
#     "Получение инфы сервера"
#     players = get_players()
#     await message.reply(f"Игроки на сервере:\n{players}")



if __name__ == "__main__":
    asyncio.run(dp.start_polling())
