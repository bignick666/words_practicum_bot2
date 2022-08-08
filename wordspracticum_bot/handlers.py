from aiogram import Dispatcher, types
from aiogram.types import CallbackQuery

from loader import bot
from keyboards import *
from database import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import random

USER_DATA = {}
WORD = ''

class FSMChoose(StatesGroup):
    level = State()
    mode = State()


async def start_handler(message: types.Message):
    await FSMChoose.level.set()
    await message.answer(f'Добрый день, {message.from_user.full_name}.\nХотите подтянуть свой английский?\n'
                         f'Данный бот отлично вам в этом поможет\n'
                         f'Мы подготовили для вас огромную, ежедневно обновляемую базу слов разных уровней сложности\n'
                         f'Выбери уровень сложности\n'
                         f'Удачи!', reply_markup=start_keyboard)


async def level_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['level'] = message.text
    await FSMChoose.next()
    await message.answer('Выбери режим тренивроки:', reply_markup=mode_keyboard)


async def mode_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mode'] = message.text
        await message.answer(f'Вы выбрали:\n'
                         f'Уровень сложности: {data["level"]}\n'
                         f'Режим тренировки: {data["mode"]}')
        USER_DATA['level'] = data['level']
        USER_DATA['mode'] = data['mode']
        # await message.answer(USER_DATA)
    await state.finish()
    word = random.choice(select_easy_level(data['level']))[1]
    await message.answer(f"Как переводиться слово: {word}",
                         reply_markup=inline_keyboard)
    WORD = word
    # print(type(random.choice(select_easy_level(data['level']))[1]))


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn_'))


# @dp.callback_query_handler(text=random_translates()[2])
# async def word_call(callback: types.CallbackQuery):
#     if USER_DATA["mode"] == all_words_button.text:
#         await callback.message.answer(f"Как переводиться слово: {random.choice(select_easy_level(USER_DATA['level']))[1]}?"
#                                       ,reply_markup=inline_keyboard)





# async def easy_level(message: types.Message):
#     for word in select_easy_level(message.text):
#         await message.answer(word)
# if data["mode"] == ten_words_button.text:
#     await message.answer(f"Как переводиться слово: {random.choice(select_easy_level(data['level']))[1]}?")
# elif data['mode'] == all_words_button.text:
#     for word in select_easy_level(data['level']):
#         await message.answer(f'Как переводиться слово: {word[1]}?')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands='start', state=None)
    dp.register_message_handler(level_handler, state=FSMChoose.level)
    dp.register_message_handler(mode_handler, state=FSMChoose.mode)
    dp.register_callback_query_handler(choose, lambda c: c.data and c.data.startswith('btn_'), state=None)
    # dp.register_callback_query_handler(word_call, state=None)
