from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b_elements = KeyboardButton('elements')
b_close = KeyboardButton('close')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(b_elements).add(b_close)
