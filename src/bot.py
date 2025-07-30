from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio
import yaml

# Загружаем конфиг
def load_config(path="config/config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

config = load_config()
bot = Bot(token=config["bot"]["token"])
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.answer("🔹 Добро пожаловать в KriptoOrakulBot!\nБот активен и готов к работе.")

# Точка запуска
def run_bot():
    print("Бот запускается...")
    executor.start_polling(dp, skip_updates=True)

# НЕ запускать напрямую, теперь запуск идёт через main.py
