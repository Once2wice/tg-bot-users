from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filters_admin_comands import filter_callback_chat_id, filter_callback
from SQL import get_list_user_group


def inline_list_user_group(moder_chat_id=None, action=None):
    list_buttom = get_list_user_group(moder_chat_id)
    list_buttom = [(x[1], x[2]) for x in list_buttom]

    res_list_buttom = []
    for x, y in list_buttom:
        line = []
        buttom = InlineKeyboardButton(text=x, callback_data=filter_callback_chat_id.new(action=action,
                                                                                        chat_id=y))
        line.append(buttom)
        res_list_buttom.append(line)
    line = []

    buttom = InlineKeyboardButton(text='Отмена', callback_data=filter_callback.new(answer='StartPanel'))
    line.append(buttom)
    res_list_buttom.append(line)

    return InlineKeyboardMarkup(row_width=1, inline_keyboard=res_list_buttom)
