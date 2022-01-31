from unittest import skip
from aiogram import types
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from loguru import logger


class LoggingMiddleware(LifetimeControllerMiddleware):

    async def pre_process(self, obj, data, *args):
        logger.debug(
            f'{obj} | {data} | {args}'
        )
