from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from bot.filters.chat import IsPrivate


async def on_start(message: types.Message):
    text = 'Hi, user'
    await message.answer(text)


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(on_start, Command('start'), IsPrivate())
