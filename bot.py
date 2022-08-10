#Main Discord Bot funtion (CatBucks)

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

client = MyClient()
client.run('TOKEN')