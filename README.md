# MineCraft_server_bot
## Бот в пайтоне, который не много упрощает администрирование сервера 

## Этот бот по сути личный не большой  проект. Он нужен мне только для того, чтоб было более комфортно играть с друзьями на серевере майнкрафт. Тут нет кода, который можно было бы взять в другой проект. Если вы случайно забрели на мой реп, то могу пожелать вам только хорошего дня 
## Все следующие записи я введу только для себя 
### Сервер по майнкрафту развернут на ВМ на убунту, на ядре mahist. Выбрали мы его потому что он включает в себя возможность работы с плагинами и с модами. Да и в принципе захотелось. Бот в принципе, наверное подойдет и для других версий майнкрафта, но в этом боте, скорее всего ввключена работа с планином rcon, а может и нет. Я еще не знаю. 

# Деплой 

###  1. Сначала требуется установить все зависимости на сервере
```
sudo apt install python3 python3-pip python3-venv git -y
```
### 2. Клонируем репозиторий
```
git clone 
```

### 3. Настроить виртуальное окружение 
```
python3 -m venv venv
source venv/bin/activate
```
* Установка зависимостей 
```
pip install -r requirements.txt

```
* Заполни файлик 
```
aiogram==3.2.0
python-dotenv==1.0.0
apscheduler==3.10.1
```

### 4. Работа с .env
* Создали файлик
```
nano .env
```
* Заполняем 
```
#Конфигурация бота

#Токен бота
BOT_TOKEN="7887888531:AAGO4ubsnL2ygTzzdHl6XamdWq3l3V4bDQU"

#Конфигурация Майнкрафт сервера
BACKUP_DIR = /opt/minecraft_server/backup

BACKUP_RETENTION_DAYS = 4
IMPORTANT_BACKUP_HOUR = 12
MINECRAFT_SERVICE = minecraft.service
MINECRAFT_WORLD_DIR = /opt/minecraft_server/ZalupnieSosiski
MINECRAFT_WORLD_NAME = ZalupnieSosiski
```
### 5. Создаем сервис 
```
[Unit]
Description=Minecraft Bot
After=network.target

[Service]
User=root
WorkingDirectory=
ExecStart=
Restart=always

[Install]
WantedBy=multi-user.target

```
* Запускаем 
```
sudo systemctl daemon-reload
sudo systemctl enable minecraft-bot
sudo systemctl start minecraft-bot
```
* Навсякий 
```
systemctl status minecraft-bot
```
## Штука для обновления кода
### В директории создадим файлик 
```
nano update_bot.sh
```
### Заполнили
```
#!/bin/bash
cd 
git pull
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart minecraft-bot
```
### Сделали исполнямым 
```
chmod +x update_bot.sh
```
* Если надо обновить, то просто запускаем update файл 



Скорее всего нужен будет исполняемый файл 
start.sh 
```
#!/bin/bash
source /home/your-user/bot/venv/bin/activate
python main.py &
python scheduler.py &
wait
```