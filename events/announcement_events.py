import discord
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

class Announcements:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        channel = message.channel
        announcement_channel = discord.utils.get(message.server.channels, name=config['channel_text']['announcement_channel_text'])
        if channel is not announcement_channel:
            if "@everyone" in message.content:
                await self.bot.delete_message(message)
                await self.bot.send_message(channel, "You can't use @ everyone in this channel.")
                print(f"{message.author} tried using @everyone in {channel}")
def setup(bot):
    bot.add_cog(Announcements(bot))