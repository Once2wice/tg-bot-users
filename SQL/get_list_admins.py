import os
import sqlite3


def get_bot_admins(full=False):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        if full:
            sqlite_insert_query = """SELECT username, user_id FROM admins;"""
            cursor.execute(sqlite_insert_query)
            records = cursor.fetchall()
            sqlite_connection.commit()
        else:
            sqlite_insert_query = """SELECT user_id FROM admins;"""
            cursor.execute(sqlite_insert_query)
            records = cursor.fetchall()
            sqlite_connection.commit()
            records = sum(map(list, records), [])
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
