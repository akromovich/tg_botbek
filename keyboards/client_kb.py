from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kb_markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
k_1 = KeyboardButton('/start')
k_2 = KeyboardButton('/Загрузить')
k_3 = KeyboardButton('/menu')
kb_markup.add(k_1,k_2,k_3)
