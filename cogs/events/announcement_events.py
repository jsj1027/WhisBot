from log_sys.log_system import send_log
import datetime
from discord.ext import commands
from utils.openYaml import yamlLoader

config = yamlLoader('config.yaml').fileObj


log_location = "user_event"


class Announcements(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

# Makes sure users cant use @everyone anywhere except the announcement channel.
    async def on_message(self, message):
        try:
            announcement_channel = self.bot.get_channel(id=config['textChannels']['announcement'])
            channel = message.channel
            if channel.id is not announcement_channel.id and '@everyone' in message.content:
                await message.delete()
                await channel.send("You can't use @ everyone in this battleground, it is annoying!"
                                   " Use @ here if you really need a call to arms.")
                log_msg = f"{message.author} tried using @everyone in {channel} on {datetime.datetime.now}"
                send_log(log_msg, log_location)
        except Exception as error:
            send_log(str(error), log_location)


def setup(bot):
    bot.add_cog(Announcements(bot))
