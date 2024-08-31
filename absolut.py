import nest_asyncio
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler
from data_manager import load_data, get_user_score, update_user_score

# Примените nest_asyncio
nest_asyncio.apply()

DATA_FILE = 'Data/data.json'

# Загрузка данных из файла
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {"users": {}}

# Сохранение данных в файл
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Получение очков пользователя
def get_user_score(user_id, data):
    return data["users"].get(str(user_id), {"score": 0})["score"]

# Обновление очков пользователя
def update_user_score(user_id, score, data):
    if str(user_id) not in data["users"]:
        data["users"][str(user_id)] = {"score": 0}
    data["users"][str(user_id)]["score"] += score
    save_data(data)

# Функция для команды /start
async def start(update: Update, context):
    user_id = update.message.from_user.id
    data = load_data()
    user_score = get_user_score(user_id, data)
    keyboard = [
        [InlineKeyboardButton("Играть", web_app=WebAppInfo(url="https://absolutelynothingapp.github.io/AbsolutelyNothingApp/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Absolutely Nothing. You can press "Play",if you want but for what?.', reply_markup=reply_markup)

# Основная функция для запуска бота
async def main():
    application = Application.builder().token("6926943403:AAEXHHWGc-u_TcyjGN6OKX_UOkhqp9W-lRM").build()

    # Команда /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
