from filters import IsPrivate
from aiogram import types
from loader import dp
from filters.SQL import get_bot_password, add_new_admin


@dp.message_handler(IsPrivate(),
                    text=[get_bot_password()])
async def auth(message: types.Message):
    await message.answer('Добавляем в администраторы')
    res = add_new_admin(username=message.from_user.username, user_id=message.from_user.id)
    if res is not None:
        await message.answer(res)
