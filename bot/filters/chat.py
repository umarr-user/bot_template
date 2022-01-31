from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroup(BoundFilter):

    async def check(self, *args) -> bool:
        obj = args[0]
        if isinstance(obj, types.Message) or isinstance(obj, types.CallbackQuery):
            return obj.chat.type in [types.ChatType.GROUP, types.ChatType.SUPERGROUP]


class IsPrivate(BoundFilter):
    async def check(self, *args) -> bool:
        obj = args[0]
        if isinstance(obj, types.Message) or isinstance(obj, types.CallbackQuery):
            return obj.chat.type in [types.ChatType.PRIVATE]
