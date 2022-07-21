from filters import IsAdmin
from keyboards.inline.moder_panel import inline_moder_panel
from keyboards.inline.filters_admin_comands import yes_no_callback
from aiogram import types
from loader import dp


@dp.callback_query_handler(IsAdmin(), yes_no_callback.filter(answer='ModerPanel'), state='*')
async def moder_panel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Панель управление модераторами', reply_markup=inline_moder_panel)
