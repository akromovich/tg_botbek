from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from bot_create import dp,bot
from aiogram import types,Dispatcher
from db import add_data
from bot_create import dp
from keyboards.client_kb import kb_markup

class Users(StatesGroup):
    name = State()
    age = State()


# @dp.message_handler(commands=['Загрузить'],state=None)
async def load(message:types.Message,state=FSMContext):
    await Users.first()
    await message.answer('Введите имя')
# @dp.message_handler(state=Users.name)
async def load_name(message:types.Message,state=FSMContext):
    async with state.proxy() as data:
        data['name']=message.text
    await message.answer('Введите возраст')
    await Users.next()

# @dp.message_handler(state=Users.age)
async def load_age(message:types.Message,state=FSMContext):
    async with state.proxy() as data:
        data['age']=message.text

    await add_data(state)
    await message.answer('Добавлено',reply_markup=kb_markup)
    await state.finish()

def register_handler_admin(dp:Dispatcher):
    dp.register_message_handler(load,commands=['Загрузить'],state=None)
    dp.register_message_handler(load_name,state=Users.name)
    dp.register_message_handler(load_age,state=Users.age)