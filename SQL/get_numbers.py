import os
import sqlite3


def get_numbers(chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """SELECT multiplicity_numbers
                                FROM skillbox_chat
                                WHERE chat_id=?"""
        data = (chat_id,)
        cursor.execute(sqlite_insert_query, data)
        records = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
