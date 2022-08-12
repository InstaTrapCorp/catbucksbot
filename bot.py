#Main Discord Bot funtion (CatBucks)

import os
import discord
import time

from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('iwubchu'):
            await message.channel.send("iwubchutoo")

load_dotenv()
token = os.getenv("BOT_TOKEN")
client = MyClient()
client.run(token)
time.sleep(5)