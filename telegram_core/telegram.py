from telebot import TeleBot
from telebot.types import ChatFullInfo, Update, Message
from django.conf import settings


class ExceptionHandler:
    @staticmethod
    def handle(exception):
        raise exception


class TgProvider(object):
    bot = TeleBot(token=settings.TELEGRAM_BOT_TOKEN)
    bot.exception_handler = ExceptionHandler

    @classmethod
    def send_message(cls, uid, message, markup=None) -> Message:
        return cls.bot.send_message(
            chat_id=uid, text=message,
            reply_markup=markup,
            parse_mode='HTML'
        )

    @classmethod
    def del_message(cls, uid, message: Message) -> bool:
        return cls.bot.delete_message(
            chat_id=uid, message_id=message.id
        )

    @classmethod
    def get_chat(cls, chat_id) -> ChatFullInfo:
        return cls.bot.get_chat(chat_id)

    @classmethod
    def dispatch(cls, update: Update):
        cls.bot.process_new_updates(updates=[update])
