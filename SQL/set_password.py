import os
import sqlite3


def set_bot_password(password):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """Update bot_info set password = ? where id = 1"""
        data = (password,)
        cursor.execute(sqlite_insert_query, data)
        sqlite_connection.commit()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()