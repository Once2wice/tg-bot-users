import os
import sqlite3


def add_new_admin(username, user_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_insert_with_param = """INSERT INTO admins
                                      (username, user_id)
                                      VALUES (?, ?);"""

        data_tuple = (username, user_id)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        if str(error) == 'UNIQUE constraint failed: admins.user_id':
            return 'Пользователь с таким id уже является администратором'
    finally:
        if sqlite_connection:
            sqlite_connection.close()