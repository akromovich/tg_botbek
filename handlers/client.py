from bot_create import dp,bot
from aiogram import types,Dispatcher
from db import read_db
from keyboards.client_kb import kb_markup

async def start(message:types.Message):
    await message.answer('Привет',reply_markup=kb_markup)

async def list_of_users(message:types.Message):
    await read_db(message,reply_markup=kb_markup)

def register_handler_client(dp:Dispatcher):
    dp.register_message_handler(start,commands=['start'])
    dp.register_message_handler(list_of_users,commands=['menu'])
