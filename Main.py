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

from Backup_query import create_backup, clean_old_backups
from Service_qury import restart_minecraft, get_players
from Scheduler_query import scheduler
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

# Сшедулёр
def start_scheduler():
    """Запускает планировщика."""
    scheduler.add_job(create_backup, 'cron', hour='*/3')  # Каждые 3 часа
    scheduler.add_job(clean_old_backups, 'cron', hour=4, minute=0)  # Чистка бэкапов в 04:00
    scheduler.start()


if __name__ == "__main__":
    start_scheduler()  # Запуск планировщика
    asyncio.run(dp.start_polling())
