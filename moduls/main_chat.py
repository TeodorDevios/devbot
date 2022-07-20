from aiogram.types import Message
from aiogram import types, Dispatcher
from config import bot, dp, texts
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


async def start_message(message: Message):
    await bot.send_message(message.chat.id, texts['start'], parse_mode='HTML')


async def help_message(message: Message):
    await bot.send_message(message.chat.id, f'Лечу на помощь: \n{texts["help"]}')


async def report(message: Message):
    await bot.send_message(message.chat.id, texts['report'][0])


def init_chat(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_message_handler(help_message, commands=['help'])
    dp.register_message_handler(report, commands=['report'])

