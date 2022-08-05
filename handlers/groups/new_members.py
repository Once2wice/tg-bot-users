from loader import dp, bot
from aiogram import types
from aiogram.types import ContentType, Message
from filters.SQL import add_new_skillbox_chat, get_numbers, set_multiplicity_numbers, add_user, get_moder, check_student, \
    get_count_user, get_bot_admins, update_status, get_lost_3_favorite, get_str_status
from keyboards.inline import inline_moder_to_user, inline_list_user_group, filter_callback
from keyboards.inline import filter_callback_moder, filter_callback_chat_id
from filters import IsModers
import datetime


@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS],
                    state='*')
async def new_members_handler(message: Message):
    bot_id = (await bot.get_me()).id
    new_member = message.new_chat_members[0]
    if new_member.id == bot_id:
        if str(message.from_user.id) in get_bot_admins():
            await add_new_skillbox_chat(chat_id=message.chat.id, name=message.chat.title)
        else:
            await message.answer('Меня добавил не админ, всем пока')
            await bot.leave_chat(message.chat.id)
    else:
        if not new_member.is_bot:
            await message.answer(f"Добро пожаловать, {new_member.mention}")
            result = await check_user(message.chat.id, new_member.id)
            if result is not None:
                add_user(user_name=new_member.mention,
                         user_id=new_member.id,
                         number=result,
                         chat_id=message.chat.id)
                moder_id = get_moder(message.chat.id)
                text = f'🎉 {message.chat.title}\n' \
                       f'👤{new_member.mention}\n' \
                       f'({new_member.first_name} {new_member.last_name})\n' \
                       f'🔢 {result}\n' \
                       f'🕐{datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}'
                await bot.send_message(moder_id, text, reply_markup=inline_moder_to_user(user_name=new_member.mention,
                                                                                         chat_id=message.chat.id,
                                                                                         number=result,
                                                                                         user_id=new_member.id))


async def get_number(chat_id):
    numbers = get_numbers(chat_id)
    if numbers is None:
        return None
    list_numbers = numbers.split(',')
    return sorted(list(map(int, list_numbers)))


async def check_user(chat_id, user_id):
    count = await bot.get_chat_members_count(chat_id)
    number = await get_number(chat_id)
    if number is None:
        return
    min_number = min(number)
    print(count, min_number)
    count_user = get_count_user(chat_id=chat_id, number=min_number)
    if count >= min_number:
        moder_chat_id = get_moder(chat_id=chat_id)
        status = (await bot.get_chat_member(chat_id=moder_chat_id, user_id=user_id)).status
        if status != 'member' and str(user_id) not in get_bot_admins():
            print(check_student(user_id=user_id, chat_id=chat_id))
            if not check_student(user_id=user_id, chat_id=chat_id):
                if count_user == 2:
                    set_multiplicity_numbers(chat_id, sett=number[1:])
                    print('удалить минималку')
                print('выйгрышное место')
                return min_number
            else:
                print('Такой пользователь уже занял место')
        else:
            print('Модератор')
    else:
        print('Посредственность')
    return None


@dp.callback_query_handler(filter_callback_moder.filter(answer='Сongratulate'))
async def admin_panel(call: types.CallbackQuery, callback_data: dict):
    text = call.message.text + f'\n{call.from_user.mention} Поздравил'
    await call.message.answer(text=text, reply_markup=None)
    name = callback_data.get('user_name')
    chat_id = callback_data.get('chat_id')
    user_id = callback_data.get('user_id')
    number = callback_data.get('number')
    await bot.send_message(chat_id=chat_id, text=f'🎉 Поздравляю, {name}!\n'
                                                 f'Как же удачно вы попали в нужное место и в нужное время!\n'
                                                 f'Вы {number} участник коммьюнити.\n'
                                                 f'Вас ждут плюшки и печенюшки!🎉')
    await call.message.delete()
    update_status(user_id=user_id, chat_id=chat_id)


@dp.callback_query_handler(filter_callback_moder.filter(answer='Skip'))
async def admin_panel(call: types.CallbackQuery):
    text = call.message.text + f'\n{call.from_user.mention} скипнул'
    await call.message.answer(text=text, reply_markup=None)
    await call.message.delete()


@dp.message_handler(IsModers(), commands=['groups'])
async def groups_moders(message: types.Message):
    await message.answer('Группы модера',
                         reply_markup=inline_list_user_group(moder_chat_id=message.chat.id,
                                                             action='ListUserFromModer'))


@dp.callback_query_handler(filter_callback_chat_id.filter(action='ListUserFromModer'))
async def list_people(call: types.CallbackQuery, callback_data: dict):
    await call.answer()
    chat_id = callback_data.get('chat_id')
    records, name_chat = get_lost_3_favorite(chat_id)
    print(records, name_chat)
    for record in records:
        user_name = record[1]
        user_id = record[2]
        number = record[3]
        date = record[4]
        status = get_str_status(record[5])
        text = f'🎉 {name_chat}\n' \
               f'({user_name})\n' \
               f'🔢 {number}\n' \
               f'🕐{date}\n'\
               f'Прошлый статус: {status}'
        await call.message.answer(text, reply_markup=inline_moder_to_user(user_name=user_name,
                                                                          chat_id=chat_id,
                                                                          number=number,
                                                                          user_id=user_id))


@dp.callback_query_handler(filter_callback.filter(answer='StartPanel'))
async def start_panel(call: types.CallbackQuery):
    await call.message.delete()
