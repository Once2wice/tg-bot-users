import os
import sqlite3


def update_status(user_id, chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_select_with_param = """SELECT id FROM skillbox_chat WHERE chat_id = ?"""
        data = (chat_id,)
        cursor.execute(sqlite_select_with_param, data)
        records = cursor.fetchall()[0][0]
        print(records)
        print(type(records))
        print(user_id, chat_id)
        sqlite_insert_query = """UPDATE student_chat SET
                                status_id = 1
                                WHERE user_id = ? AND skillbox_chat_id = ?"""
        data = (user_id, records)
        cursor.execute(sqlite_insert_query, data)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
