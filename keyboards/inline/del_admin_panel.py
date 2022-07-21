from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filters_admin_comands import filter_callback_id_name
from SQL import get_bot_admins


def inline_dell_admin_panel():
    name, user_id = get_bot_admins(full=True)[0]
    list_buttom = [(name, user_id, name),
                   ('Отмена', 'StartPanel', '-')]

    res_list_buttom = []
    for x, y, z in list_buttom:
        line = []
        buttom = InlineKeyboardButton(text=x, callback_data=filter_callback_id_name.new(user_id=y, user_name=z))
        line.append(buttom)
        res_list_buttom.append(line)
    return InlineKeyboardMarkup(row_width=1, inline_keyboard=res_list_buttom)
