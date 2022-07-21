import os
import sqlite3


def update_status(user_id, chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """UPDATE skillbox_chat SET
                                status_id = 1
                                WHERE user_id = ? AND chat_id = ?"""
        data = (user_id, chat_id)
        cursor.execute(sqlite_insert_query, data)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
