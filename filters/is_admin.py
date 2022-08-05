from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from filters.SQL import get_bot_admins, get_list_moder_group


class IsAdmin(BoundFilter):

    async def check(self, message: types.Message)-> bool:
        res = str(message.from_user.id) in get_bot_admins()
        return res


class IsPrivate(BoundFilter):

    async def check(self, message) -> bool:
        if isinstance(message, types.Message):
            return message.chat.type == types.ChatType.PRIVATE
        elif isinstance(message, types.CallbackQuery):
            return message.message.chat.type == types.ChatType.PRIVATE


class IsModers(BoundFilter):
    async def check(self, message) -> bool:
        groups_moder_list = get_list_moder_group()
        moder_id = [data[2] for data in groups_moder_list]
        if isinstance(message, types.Message):
            chat_id = message.chat.id
        else:
            chat_id = message.message.chat.id
        if str(chat_id) in moder_id:
            return True
        return False
