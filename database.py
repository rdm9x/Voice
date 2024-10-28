import sqlite3

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect('users.db')  # Создает базу данных users.db
    cursor = conn.cursor()

    # Создание таблицы пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие соединения

# Функция для добавления пользователя
def add_user(username, phone):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, phone) VALUES (?, ?)', (username, phone))
    conn.commit()
    conn.close()

# Функция для получения всех пользователей
def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users