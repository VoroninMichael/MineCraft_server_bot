import logging
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("async_scheduler.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Асинхронные функции задач
async def create_backup():
    logger.info("Создание бэкапа началось...")
    await asyncio.sleep(2)  # Симуляция долгой операции
    logger.info("Бэкап создан.")

async def clean_old_backups():
    logger.info("Начата чистка старых бэкапов...")
    await asyncio.sleep(2)  # Симуляция долгой операции
    logger.info("Чистка завершена.")

# Основная функция запуска
async def main():
    scheduler = AsyncIOScheduler()

    # Добавление задач в планировщик
    scheduler.add_job(create_backup, CronTrigger(hour="17-23", minute="0"), id="backup_evening")
    scheduler.add_job(create_backup, CronTrigger(hour="0-2", minute="0"), id="backup_night")
    scheduler.add_job(clean_old_backups, CronTrigger(hour="5", minute="0"), id="clean_backups")

    # Логи задач при запуске
    logger.info("Планировщик задач запущен.")
    for job in scheduler.get_jobs():
        logger.info(f"Запланированная задача: {job}")

    scheduler.start()

    try:
        # Ожидание завершения работы (или прерывания)
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Остановка планировщика...")
        scheduler.shutdown()
        logger.info("Планировщик остановлен.")

# Запуск основного цикла
if __name__ == "__main__":
    asyncio.run(main())
