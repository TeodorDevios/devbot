from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# переменные для хранения токена, бота и его памяти. еще диспетчера
storage = MemoryStorage()
bot = Bot('5527733278:AAFp1Q4D6dE-OOzKgfsm-Y4afuxM8afs_zI')
dp = Dispatcher(bot, storage=storage)
admins = [1330646571, 904249798]
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
               ],
    'main_admin': [
        'ля, кто явился, его величество '
    ]
}
langs = ['py', 'html', 'css', 'js']


def check_language(language: str):
    if language in langs:
        return [language, True]
    return ['so', False]


def create_key(list_reports: list, report: tuple, key: InlineKeyboardMarkup):
    len_reports = len(list_reports)
    go_up = InlineKeyboardButton('>>>', callback_data='go_up')
    go_out = InlineKeyboardButton('<<<', callback_data="go_out")
    report_answer = InlineKeyboardButton('Ответить на репорт', callback_data="report_answer")
    if len_reports == 1:
        key.add(report_answer)
    elif list_reports.index(report) == len_reports - 1:
        key.add(go_out, report_answer)
    elif list_reports.index(report) == 0 and len_reports != 1:
        key.add(go_up, report_answer)
    else:
        key.add(go_out, go_up, report_answer)
    return key
