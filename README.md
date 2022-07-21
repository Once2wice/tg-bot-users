# tg-bot-users 🤖
 Телеграм-бот, который отслеживет количество вступивших пользователей в группу и определяет юбилейных пользователей. При вступлении в группу юбилейного участника,
бот присылает в группу модераторов уведомление, содержащее название группы, имя, ник, id пользователя и дату и время вступления. Также уведомление содержит две кнопки: "Поздравить" - для автоматической отправки поздравления в группу и "Отклонить". Кроме юбилейных пользователей, бот сохраняет двух последующих участников, т.к. юбилейным участником может оказаться модератор или бот.

# Особенности
- Бот автоматически отслеживает юбилейного пользователя. Если участник группы является юбилейным, то информация сохраняется в базу данных;
- Исключены повторные поздравления одного и того же пользователя, находящегося в одной группе;
- Управление настройками бота осуществляется пользователями, обладающих правами администратора;
- Информация о поздравлении/отклонении отправляется в групповой чат модераторов;
- Простая подготовка запуска бота;
- Для управления ботом используются кнопки вместо команд;
- Если бот добавлен в чат не администратором, то бот выходит из чата.

# Requirements
- Python 3.8
- aiogram 2.7
- aiohttp 3.6.2
- aioredis 1.3.1
- python-dotenv

# Запуск телеграм-бота
Запустить файл app.py.

# Для администраторов
Для активации прав администратора необходимо ввести начальный пароль (12345) из базы данных bot_info, который администратор может изменить.
Функция администратора разделяетя на:
1. Управление гпуппами:
    + Вывод списка групп модераторов и их дочерних групп (которые они модерируют);
    + Привязка/отвязка группы модераторов к студенческой группе;
3. Управление администраторами (изменение настроек бота):
    + Изменить пароль;
    + Удалить администратора;
    + Вывести список администраторов.

# Для разработчиков
Структура:
- SQL:
  + sqlite_sequence - автоматически созданная таблица, которая является счетчиком первичного ключа всех таблиц в текущей базе данных;
  + skillbox_chat - таблица, в которой хранятся id и названия групп, в которых бот является администратором;
    + id (INTEGER) - первичный ключ;
    + name (TEXT) - название групп;
    + chat_id (TEXT) - id группы;
    + multiplicity_numbers (BLOB) - строка, содержащая порядковые номера юбилейного пользователя для поздравления;
    + chat_moderators_id (BLOB) - id группы модераторов;
  + admins - таблица, в которой хранятся данные о пользователях, обладающих правами для настройки телеграм-бота;
    + id (INTEGER) - первичный ключ;
    + username (INTEGER) - ник пользователя, обладающего правами администратора;
    + user_id (INTEGER) - id пользователя, обладающего правами администратора;
  + moderators - таблица, в которой хранятся данные о пользователях, являющихся модераторами;
    + id (INTEGER) - первичный ключ;
    + username (TEXT) - ник пользователя, являющегося модератором групп(-ы);
    + user_id (TEXT) id пользователя, обладающего правами администратора;
    + chat_id (INTEGER) - внешний ключ, который соединяет таблицу модератора с таблицей skillbox_chat, определяя, какой чат модерирует пользователь;
  + student_chat - таблица, которая содержит информацию о юбилейном и двух следующих за ним пользователях;
    + id (INTEGER) - первичный ключ;
    + user_name (TEXT) - ник пользователя;
    + user_id (TEXT) - id пользователя;
    + number (INTEGER) - порядковый номер;
    + data (DATABASE) - дата и время вступления в группу;
    + status_id (INTEGER) - внешний ключ, который обозначает статус пользователя на текущий момент времени (поздравлен или нет);
    + skillbox_chat_id (INTEGER) - id таблицы с данными о группах, в которых бот является администратором;
   + status - таблица, содержащая информацию о статусе пользователя (поздравлен или нет);
     + id (INTEGER) - первичный ключ;
     + name_status (TEXT) - статус (поздравлен или нет);
   + bot_info - таблица, содержащая информацию о боте;
     + id (INTEGER) - первичный ключ;
     + token (TEXT) - токен бота;
     + password (TEXT) - пароль, который необходимо внести для приобретения прав администратора;
 + data - данные для запуска бота;
 + filters - условие для попадания в handlers;
 + handlers - хендлеры для обработки команд;
 + keyboards - функции для создания управляющих кнопок;
 + middlewares - предобработка запроса;
 + states - машинное состояние;
 + utils - поступление администраторам информации о запуске бота и инициация кнопок и команд;
 + app.py - запуск файла, в котором импортируются все фильтры, handlers и middlewares;
 + loader.py - запуск бота.
# Команды бота
/start - запуск бота
