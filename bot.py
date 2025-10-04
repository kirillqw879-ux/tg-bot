python -m venv venv
venv\Scripts\activate
pip install aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔑 Твій токен
TOKEN = 8218595704:AAGn0UaSZVlvPT1_8lZFnR5-ImEown5EptE

# Ініціалізація
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привіт! 👋 Я твій перший Telegram бот на Python!")

# Обробка звичайних повідомлень
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(f"Ти написав: {message.text}")

# Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

