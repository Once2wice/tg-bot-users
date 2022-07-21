import os
import sqlite3


def set_multiplicity_numbers(chat_id, reset=False, add=None, sett=None):
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()

        if reset:
            ultiplicity = [x for x in range(500, 10001, 500)]
        elif sett is not None:
            if len(sett) == 0:
                sett = 0
            ultiplicity = sett
        else:
            sqlite_insert_query = """SELECT multiplicity_numbers
                                    FROM skillbox_chat
                                    WHERE chat_id = ?"""
            data = (chat_id, )
            cursor.execute(sqlite_insert_query, data)
            ultiplicity = cursor.fetchall()
            sqlite_connection.commit()
            if ultiplicity[0][0] is None:
                ultiplicity = '0'
            else:
                ultiplicity = ultiplicity[0][0].split(',')

        if add is not None:
            ultiplicity.extend(add)

        ultiplicity = ','.join(map(str, ultiplicity))

        sqlite_insert_query = """UPDATE skillbox_chat SET
                                multiplicity_numbers = ?
                                WHERE chat_id = ?"""
        data = (ultiplicity, chat_id)
        cursor.execute(sqlite_insert_query, data)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
