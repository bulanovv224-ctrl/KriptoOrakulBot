from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio
import yaml
from datetime import datetime

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

# Обработка команды /замены
@dp.message_handler(commands=["замены"])
async def replacements_command(message: Message):
    ALLOWED_USERS = [26072022]  # ← Укажи свой Telegram ID

    if message.from_user.id not in ALLOWED_USERS:
        await message.answer("❌ У вас нет доступа к этой команде.")
        return

    try:
        with open("data/replacement_log.yaml", "r", encoding="utf-8") as f:
            log = yaml.safe_load(f)
    except FileNotFoundError:
        await message.answer("❗ Файл истории замен не найден.")
        return

    if not log or "replacements" not in log or not log["replacements"]:
        await message.answer("🔸 История замен пока пуста.")
        return

    reply = "🔁 История замен токенов:\n\n"
    for item in reversed(log["replacements"][-5:]):  # последние 5
        reply += (
            f"📆 {item['date']}\n"
            f"➖ {item['removed']} → ➕ {item['added']}\n"
            f"🔍 Причина: {item['reason']}\n\n"
        )

    await message.answer(reply)

# Точка запуска
def run_bot():
    print("Бот запускается...")
    executor.start_polling(dp, skip_updates=True)

# НЕ запускать напрямую, теперь запуск идёт через main.py
