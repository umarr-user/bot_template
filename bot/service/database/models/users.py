from typing import Optional

from aiogram import Bot
from bot.service.database import Base, Model
from sqlalchemy import (Boolean, Column, Date, Integer, String, insert, select,
                        update)


class User(Base, Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    reg_date = Column(Date)

    @classmethod
    async def new(cls, user_id: int, bot: Optional[Bot] = None):
        db_session = cls.get_db_session(bot)
        async with db_session() as session:
            sql = insert(cls).values(user_id=user_id)
            await session.execute(sql)
            await session.commit()

    @classmethod
    async def get(cls, user_id: int, bot: Optional[Bot] = None) -> 'User':
        db_session = cls.get_db_session(bot)
        async with db_session() as session:
            sql = select(cls).where(cls.user_id == user_id)
            response = await session.execute(sql)
            user: cls = response.scalar()
        return user
