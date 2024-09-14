from pyrogram import Client

class Bots:
    def __init__(self, tokens):
        self.tokens = tokens
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