from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filters_admin_comands import filter_callback_moder


def inline_moder_to_user(user_name, chat_id, number, user_id):
    list_buttom = [
        ('Поздравить', 'Сongratulate'),
        ('Игнорировать', 'Skip')
    ]

    res_list_buttom = []
    for x, y in list_buttom:
        line = []
        buttom = InlineKeyboardButton(text=x, callback_data=filter_callback_moder.new(answer=y,
                                                                                      user_name=user_name,
                                                                                      chat_id=chat_id,
                                                                                      number=number,
                                                                                      user_id=user_id))
        line.append(buttom)
        res_list_buttom.append(line)

    return InlineKeyboardMarkup(row_width=1, inline_keyboard=res_list_buttom)
