from filters import IsAdmin, IsPrivate
from keyboards.inline import inline_password
from keyboards.inline import filter_callback
from keyboards.inline import inline_back
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp, bot
from states import Admin_state
from SQL import set_bot_password


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='Password'), state='*')
async def password(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Введите новый пароль', reply_markup=inline_password())
    await Admin_state.password.set()


@dp.message_handler(IsAdmin(),
                    IsPrivate(),
                    state=Admin_state.password)
async def password(mes: types.Message, state: FSMContext):
    print('Новый пароль', mes.text)
    set_bot_password(mes.text)
    await state.finish()
    await bot.delete_message(mes.from_user.id, mes.message_id - 1)
    await mes.answer('Пароль изменен', reply_markup=inline_back())
