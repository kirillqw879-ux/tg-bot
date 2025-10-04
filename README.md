# Telegram Bot на Python

Цей бот створений для навчання роботі з Telegram API за допомогою бібліотеки aiogram.

## Запуск локально

1. **Встановіть Python 3.10+**.

2. **Створіть віртуальне середовище**:

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
Встановіть залежності:

bash
Копіювати код
pip install -r requirements.txt
Додайте токен бота:

bash
Копіювати код
# Linux/macOS
export TOKEN="тут_твій_токен"
# Windows
set TOKEN="тут_твій_токен"
Запустіть бота:

bash
Копіювати код
python bot.py
Запуск на Render
Підключіть репозиторій до Render як Web Service.

Build Command: pip install -r requirements.txt

Start Command: python bot.py

Додайте Environment Variable TOKEN із токеном бота.
