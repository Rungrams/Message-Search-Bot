# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    ABOUT_BOT_TEXT = """
Hey! This is TeleRoid BotList Bot @PHListBot.

🤖 **My Name:** [@PHListBot](https://t.me/PHListBot)

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

👨‍💻 **Developer:** [@PredatorHackerzZ](https://t.me/PredatorHackerzZ) 

🌐 **Github :** [@PHListBot_Repo](https://github.com/PredatorHackerzZ) 

👥 **Support Group:** [TeleRoid Support](https://t.me/TeleRoid14)

📢 **Updates Channel:** [TeleRoid Updates](https://t.me/TeleRoidGroup)
"""
    ABOUT_HELP_TEXT = """Choose Bot category 😎

☛ RENAME_BOTS
☛ FILE_TO_LINK_BOTS
☛ GDRIVE_BOTS
☛ TORRENT_BOTS
☛ URL_UPLOADER_BOTS
☛ SCREENSHOT_BOTS
☛ GROUP_MANAGER_BOTS
☛ YOUTUBE_BOTS
☛ FILE_CONVERTOR_BOTS
☛ LINK_TO_FILE_BOTS

There are multiple things I can do:

🌀 I can get you Best Available Telegram Bots under AMC Projects

🌀 If u Get any Error Regarding Bots in the Botlist .Report : @TeleRoid14

😎 Our Project Channel : @TeleRoidGroup

🌀🎦 All Bots Based on your Interest will be Uploaded. You can send your feedback 

📢JOIN @TeleRoidGroup.
"""
    HOME_TEXT = """
Hello! [{}](tg://user?id={})\n\nThis is Bots Finder List Bot**@PHListBot**.

How To Use This Bot??

📜 Check Help **♻ HELP**  Section of Bot.
"""
