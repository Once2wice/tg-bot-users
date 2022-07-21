from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin_state(StatesGroup):
    del_admin = State()
    password = State()
    add_group = State()
    add_group2 = State()
    del_group = State()
    del_group2 = State()