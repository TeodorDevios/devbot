from aiogram.types import Message
from aiogram import types, Dispatcher
from config import bot, dp, texts
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Report(StatesGroup):
    report_headline = State()
    report_text = State()

class Code(StatesGroup):
    code_info = State()
    exs = ''


async def start_message(message: Message):
    await bot.send_message(message.chat.id, texts['start'], parse_mode='HTML')


async def help_message(message: Message):
    await bot.send_message(message.chat.id, f'Лечу на помощь: \n{texts["help"]}')


async def report(message: Message):
    if message.chat.type == 'private':
        await bot.send_message(message.chat.id, texts['report'][0])
        await Report.report_headline.set()
    else:
        await message.reply('Напиши в лс, там и поболтаем ;)')


async def report_headline(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['report_headline'] = message.text
    await bot.send_message(message.chat.id, texts['report'][1])
    await Report.next()


async def report_text(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['report_text'] = message.text
    await bot.send_message(message.chat.id, 'Репорт отправлен. Ожидай ответа =)')


async def generate_code(message: Message):
    await message.reply("""Выберите соответствующий язык:
    /py - Python
    /html - HTML
    /css - CSS
    /js - JavaScript""")


async def file_with_code(message: Message):
    langs = ['py', 'html', 'css', 'js']
    if message.text[1:] in langs:
        Code.exs = message.text[1:]
        await bot.send_message(message.chat.id, "Присылай код")
        await Code.code_info.set()


async def code_info(message: Message, state = FSMContext):
    mes = message.text
    file = 'lol' + '.' + Code.exs
    files = open(file, "w")
    files.write(mes)
    files = open(file, "rb")
    await bot.send_document(chat_id = message.chat.id, document = files)
    files.close()
    await state.finish()


def init_chat(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(help_message, commands=['help'])
    dp.register_message_handler(report, commands=['report'])
    dp.register_message_handler(report_headline, state=Report.report_headline)
    dp.register_message_handler(report_text, state=Report.report_text)
    dp.register_message_handler(generate_code, commands=['generate_code'])
    dp.register_message_handler(file_with_code, commands=['py', 'html', 'css', 'js'])
    dp.register_message_handler(code_info, state=Code.code_info)

