from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# переменные для хранения токена, бота и его памяти. еще диспетчера
storage = MemoryStorage()
bot = Bot('5527733278:AAFp1Q4D6dE-OOzKgfsm-Y4afuxM8afs_zI')
dp = Dispatcher(bot, storage=storage)
