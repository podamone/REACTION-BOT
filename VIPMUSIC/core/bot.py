from pyrogram import Client, idle
from .logger import LOGGER
from config import BOT_TOKENS

log = LOGGER(__name__)

class Bots:
    def __init__(self):
        self.tokens = BOT_TOKENS
        self.clients = []
        self.client_ids = []

    async def start(self):
        self.clients.clear()
        self.client_ids.clear()
        
        for i, token in enumerate(self.tokens):
            client = Client(
                f"client_{i}",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                bot_token=token,
                plugins=dict(root="VIPMUSIC/plugins"),
                in_memory=True,
            )
            await client.start()
            self.clients.append((client, client.me.id))
            self.client_ids.append(client.me.id)

    async def stop(self):
        for client, _ in self.clients:
            await client.stop()
        self.clients.clear()
        self.client_ids.clear()

    def setup(self):
        loop = asyncio.get_event_loop_policy().get_event_loop()
        async def start():
            log.info("Starting All bots")
            await self.start()
            await idle()
            log.info("Stoping All bots...\nGoodBye")
            await self.stop()

        loop.run_until_complete(start())