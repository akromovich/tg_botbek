from aiogram import executor
from bot_create import dp
from handlers import client,admin
from db import create_db
async def onstart_up(_):
    print('Bot:online')
    create_db()


client.register_handler_client(dp)
admin.register_handler_admin(dp)


executor.start_polling(dp,skip_updates=True,on_startup=onstart_up)