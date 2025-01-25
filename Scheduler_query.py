from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from Backup_query import create_backup, clean_old_backups

scheduler = BackgroundScheduler()

# Настройка расписания
scheduler.add_job(create_backup, CronTrigger(hour="*/3"))  # Каждые 3 часа
scheduler.add_job(clean_old_backups, CronTrigger(hour="4", minute="0"))  # Чистка бэкапов в 04:00
scheduler.start()
