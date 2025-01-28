import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from Backup_query import create_backup, clean_old_backup
import logging

logger = logging.getLogger(__name__)

# Асинхронные функции задач
async def everyday_backup():
    logger.info("Создание бэкапа началось...")
    create_backup()
    await asyncio.sleep(2)  # Симуляция долгой операции
    logger.info("Бэкап создан.")

async def clean_backups():
    logger.info("Начата чистка старых бэкапов...")
    clean_old_backup()
    await asyncio.sleep(2)  # Симуляция долгой операции
    logger.info("Чистка завершена.")

# Основная функция запуска
async def main():
    scheduler = AsyncIOScheduler()
    # Добавление задач в планировщик
    scheduler.add_job(create_backup, CronTrigger(hour="17-23", minute="0"), id="backup_evening")
    scheduler.add_job(create_backup, CronTrigger(hour="0-2", minute="0"), id="backup_night")
    scheduler.add_job(clean_backups, CronTrigger(hour="5", minute="0"), id="clean_backups")


# Запуск основного цикла
if __name__ == "__main__":
    asyncio.run(main())
