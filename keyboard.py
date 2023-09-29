from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

random_fact_rus = KeyboardButton("Рандомный факт о кошках")
random_fact_eng = KeyboardButton("Random fact about cats")

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(random_fact_eng).add(random_fact_rus)



