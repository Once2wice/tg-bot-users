import os
import sqlite3


def get_lost_3_favorite(chat_id):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        sqlite_select_with_param = """SELECT id, name FROM 
                                    skillbox_chat 
                                    WHERE chat_id = ?"""
        data = (chat_id,)
        cursor.execute(sqlite_select_with_param, data)
        new_chat_id, name_chat = cursor.fetchall()[0]

        sqlite_select_with_param = """SELECT number 
                                    FROM student_chat 
                                    WHERE skillbox_chat_id = ?
                                    ORDER BY data DESC
                                    LIMIT 1"""
        data = (new_chat_id,)
        cursor.execute(sqlite_select_with_param, data)
        number = cursor.fetchall()[0][0]

        sqlite_select_with_param = """SELECT * 
                                    FROM student_chat 
                                    WHERE skillbox_chat_id = ? AND number = ?
                                    ORDER BY data DESC"""
        data = (new_chat_id, number)
        cursor.execute(sqlite_select_with_param, data)
        records = cursor.fetchall()

        sqlite_connection.commit()
        cursor.close()
        return records, name_chat

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        if str(error) == 'UNIQUE constraint failed: admins.user_id':
            return 'Пользователь с таким id уже является администратором'
    finally:
        if sqlite_connection:
            sqlite_connection.close()
