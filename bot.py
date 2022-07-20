from aiogram import executor
from config import dp
from moduls.main_chat import init_chat


async def on_startup(_):
    print('Я работаю, хозяинка')


init_chat(dp)
executor.start_polling(dp, skip_updates=True)
