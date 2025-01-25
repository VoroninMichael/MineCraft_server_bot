import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from Backup_query import create_backup, get_players, restart_minecraft

bot =  os.getenv('BOT_TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=['backup'])
async def handle_backup(message: types.Message):
    create_backup()
    await message.reply("Бэкап создан.")

@dp.message_handler(commands=['restart'])
async def handle_restart(message: types.Message):
    restart_minecraft()
    await message.reply("Сервер Minecraft перезапущен.")

@dp.message_handler(commands=['players'])
async def handle_players(message: types.Message):
    players = get_players()
    await message.reply(f"Игроки на сервере:\n{players}")
