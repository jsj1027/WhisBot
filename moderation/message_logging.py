import configparser
from log_sys.log_system import *

config = configparser.ConfigParser()
config.read("config.ini")
whis_id = config['id']['whis_id']
log_location = "bot_moderation"


class MessageLog:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_message_delete(self, message):
        self.bot.wait_until_ready()
        if message.author.id == whis_id:
            pass
        else:
            log_msg = f"{message.author}, {message.author.id}, deleted their message on {datetime.datetime.now()}.\n" \
                      f"Their message was {message.content}."
            send_log(log_msg, log_location)

    async def on_message_edit(self, before, after):
        self.bot.wait_until_ready()
        if before.author.id == whis_id:
            pass
        else:
            log_msg = f"{before.author} changed their message.\n" \
                      f"Their message was '{before.content}'\n ,now it is " \
                       f" '{after.content}' on {datetime.datetime.now()}"
            send_log(log_msg, log_location)
            print("message was edited")


def setup(bot):
    bot.add_cog(MessageLog(bot))