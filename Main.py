import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from logger_config import setup_logger
from Backup_query import create_backup, clean_old_backup
from Service_qury import restart_minecraft

# Логирование
setup_logger()
logging.basicConfig(level=logging.INFO)

# Загрузка переменных окружения
load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Обработчик команды /backup
@dp.message(Command("backup"))
async def handle_backup(message: Message):
    create_backup()
    await message.reply("Бэкап создан.")

# Обработчик команды /restart
@dp.message(Command("restart"))
async def handle_restart(message: Message):
    restart_minecraft()
    await message.reply("Сервер Minecraft перезапущен.")

# Функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
