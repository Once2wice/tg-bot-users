import os
import sqlite3


def set_moderator_chat(moder_id, user_chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = """UPDATE skillbox_chat SET
                                chat_moderators_id = ?
                                WHERE chat_id = ?"""
        deta = (moder_id, user_chat_id)
        cursor.execute(sqlite_insert_query, deta)

        sqlite_insert_query = """UPDATE skillbox_chat SET
                                        multiplicity_numbers = NULL
                                        WHERE chat_id = ?"""
        deta = (moder_id, )
        cursor.execute(sqlite_insert_query, deta)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
