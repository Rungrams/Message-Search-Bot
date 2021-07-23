# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    ABOUT_BOT_TEXT = f"""
𝐓𝐡𝐢𝐬 𝐢𝐬 𝐀 𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 𝐎𝐟 **@TheTeleRoid** 𝐀𝐧𝐝 𝐒𝐨𝐦𝐞 𝐎𝐭𝐡𝐞𝐫 𝐁𝐨𝐭𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦. 
🤖 **My Name:** [@𝐏𝐇𝐋𝐢𝐬𝐭𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})

📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)

📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)

📡 **Hosted on:** [𝐇𝐞𝐫𝐨𝐤𝐮](https://heroku.com)

🧑🏻‍💻 **Developer:** **@PredatorHackerzZ**

👥 **Support Group:** [𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/TeleRoid14)

📢 **Updates Channel:** [𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/TeleRoidGroup)
"""
    ABOUT_HELP_TEXT = f"""
🧑🏻‍💻 **Developer:** @PredatorHackerzZ_bot

Developer is Super Noob. Just Learning from Official Docs.\n@TheTeleRoid

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.


"""
    HOME_TEXT = """
𝐇𝐞𝐲!, [{}](tg://user?id={})\n\n𝐓𝐡𝐢𝐬 𝐈𝐬 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭**@PHListBot**.

**𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲** : **@TeamTeleRoid**\n𝐄𝐯𝐞𝐫𝐲𝐎𝐧𝐞 𝐈𝐧 𝐓𝐡𝐢𝐬 𝐉𝐨𝐮𝐫𝐧𝐞𝐲. 
"""
