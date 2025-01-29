import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

import logging
logger = logging.getLogger(__name__)

load_dotenv()
backup_dir =  os.getenv("BACKUP_DIR")
world_dir = os.getenv("MINECRAFT_WORLD_DIR")
world_name = os.getenv("MINECRAFT_WORLD_NAME")
retantion_days = os.getenv("BACKUP_RETENTION_DAYS")
imprtant_hour = os.getenv("IMPORTANT_BACKUP_HOUR")

def sosal ():
    """Проверка папки бэкапа на ее наличие """
    if os.makedirs(backup_dir, exist_ok=True):
        logger.info( "Папка с бэкапами найдена")
    else:
        logger.info("Папка с бэкапами не найдена")

def create_backup():
    """Создает бэкап мира."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = Path(backup_dir) / f"{world_name}_{timestamp}.tar.gz"
    world_path = Path(world_dir) / f"{world_dir}"
    try:
        subprocess.run([
            "tar", "-czf", str(backup_path),str(world_path), "."
        ], check=True)
        logger.info(f"Бэкап создан: {backup_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка создания бэкапа: {e}")

def clean_old_backup():
    """Удаляет старые бэкапы, оставляя только важные."""
    now = datetime.now()
    retention_time = now - timedelta(days = retantion_days)
    for backup_file in Path(backup_dir).iterdir():
        if backup_file.is_file() and backup_file.suffix == ".gz":
            backup_time = datetime.strptime(backup_file.stem.split("_")[1], "%Y-%m-%d")
            if backup_time < retention_time:
                # Проверяем, что это не важный бэкап
                if not (backup_time.hour == imprtant_hour and backup_time.date() == (now - timedelta(days=1)).date()):
                    os.remove(backup_file)
                    logger.info(f"Удален старый бэкап: {backup_file}")
