from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from bot.filters.admin import IsAdmin
from bot.filters.chat import IsPrivate


async def on_start(message: types.Message):
    text = 'Hi, admin'
    await message.answer(text)


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        on_start, Command('start'), IsPrivate(), IsAdmin())
