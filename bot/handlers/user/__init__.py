from aiogram import Dispatcher

from .start import register_start_handlers


def register_user_handlers(dp: Dispatcher):
    register_start_handlers(dp)
