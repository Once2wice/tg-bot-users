from aiogram import Dispatcher

from .is_admin import IsAdmin, IsPrivate

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsPrivate)
    pass
