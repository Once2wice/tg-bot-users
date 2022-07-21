from aiogram.dispatcher import FSMContext
from keyboards.inline import inline_group_panel, filter_callback, inline_back, inline_list_user_group, \
    inline_list_moder_group
from aiogram import types
from filters import IsAdmin, IsPrivate
from states import Admin_state
from loader import dp
from SQL import get_list_user_group, set_moderator_chat, dell_moderator_chat, check_moder_chat, set_multiplicity_numbers


def list_groups_in_text(list_group: list) -> str:
    dict_group = {}
    dict_group_moder = {}
    for info_group in list_group:
        if info_group[-1] is not None:
            if info_group[-1] in dict_group.keys():
                dict_group[info_group[-1]].append(info_group[1])
            else:
                dict_group[info_group[-1]] = [info_group[1]]
        else:
            dict_group_moder[info_group[2]] = info_group[1]

    count_number = 1
    text = ''
    for key_dict, values_dict in dict_group.items():
        text += f"{count_number}. {dict_group_moder[key_dict]}:\n"
        for elem in values_dict:
            text += f"\t - {elem}.\n"
        del dict_group_moder[key_dict]
        count_number += 1
    if len(dict_group_moder.keys()) > 0:
        text += f'{count_number}. Иные группы:\n'
        for key_dict, values_dict in dict_group_moder.items():
            text += f"\t- {values_dict}\n"
    return text


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='GroupPanel'))
async def group_panel(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer('Панель управление группами',
                              reply_markup=inline_group_panel())


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='ListGroup'))
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    result = get_list_user_group()
    result = list_groups_in_text(result)
    await call.message.answer(result)
    await call.message.answer('В начало', reply_markup=inline_back())


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='setModerGroup'))
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Выберите группу кто будет следить',
                              reply_markup=inline_list_user_group(key='NULL'))
    await Admin_state.add_group.set()


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           state=Admin_state.add_group)
async def group_panel(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(first=call.data.split(":")[1])
    await call.message.delete()
    await call.message.answer('Выберите группу за кем будут следить',
                              reply_markup=inline_list_user_group())
    await Admin_state.add_group2.set()


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           state=Admin_state.add_group2)
async def group_panel(call: types.CallbackQuery, state: FSMContext):
    first = (await state.get_data()).get("first")
    lost = call.data.split(":")[1]
    if first == lost:
        await call.message.answer('Группа не может следить сама за собой')
    else:
        set_moderator_chat(first, lost)
    await call.message.delete()
    await call.message.answer('Группа назначена',
                              reply_markup=inline_back())


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='delModerGroup'))
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Список групп модераторов',
                              reply_markup=inline_list_moder_group())
    await Admin_state.del_group.set()


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           state=Admin_state.del_group)
async def group_panel(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    id_moder_chat = call.data.split(":")[1]
    await state.update_data(id_moder_chat=id_moder_chat)
    await call.message.answer('Список групп, которые к ней привязаны\n'
                              'Выберите группу, с которой хотите снять группу',
                              reply_markup=inline_list_user_group(id_moder_chat))
    await Admin_state.del_group2.set()


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           state=Admin_state.del_group2)
async def group_panel(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    id_user_group = call.data.split(":")[1]
    data = await state.get_data()
    id_moder_chat = data.get('id_moder_chat')
    dell_moderator_chat(id_user_group)
    result = check_moder_chat(id_moder_chat)
    if result[0][0] == 0:
        set_multiplicity_numbers(id_moder_chat, reset=True)
        await call.message.answer('Данная группа больше не имеет пользовательских групп')

    await call.message.answer('Вроде удалилось', reply_markup=inline_back())
    await state.finish()


@dp.callback_query_handler(IsAdmin(),
                           IsPrivate(),
                           filter_callback.filter(answer='setGrad'))
async def group_panel(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('НА ЧТО ТЫ НАДЕЯЛАСЬ!?', reply_markup=inline_back())
