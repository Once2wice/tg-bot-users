from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from SQL import get_bot_admins


class IsAdmin(BoundFilter):

    async def check(self, message: types.Message):
        res = str(message.from_user.id) in get_bot_admins()
        # print(res)
        return res


class IsPrivate(BoundFilter):

    async def check(self, message):
        if isinstance(message, types.Message):
            return message.chat.type == types.ChatType.PRIVATE
        elif isinstance(message, types.CallbackQuery):
            return message.message.chat.type == types.ChatType.PRIVATE