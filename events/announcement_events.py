import discord
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
        try:
            if message.mention_everyone:
                channel = message.channel
                announcement_channel = discord.utils.get(message.guild.channels,
                                                         id=config['channel_text']['announcement_channel_text'])
                if channel is not announcement_channel:
                    await message.delete()
                    await channel.send("You can't use @ everyone in this battleground, it is annoying!"
                                       " Use @ here if you really need a call to arms.")
                    log_msg = f"{message.author} tried using @everyone in {channel} on {datetime.datetime.now}"
                    send_log(log_msg, log_location)
                else:
                    pass
        except Exception as error:
            send_log(str(error), log_location)

def setup(bot):
    bot.add_cog(Announcements(bot))
