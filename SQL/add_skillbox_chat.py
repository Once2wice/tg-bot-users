import sqlite3
import os


async def check_chat(cursor, chat_id) -> bool:
    req = '''SELECT EXISTS(SELECT chat_id FROM skillbox_chat where chat_id = ?)'''
    data_tuple = (chat_id,)
    res = cursor.execute(req, data_tuple).fetchone()[0]
    if res == 0:
        print('Запись не найдена')
        return False
    print('Запись уже существует')
    return True


async def add_new_skillbox_chat(name=None, chat_id=None, multiplicity_numbers=None, chat_moderators_id=None):
    if multiplicity_numbers is None:
        multiplicity_numbers = [x for x in range(500, 10001, 500)]
        multiplicity_numbers = (',').join(map(str, multiplicity_numbers))
    try:
        path = os.path.join(os.getcwd(), 'SQL', 'my-test.db')
        sqlite_connection = sqlite3.connect(path)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        if not await check_chat(cursor, chat_id):
            sqlite_insert_query = """INSERT INTO skillbox_chat (name, chat_id, multiplicity_numbers, chat_moderators_id)
                                      VALUES
                                     (?, ?, ?, ?);"""
            data_tuple = (name, chat_id, multiplicity_numbers, chat_moderators_id)
            cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        print('Добавили новую запись')
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
