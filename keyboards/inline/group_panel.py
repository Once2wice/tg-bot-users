from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.filters_admin_comands import filter_callback


def inline_group_panel():
    list_buttom = [
        ('Список Групп', 'ListGroup'),
        # ('Список moder_group', 'ModerGroup'),
        ('Дать права группе', 'setModerGroup'),
        ('Снять права с группы', 'delModerGroup'),
        # ('Настроить призовые места', 'setGrad'),
        ('В начало', 'StartPanel')
    ]

    res_list_buttom = []
    for x, y in list_buttom:
        line = []
        buttom = InlineKeyboardButton(text=x, callback_data=filter_callback.new(answer=y))
        line.append(buttom)
        res_list_buttom.append(line)

    return InlineKeyboardMarkup(row_width=1, inline_keyboard=res_list_buttom)
