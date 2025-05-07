import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Confere se a mensagem é de si mesmo
        if message.author == self.user:
            return
        #ping pong básico
        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

# Token do bot
client.run('token')
