import os
import sqlite3


def get_count_user(number, chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_select_with_param = """SELECT id FROM skillbox_chat WHERE chat_id = ?"""
        data = (chat_id,)
        cursor.execute(sqlite_select_with_param, data)
        records = cursor.fetchall()[0][0]
        sqlite_select_count_with_param = """SELECT COUNT(*) FROM student_chat WHERE skillbox_chat_id = ? AND number = 
        ? """
        data = (records, number)
        cursor.execute(sqlite_select_count_with_param, data)
        records = cursor.fetchall()[0][0]
        sqlite_connection.commit()
        cursor.close()
        print(records)
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        if str(error) == 'UNIQUE constraint failed: admins.user_id':
            return 'Пользователь с таким id уже является администратором'
    finally:
        if sqlite_connection:
            sqlite_connection.close()
