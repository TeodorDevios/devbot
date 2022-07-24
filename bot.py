from aiogram import executor
from config import dp
from moduls.main_chat import init_main_chat
from moduls.main_admin import init_main_admin


async def on_startup(_):
    print('Я работаю, хозяинка')


init_main_chat(dp)
init_main_admin(dp)
executor.start_polling(dp, skip_updates=True)
