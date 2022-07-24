from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
import database
from config import texts, admins, bot, dp, create_key


class Report(StatesGroup):
    report_user_id: int
    report_index: int
    report: tuple
    report_list: list
    report_message = State()


async def reports(message: Message):
    if message.chat.type == 'private' and message.chat.id in admins:
        await message.reply(texts['main_admin'][0] + message.chat.first_name)
        try:
            reports_all = database.get_reports()
            report = reports_all[random.randint(0, len(reports_all) - 1)]
            key = InlineKeyboardMarkup(row_width=2)
            create_key(reports_all, report, key)
            mess = await bot.send_message(message.chat.id, f'<b>{report[1]}</b>\n<i>{report[2]}</i>', parse_mode='HTMl', reply_markup=key)
            Report.report_index = reports_all.index(report)
            Report.report_user_id = report[0]
            Report.report_list = reports_all
            Report.report = report
        except Exception as ex:
            print(ex)
            await bot.send_message(message.chat.id, 'Нету репортов')


@dp.callback_query_handler(text="report_answer")
async def send_report(call: CallbackQuery, state: FSMContext):
    await call.answer('Напиши сообщение пользователю')
    await Report.report_message.set()


@dp.callback_query_handler(text='go_up')
async def go_up(call: CallbackQuery):
    key = InlineKeyboardMarkup(row_width=2)
    all_list = Report.report_list
    report = all_list[Report.report_index + 1]
    Report.report_index = all_list.index(report)
    Report.report_user_id = report[0]
    create_key(all_list, report, key)
    await call.message.edit_text(f'<b>{report[1]}</b>\n<i>{report[2]}</i>', parse_mode='HTMl', reply_markup=key)


@dp.callback_query_handler(text='go_out')
async def go_up(call: CallbackQuery):
    key = InlineKeyboardMarkup(row_width=2)
    all_list = Report.report_list
    report = all_list[Report.report_index - 1]
    Report.report_index = all_list.index(report)
    create_key(all_list, report, key)
    Report.report_user_id = report[0]
    await call.message.edit_text(f'<b>{report[1]}</b>\n<i>{report[2]}</i>', parse_mode='HTMl', reply_markup=key)


async def report_ans_send(message: Message, state: FSMContext):
    await bot.send_message(message.chat.id, 'Усе сделано, солнце')
    await bot.send_message(Report.report_user_id, '<b>Ответ Администратора: </b>' + message.text, parse_mode='HTML')
    database.delete_report(Report.report_user_id)
    await state.finish()


def init_main_admin(dp: Dispatcher):
    dp.register_message_handler(reports, commands=['reports'])
    dp.register_message_handler(report_ans_send, state=Report.report_message)
