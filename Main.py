import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ParseMode
from apscheduler.schedulers.background import BackgroundScheduler
from Backup_query import create_backup, clean_old_backups
from Service_qury import restart_minecraft, get_players
from Scheduler_query import scheduler
from config import BOT_TOKEN

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Убедимся, что директория для бэкапов существует
os.makedirs("./backups", exist_ok=True)

# Команды для работы с ботом
@dp.message_handler(commands=['backup'])
async def handle_backup(message: types.Message):
    """Создает бэкап мира."""
    create_backup()
    await message.reply("Бэкап создан.")

@dp.message_handler(commands=['restart'])
async def handle_restart(message: types.Message):
    """Перезапускает сервер Minecraft."""
    restart_minecraft()
    await message.reply("Сервер Minecraft перезапущен.")

@dp.message_handler(commands=['players'])
async def handle_players(message: types.Message):
    """Отправляет список игроков на сервере."""
    players = get_players()
    await message.reply(f"Игроки на сервере:\n{players}")

# Функция для запуска планировщика и бота
def start_scheduler():
    """Запускает планировщик для бэкапов и чистки старых бэкапов."""
    scheduler.add_job(create_backup, 'cron', hour='*/3')  # Каждые 3 часа
    scheduler.add_job(clean_old_backups, 'cron', hour=4, minute=0)  # Чистка бэкапов в 04:00
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()  # Запуск планировщика
    executor.start_polling(dp, skip_updates=True)  # Запуск бота
