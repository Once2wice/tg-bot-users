import os
import sqlite3


def get_list_moder_group(key):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """SELECT *
                                FROM skillbox_chat
                                WHERE multiplicity_numbers IS NULL"""
        cursor.execute(sqlite_insert_query)
        records = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()