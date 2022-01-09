import os
from pytz import timezone

TZ = timezone("Asia/Ho_Chi_Minh")

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv('CHAT_ID')
DB_NAME = os.getenv('DB_NAME')
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

HACKER_NEW_FIREBASE = "https://hacker-news.firebaseio.com/v0/"
HACKER_NEW_ITEM_URL = "https://news.ycombinator.com/item?id="

AMOUNT = 5

GREETING_WORDS = ["hi", "hello", "xinchào", "xinchao"]
GREETING_WORDS_REPLY = [
    "hi", "hello", "xin chào",
    "Quen biết gì đâu mà chào",
    "Xin chào. Tui là Q (cute) Bot nè :)"]
LAUGHING = ["hihi", "haha", "hehe"]
LAUGHING_REPLY = [
    "Cười hở 10 cái răng",
    "Vui ơi là vui!",
    "hi hi",
    "đéo vui",
    "cười người hôm trước, hôm sau người cười :)",
    "một nụ cười bằng mười thang thuốc bổ"]