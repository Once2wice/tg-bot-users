import os
import sqlite3
import datetime


def add_user(user_name, user_id, number, chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_with_param = """INSERT INTO student_chat
                                      (user_name, user_id, number, data, status_id, skillbox_chat_id)
                                      VALUES (?, ?, ?, ?, 2, ?);"""

        data = (user_name, user_id, number, datetime.datetime.now(), chat_id)
        cursor.execute(sqlite_insert_with_param, data)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        if str(error) == 'UNIQUE constraint failed: admins.user_id':
            return 'Пользователь с таким id уже является администратором'
    finally:
        if sqlite_connection:
            sqlite_connection.close()