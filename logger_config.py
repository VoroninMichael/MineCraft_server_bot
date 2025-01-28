import logging
import os
from logging.handlers import TimedRotatingFileHandler

'''Настройка логирования'''
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # Создаёт папку, если её нет

# Функция настройки логирования
def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Формат логов
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Ротация логов раз в сутки
    log_file = os.path.join(LOG_DIR, "app.log")
    handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1)
    handler.suffix = "%Y-%m-%d"
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(formatter)
    # logger.addHandler(console_handler)
