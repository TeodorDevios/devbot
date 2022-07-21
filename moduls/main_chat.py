from aiogram.types import Message
from aiogram import types, Dispatcher
from config import bot, dp, texts
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Report(StatesGroup):
    report_headline = State()
    report_text = State()


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


def init_chat(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(help_message, commands=['help'])
    dp.register_message_handler(report, commands=['report'])
    dp.register_message_handler(report_headline, state=Report.report_headline)
    dp.register_message_handler(report_text, state=Report.report_text)

