#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# Get it from my.telegram.org

API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH")


## Get it from @Botfather in Telegram.
BOT_TOKEN1 = getenv("BOT_TOKEN1")
BOT_TOKEN2 = getenv("BOT_TOKEN2")
BOT_TOKEN3 = getenv("BOT_TOKEN3")
BOT_TOKEN4 = getenv("BOT_TOKEN4")
BOT_TOKEN5 = getenv("BOT_TOKEN5")
BOT_TOKEN6 = getenv("BOT_TOKEN6")
BOT_TOKEN7 = getenv("BOT_TOKEN7")
BOT_TOKEN8 = getenv("BOT_TOKEN8")
BOT_TOKEN9 = getenv("BOT_TOKEN9")
BOT_TOKEN10 = getenv("BOT_TOKEN10")
BOT_TOKEN11 = getenv("BOT_TOKEN11")
BOT_TOKEN12 = getenv("BOT_TOKEN12")
BOT_TOKEN13 = getenv("BOT_TOKEN13")
BOT_TOKEN14 = getenv("BOT_TOKEN14")
BOT_TOKEN15 = getenv("BOT_TOKEN15")
BOT_TOKEN16 = getenv("BOT_TOKEN16")
BOT_TOKEN17 = getenv("BOT_TOKEN17")
BOT_TOKEN18 = getenv("BOT_TOKEN18")
BOT_TOKEN19 = getenv("BOT_TOKEN19")
BOT_TOKEN20 = getenv("BOT_TOKEN20")

# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06


EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    "False",
)

# Fill True if you want to load extra plugins


EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/THE-VIP-BOY-OP/Extra-Plugin",
)
# Fill here the external plugins repo where plugins that you want to load


EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

# Your folder name in your extra plugins repo where all plugins stored


# Duration Limit for downloading Songs in MP3 or MP4 format from bot
