import  sqlite3 as sq
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup



ad_markup = ReplyKeyboardMarkup(row_width=4,resize_keyboard=True)

def create_db():
    global cur,base
    base = sq.connect('users.db')
    cur = base.cursor()
    if base:
        print('DB:connect')

    base.execute('CREATE TABLE IF NOT EXISTS users(name TEXT,age INTEGER)')
    base.commit()

async def add_data(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES(?,?)',tuple(data.values()))
        print('DB:data-updates')
    base.commit()

async def read_db(message,reply_markup):
    # await message.answer('СПИСОК ПОЛЬЗОВАТЕЛЕЙ')
    for item in cur.execute('SELECT * FROM users').fetchall():
        k_1 = KeyboardButton(f'{item[0]}') 
        ad_markup.add(k_1)
        await message.answer(f'имя: {item[0]}\nвозраст: {item[1]}',reply_markup=ad_markup)
    await message.answer('для удаления пользователей нажмите кнопку с именем пользователя')
    if message.text in  cur.execute('SELECT * FROM users').fetchall():
        cur.execute('DELETE FROM users WHERE name==?',(message.text))
        await message.answer('удалено')
    else:
        await message.answer('ошибка')
# async def delete_user(message):
#     cur.execute(f'DELETE FROM users WHERE name==?',message.text)
#     await message.answer(f'{message.text} удалено')

# async def but():
#     for item in cur.execute('SELECT * FROM users').fetchall():
#         k_1 = KeyboardButton(f'{item[1]}') 
#         ad_markup.add(k_1)