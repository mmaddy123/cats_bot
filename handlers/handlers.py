import random
from aiogram import types
from aiogram.dispatcher.filters import Text
from bot import dp, bot
from cat_api import get_fact, get_fact_ru
from qazaq_transliterator import translit
import keyboard as kb


@dp.message_handler(commands=['start'])
async def cmd_start_handler(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=f"https://cataas.com/cat/says/Hello {translit(message.from_user.first_name)}?rnum={random.randint(0, 1000000)}",
                         reply_markup=kb.main_keyboard)


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer("/start - команда для запуска бота\n"
                         "Используйте кнопки для получения факта о кошках")


@dp.message_handler(Text(equals="Рандомный факт о кошках"))
async def get_fact_rus(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=f"https://cataas.com/cat?rnum={random.randint(0, 1000000)}",
                         caption=f"Факт: {get_fact_ru()}")


@dp.message_handler(Text(equals="Random fact about cats"))
async def get_fact_eng(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=f"https://cataas.com/cat?rnum={random.randint(0, 1000000)}",
                         caption=f"Fact: {get_fact()}")


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)

# @dp.message_handler(commands=['get_random_cat'])
# async def get_random_cat_handler(message: types.Message):
#     await bot.send_photo(chat_id=message.chat.id,
#                          photo=f"https://cataas.com/cat?rnum={random.randint(0, 1000000)}",
#                          caption=f"Fact: {get_fact()}")
