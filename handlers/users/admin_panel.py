from aiogram.dispatcher import FSMContext
from keyboards.inline import inline_admin_panel
from keyboards.inline import filter_callback
from keyboards.inline import inline_dell_admin_panel
from keyboards.inline import inline_back
from filters import IsAdmin, IsPrivate
from aiogram import types
from loader import dp
from states import Admin_state
from filters.SQL import get_bot_admins, del_admin


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='AdminPanel'),
                           state='*')
async def admin_panel(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    await call.message.answer('Панель управление администраторами', reply_markup=inline_admin_panel())


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='ListAdmin'))
async def admin_panel(call: types.CallbackQuery):
    await call.answer()
    result = get_bot_admins(full=True)
    new_string = 'Список администраторов:\n'
    for count_users, element in enumerate(result):
        new_string += f"{count_users + 1}) {element[0]}  ID ({element[1]})\n"
    await call.message.delete()
    await call.message.answer(new_string)
    await call.message.answer('Назад', reply_markup=inline_back())


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='DelAdmin'))
async def admin_panel(call: types.CallbackQuery):
    await Admin_state.del_admin.set()
    await call.message.delete()
    await call.message.answer('Кого вы хотите удалить?', reply_markup=inline_dell_admin_panel())


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           state=Admin_state.del_admin)
async def admin_panel(call: types.CallbackQuery,state: FSMContext):
    await state.finish()
    await call.message.delete()
    data = call.data.split(":")[1:]
    name = data[1]
    user_id = data[0]
    del_admin(user_id)
    await call.message.answer(f'Админ {name} удален', reply_markup=inline_back())
