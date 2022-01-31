from typing import Optional
from aiogram import Bot
from bot.config import Config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Model:

    def get_db_session(self, bot: Optional[Bot] = None) -> sessionmaker:
        if not bot:
            bot = Bot.get_current()
        return bot.get('db')


async def create_db_session(config: Config) -> sessionmaker:
    engine = create_async_engine(
        f"postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}/{config.db.database}",
        future=True
    )
    async with engine.begin() as conn:
        # drop all data in db (debug mode)
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    return async_session
