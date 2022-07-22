from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# переменные для хранения токена, бота и его памяти. еще диспетчера
storage = MemoryStorage()
bot = Bot('5527733278:AAFp1Q4D6dE-OOzKgfsm-Y4afuxM8afs_zI')
dp = Dispatcher(bot, storage=storage)
texts = {
    'start': '<i>Hello world!</i> \nЯ - Дев, лучший помощник для вашего чата! \nНапиши команду /help, чтобы узнать больше',
    'help': 'https://telegra.ph/CHat-bot-Dev-Kak-polzovatsya-07-20',
    'report': [
               'Нашли баг? Есть предложения? Напиши тему репорта, например: "Невкусный компот"',
               'Такс, а теперь опиши суть'
               ]
}
langs = ['py', 'html', 'css', 'js']


def check_language(language):
    if language in langs:
        return True
    return False
