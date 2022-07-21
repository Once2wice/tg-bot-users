import os
import sqlite3


def get_moder(chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """SELECT chat_moderators_id
                                FROM skillbox_chat
                                WHERE chat_id=?"""
        data = (chat_id,)
        cursor.execute(sqlite_insert_query, data)
        records = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return records[0][0]

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
