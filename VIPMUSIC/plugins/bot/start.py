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


@app.on_message(filters.text)
async def react_to_message(client: Client, message: Message):
    """
    This function reacts to any message with a random reaction from the 'reactions' list.
    """
    
    emoji = random.choice(reactions)
    await message.react(emoji)

@app.on_message(filters.command(["start", "help"]))
async def react_to_message(client: Client, message: Message):
    await message.reply_text("I am auto reaction bot. Add me in group or channels for auto react on your post")
