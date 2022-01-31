from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from bot.config import Config


class IsAdmin(BoundFilter):

    async def check(self, *args) -> bool:
        obj = args[0]
        if isinstance(obj, types.Message) or isinstance(obj, types.CallbackQuery):
            config: Config = obj.bot.get('config')

            return obj.from_user.id in config.bot.admin_ids
