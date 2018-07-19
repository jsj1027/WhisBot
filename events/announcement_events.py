import discord
from discord.ext import commands
import configparser
from log_sys.log_system import send_log
import datetime

config = configparser.ConfigParser()
config.read("config.ini")

log_location = "user_event"


class Announcements:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        channel = message.channel
        announcement_channel = discord.utils.get(message.server.channels,
                                                 name=config['channel_text']['announcement_channel_text'])
        if channel is not announcement_channel:
            if message.mention_everyone:
                await self.bot.delete_message(message)
                await self.bot.send_message(channel, "You can't use '@everyone' in this channel.")
                log_msg = f"{message.author} tried using @everyone in {channel} on {datetime.datetime.now}"
                send_log(log_msg, log_location)
                print(log_msg)


def setup(bot):
    bot.add_cog(Announcements(bot))