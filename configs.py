# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    ABOUT_BOT_TEXT = """🛑<b>My Name : @TeleRoid_Zee5_Bot</b>

<b>👨‍💻 ᴄʀᴇᴀᴛᴏʀ :</b> @PredatorHackerzZ

<b>🈂 ʟᴀɴɢᴜᴀɢᴇ :</b> <code>ᴘʏᴛʜᴏɴ3</code>

<b>📚 ʟɪʙʀᴀʀʏ :</b> <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ 1.0.7</a> 

<b>📌 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :</b> 👉 <a href='https://GitHub.com/PredatorHackerzZ/Zee5-Downloader>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>

<b>ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :</b> <a href='https://t.me/TeleRoid14'> ᴄʜᴇᴄᴋ ʜᴇʀᴇ </a>

<b> ᴛᴇʟᴇʀᴏɪᴅ ɢʀᴏᴜᴘ :</b> <a href='https://t.me/TeleRoidGroup'> Channel Updates </a>

<b> ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛʟɪꜱᴛ :</b> @TGRobot_List
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
