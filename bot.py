import discord
from keep_alive import keep_alive
class MyClient(discord.Client):

    async def on_ready(self, message):
        word_list = ['nigger','nig', 'nazi', 'cum', 'n@zi', 'pedo', 'nibba', 'nigga', 'niggera', 'niga', 'porn', 'pornhub.com', 'youporn.com',]





        if message.author == self.user:
            return

        messageContent = message.content
        if len(messageContent) > 0:
            for word in word_list:
                if word in messageContent:
                    await message.delete()
                    await message.channel.send('Hey! do not say that.')



keep_alive()
client = MyClient()
client.run('OTcwMjQ2Mzk3MDAzNjk4MTc2.GR1VZO.4WgsnrTSi6l6Cevz6i-CJBrtVjR4i5zs8hgwV0')
