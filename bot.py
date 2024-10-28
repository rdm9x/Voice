import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import init_db, get_users, add_user  # Импортируем необходимые функции

# Инициализация базы данных
init_db()

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")

if TOKEN is None:
    print("Ошибка: Токен не загружен. Проверьте файл .env")
    exit(1)

# Создаем приложение
app = ApplicationBuilder().token(TOKEN).build()

# Определяем команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Это тестовый бот.")

# Определяем команду /show_users
async def show_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    users = get_users()
    if not users:
        await update.message.reply_text("Нет пользователей в базе данных.")
    else:
        user_list = "\n".join([f"{user[0]}: {user[1]} ({user[2]})" for user in users])
        await update.message.reply_text(f"Пользователи:\n{user_list}")

# Определяем команду /register
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.effective_user.username or "Не указано"

    # Добавляем пользователя в базу данных
    add_user(user_id, username)

    await update.message.reply_text(f"Вы зарегистрированы как {username}.")

# Добавляем обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show_users", show_users))
app.add_handler(CommandHandler("register", register))

# Запускаем бота
app.run_polling()