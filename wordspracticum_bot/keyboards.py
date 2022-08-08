from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from database import translates_rnd_word
import random


"""ВЫБОР СЛОЖНОИСТИ"""
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
es_button = KeyboardButton(text='Easy')
mid_button = KeyboardButton(text='Medium')
hard_button = KeyboardButton(text='Hard')
insane_button = KeyboardButton(text='Insane')

start_keyboard.add(es_button, mid_button, hard_button, insane_button)

"""ВЫБОР РЕЖИМА ИГРЫ"""
mode_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
ten_words_button = KeyboardButton(text='3 случайных слова')
all_words_button = KeyboardButton(text='Все слова')

mode_keyboard.add(ten_words_button, all_words_button)

"""ИНЛАЙН КЛАВИАТУРА ДЛЯ ПЕРЕВОДА"""
inline_keyboard = InlineKeyboardMarkup(row_width=2)
ink_button1 = InlineKeyboardButton(text=str(random.choice(translates_rnd_word('Easy'))), callback_data='btn_1')
ink_button2 = InlineKeyboardButton(text=str(random.choice(translates_rnd_word('Easy'))), callback_data='btn_2')
ink_button3 = InlineKeyboardButton(text=str(random.choice(translates_rnd_word('Easy'))), callback_data='btn_3')
ink_button4 = InlineKeyboardButton(text=random.choice(translates_rnd_word('Easy')), callback_data='btn_4')
inline_keyboard.add(ink_button1, ink_button2, ink_button3, ink_button4)


"""КЛАВИТУРА ГОТОВНОСТИ"""
rdy_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
rdy_btn = KeyboardButton(text='Готов')
no_rdy_btn = KeyboardButton(text='Не готов')
rdy_kb.add(rdy_btn, no_rdy_btn)
