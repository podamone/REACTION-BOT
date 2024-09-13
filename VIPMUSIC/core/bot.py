
import pyrogram
from pyrogram import Client, filters
import config




class VIPBot(Client):
    def __init__(self, bot_token: str, bot_number: int):
        LOGGER(__name__).info(f"Initializing Bot {bot_number}")
        super().__init__(
            f"VIPMUSIC{bot_number}",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=bot_token,
        )
        self.bot_number = bot_number

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        # Simplified logging
        LOGGER(__name__).info(f"Bot {self.bot_number} started as {self.name}")

        # Check if bot is an admin in the logger group
        
def main():
    bot_tokens = [
        config.BOT_TOKEN1, config.BOT_TOKEN2, config.BOT_TOKEN3, config.BOT_TOKEN4, config.BOT_TOKEN5,
        config.BOT_TOKEN6, config.BOT_TOKEN7, config.BOT_TOKEN8, config.BOT_TOKEN9, config.BOT_TOKEN10,
        config.BOT_TOKEN11, config.BOT_TOKEN12, config.BOT_TOKEN13, config.BOT_TOKEN14, config.BOT_TOKEN15,
        config.BOT_TOKEN16, config.BOT_TOKEN17, config.BOT_TOKEN18, config.BOT_TOKEN19, config.BOT_TOKEN20
    ]

    bots = [VIPBot(token, i+1) for i, token in enumerate(bot_tokens)]

    for bot in bots:
        bot.start()

if __name__ == "__main__":
    main()
