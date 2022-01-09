import random
import logging

import telebot

from generic import (
    TOKEN,
    GREETING_WORDS, GREETING_WORDS_REPLY,
    LAUGHING, LAUGHING_REPLY)
from hackernews import get_stories_message


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

if TOKEN:
    bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Xin chào. Tui là BotQ nè :)")

@bot.message_handler(commands=['hns'])
def send_welcome(message):
    bot.reply_to(message, get_stories_message())

@bot.message_handler(content_types=['text'])
def handle_message(message):
    msg_text = message.text.strip().lower().replace(' ', '')
    if msg_text in GREETING_WORDS:
        text = random.choice(GREETING_WORDS_REPLY)
    elif msg_text in LAUGHING:
        text = random.choice(LAUGHING_REPLY)
    else:
        text = random.choice([
            'clgt?',
            f"'{message.text}' cái quần què! "])
    bot.send_message(message.chat.id, text=text)

if __name__ == "__main__":
    bot.infinity_polling()