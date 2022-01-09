import telebot

from generic import TOKEN, CHAT_ID
from hackernews import main, get_stories_message


if __name__ == '__main__':
    main()
    if TOKEN:
        bot = telebot.TeleBot(TOKEN, parse_mode=None)
        bot.send_message(CHAT_ID, get_stories_message())