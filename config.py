from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
bot = Bot('5527733278:AAFp1Q4D6dE-OOzKgfsm-Y4afuxM8afs_zI')
dp = Dispatcher(bot, storage=storage)
texts = {
    'start': '''<i>Hello world!</i> \n
Я <b>Дев</b> — первый бот-программист в телеграмме..ну или почти
Я смогу помочь тебе:
- развлечь участников твоей группы
- записать простой код в файл
- помочь избавиться от спамеров
и многое-многое другое...как же все это во мне помещается то?
Тебе нужно всего лишь написать команду /help и добавить меня в чат =3''',
    'help': 'https://telegra.ph/CHat-bot-Dev-Komandy-07-22',
    'report': [
               'Нашли баг? Есть предложения? Напиши тему репорта, например: "Невкусный компот"',
               'Такс, а теперь опиши суть'
               ]
}
langs = ['py', 'html', 'css', 'js']


def check_language(language):
    if language in langs:
        return [language, True]
    return ['so', False]
