import discord
from log_sys.log_system import send_log
import datetime
from initialization import Base_class

Base = Base_class.Base()
config = Base.config

log_location = "user_event"


class Announcements:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        try:
            announcement_channel = self.bot.get_channel(id=int(config['channel_text']['announcement_channel_text']))
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
