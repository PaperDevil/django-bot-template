from telebot.types import Message

from telegram_core.telegram import TgProvider as TG


@TG.bot.message_handler(commands=['start'])
def start_handler(message: Message):
    TG.send_message(
        uid=message.chat.id,
        message="Hello Here!"
    )
