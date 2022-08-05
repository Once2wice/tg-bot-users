from aiogram.dispatcher import FSMContext
from keyboards.inline.start_panel import inline_start_panel
from keyboards.inline.filters_admin_comands import filter_callback
from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'], state='*')
async def start_panel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Привет! Поздравляю {message.from_user.username}! Ты в чат-боте "Говори на миллион"👍',
                         '\nНапиши свое имя и фамилию, пожалуйста.')


# @dp.callback_query_handler(filter_callback.filter(answer='StartPanel'),
#                            state='*')
# async def start_panel(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     await state.finish()
#     await call.message.answer('Панель управление администраторами', reply_markup=inline_start_panel())
