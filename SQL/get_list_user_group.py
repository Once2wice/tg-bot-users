import os
import sqlite3


def get_list_user_group(key=None):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        if key is None:
            sqlite_insert_query = """SELECT *
                                    FROM skillbox_chat"""
            cursor.execute(sqlite_insert_query)
        else:
            if key == 'NULL':
                sqlite_insert_query = """SELECT *
                                        FROM skillbox_chat
                                        WHERE chat_moderators_id IS NULL"""
                cursor.execute(sqlite_insert_query)
            else:
                sqlite_insert_query = """SELECT *
                                        FROM skillbox_chat
                                        WHERE chat_moderators_id = ?"""
                data = (str(key),)
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
