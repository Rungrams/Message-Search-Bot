# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    ABOUT_BOT_TEXT = """<b>Hey! This is TeleRoid BotList Bot @PHListBot.</b>

<b>🤖 **My Name:** [@PHListBot](https://t.me/PHListBot)</b>

<b>📝 **Language:** [Python3](https://www.python.org)</b>

<b>📚 **Library:** [Pyrogram](https://docs.pyrogram.org)</b>

<b>📡 **Hosted on:** [Heroku](https://heroku.com)</b>

<b>👨‍💻 **Developer:** [@PredatorHackerzZ](https://t.me/PredatorHackerzZ) </b>

<b>🌐 **Github :** [@PHListBot_Repo](https://github.com/PredatorHackerzZ) </b>

<b>👥 **Support Group:** [TeleRoid Support](https://t.me/TeleRoid14)</b>

<b>📢 **Updates Channel:** [TeleRoid Updates](https://t.me/TeleRoidGroup)</b>
"""
    ABOUT_HELP_TEXT = """Choose Bot category 😎

<b>☛ RENAME_BOTS </b>
<b>☛ FILE_TO_LINK_BOTS </b>
<b>☛ GDRIVE_BOTS </b>
<b>☛ TORRENT_BOTS </b>
<b>☛ URL_UPLOADER_BOTS </b>
<b>☛ SCREENSHOT_BOTS </b>
<b>☛ GROUP_MANAGER_BOTS</b>
<b>☛ YOUTUBE_BOTS</b>
<b>☛ FILE_CONVERTOR_BOTS</b>
<b>☛ LINK_TO_FILE_BOTS</b>

<b>There are multiple things I can do:</b>

<b>🌀 I can get you Best Available Telegram Bots under TeleRoid Projects </b>

<b>🌀 If u Get any Error Regarding Bots in the Botlist .Report : @TeleRoid14 </b>

<b>😎 Our Project Channel : @TeleRoidGroup</b>

<b>🌀🎦 All Bots Based on your Interest will be Uploaded. You can send your feedback</b>

<b>📢JOIN @TeleRoidGroup.</b>
"""
    HOME_TEXT = """<b>Hello! [{}](tg://user?id={})\n\nThis is Bots Finder List Bot**@PHListBot**.</b>

<b>How To Use This Bot??</b>

<b>📜 Check Help **♻ HELP**  Section of Bot.</b>
"""
