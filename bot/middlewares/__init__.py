from aiogram import Dispatcher

from .logging import LoggingMiddleware


def register_middlewares(dp: Dispatcher):
    dp.setup_middleware(LoggingMiddleware())
