from aiogram import Dispatcher

from .help import register_help_handlers


def register_chat_handlers(dp: Dispatcher):
    register_help_handlers(dp)
