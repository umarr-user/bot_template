from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command
from bot.filters.chat import IsGroup


async def on_help(message: types.Message):
    text = 'HELP'
    await message.answer(text, reply=True)


def register_help_handlers(dp: Dispatcher):
    dp.register_message_handler(dp.throttled(
        rate=2)(on_help), Command('help'), IsGroup())
