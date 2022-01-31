import asyncio
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from loguru import logger

from bot.config import Config, load_config
from bot.handlers import register_handlers
from bot.middlewares import register_middlewares
from bot.service.database import create_db_session


def get_config() -> Config:
    config_file = sys.argv[1]
    return load_config(config_file)


def set_logging(config: Config):
    logger.add(config.logging.log_file,
               format=config.logging.format,
               level=config.logging.level,
               rotation=config.logging.rotation,
               compression=config.logging.compression)


@logger.catch()
async def main():
    config = get_config()

    bot = Bot(config.bot.token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=RedisStorage2())

    set_logging(config)

    bot['config'] = config
    bot['db'] = await create_db_session(config)

    register_middlewares(dp)
    register_handlers(dp)

    try:
        await dp.start_polling()
    except:
        await bot.close()
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())
