import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from config import BACKUP_DIR, BACKUP_RETENTION_DAYS, IMPORTANT_BACKUP_HOUR

def create_backup():
    """Создает бэкап мира."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = Path(BACKUP_DIR) / f"backup_{timestamp}.tar.gz"
    try:
        subprocess.run([
            "tar", "-czf", str(backup_path), "--directory=/path/to/minecraft/world", "."
        ], check=True)
        print(f"Бэкап создан: {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка создания бэкапа: {e}")

def clean_old_backups():
    """Удаляет старые бэкапы, оставляя только важные."""
    now = datetime.now()
    retention_time = now - timedelta(days=BACKUP_RETENTION_DAYS)
    for backup_file in Path(BACKUP_DIR).iterdir():
        if backup_file.is_file() and backup_file.suffix == ".gz":
            backup_time = datetime.strptime(backup_file.stem.split("_")[1], "%Y-%m-%d")
            if backup_time < retention_time:
                # Проверяем, что это не важный бэкап
                if not (backup_time.hour == IMPORTANT_BACKUP_HOUR and backup_time.date() == (now - timedelta(days=1)).date()):
                    os.remove(backup_file)
                    print(f"Удален старый бэкап: {backup_file}")
