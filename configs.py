# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNANE = os.environ.get("BOT_USERNAME","None")
    ABOUT_BOT_TEXT =  f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [File Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @PredatorHackerzZ_bot

👥 **Support Group:** [TeleRoid Support](https://t.me/TeleRoid14)

📢 **Updates Channel:** [TeleRoid Updates](https://t.me/TeleRoidGroup)
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
