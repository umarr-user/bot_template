from aiogram import Dispatcher

from .admin import register_admin_handlers
from .chat import register_chat_handlers
from .user import register_user_handlers


def register_handlers(dp: Dispatcher):
    register_admin_handlers(dp)
    register_chat_handlers(dp)
    register_user_handlers(dp)
