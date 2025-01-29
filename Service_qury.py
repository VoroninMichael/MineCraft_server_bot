import subprocess
import logging
logger = logging.getLogger(__name__)

MINECRAFT_SERVICE = "minecraft.service"

def restart_minecraft():
    """Перезапускает сервис Minecraft."""
    try:
        subprocess.run(["systemctl", "restart", MINECRAFT_SERVICE], check=True)
        logger.info("Minecraft перезапущен.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка перезапуска Minecraft: {e}")

# def get_players():
#     """Получает список игроков на сервере."""
#     try:
#         result = subprocess.run(["minecraft-rcon", "list"], capture_output=True, text=True, check=True)
#         return result.stdout.strip()
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка получения списка игроков: {e}")
#         return "Не удалось получить список игроков."
