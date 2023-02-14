import  sqlite3 as sq


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
    await message.answer('СПИСОК ПОЛЬЗОВАТЕЛЕЙ')
    for item in cur.execute('SELECT * FROM users').fetchall():
        await message.answer(f'имя: {item[0]}\nвозраст: {item[1]}')
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/akromovich/tg_botbek.git
git push -u origin main