from aiogram.utils.callback_data import CallbackData

filter_callback = CallbackData('res', 'answer')
filter_callback_id_name = CallbackData('res', 'user_id', 'user_name')
filter_callback_moder = CallbackData('res', 'answer', 'user_name', 'chat_id', 'number', 'user_id')
