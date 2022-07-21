from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filters_admin_comands import filter_callback


def inline_password():
    list_buttom = [
        ('Отмена', 'StartPanel')
    ]

    res_list_buttom = []
    for x, y in list_buttom:
        line = []
        buttom = InlineKeyboardButton(text=x, callback_data=filter_callback.new(answer=y))
        line.append(buttom)
        res_list_buttom.append(line)

    return InlineKeyboardMarkup(row_width=1, inline_keyboard=res_list_buttom)
