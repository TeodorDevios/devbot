from aiogram.types import Message
from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


async def start_message(message: Message):
    await bot.send_message(message.chat.id, 'Hello world!')


def init_chat(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=['start'])
