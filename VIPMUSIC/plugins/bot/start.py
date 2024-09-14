import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from VIPMUSIC import app
# List of reactions
reactions = [
    "👍", "👎", "❤️", "🔥", "🥳", "👏", "😁", "😂", "😲", "😱", 
    "😢", "😭", "🎉", "😇", "😍", "😅", "💩", "🙏", "🤝", "🍓", 
    "🎃", "👀", "💯", "😎", "🤖", "🐵", "👻", "🎄", "🥂", "🎅", 
    "❄️", "✍️", "🎁", "🤔", "💔", "🥰", "😢", "🥺", "🙈", "🤡", 
    "😋", "🎊", "🍾", "🌟", "👶", "🦄", "💤", "😷", "👨‍💻", "🍌", 
    "🍓", "💀", "👨‍🏫", "🤝", "☠️", "🎯", "🍕", "🦾", "🔥", "💃"
]

@Client.on_message(filters.group, group=1)
async def react_to_message(client: Client, message: Message):
    emoji = random.choice(reactions)
    await message.react(emoji)


@app.on_cmd(filters.command(["starrt", "helpp"])) #try karo agar nahi work karan to hata dena 
async def start_help_command(client: Client, message: Message):
    await message.reply_text("I am an auto reaction bot. Add me in group or channels for auto react on your posts.")


import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

# List of reactions
reactions = [
    "👍", "👎", "❤️", "🔥", "🥳", "👏", "😁", "😂", "😲", "😱", 
    "😢", "😭", "🎉", "😇", "😍", "😅", "💩", "🙏", "🤝", "🍓", 
    "🎃", "👀", "💯", "😎", "🤖", "🐵", "👻", "🎄", "🥂", "🎅", 
    "❄️", "✍️", "🎁", "🤔", "💔", "🥰", "😢", "🥺", "🙈", "🤡", 
    "😋", "🎊", "🍾", "🌟", "👶", "🦄", "💤", "😷", "👨‍💻", "🍌", 
    "🍓", "💀", "👨‍🏫", "🤝", "☠️", "🎯", "🍕", "🦾", "🔥", "💃"
]

@Client.on_message(filters.text)
async def react_to_message(client: Client, message: Message):
    # Check if the chat is a group or a channel
    if message.chat.type in ["group", "supergroup", "channel"]:
        emoji = random.choice(reactions)
        await message.react(emoji)


@Client.on_message(filters.command(["start", "help"]))
async def start_help_command(client: Client, message: Message):
    await message.reply_text("I am an auto reaction bot. Add me in group or channels for auto react on your posts.")
