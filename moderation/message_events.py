import configparser
from log_sys.log_system import *
from helpers.message_checker import *

config = configparser.ConfigParser()
config.read("config.ini")
whis_id = config['id']['whis_id']
log_location = "bot_moderation"


class MessageEvents:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        bad_words = check_contents(message)
        user_gained_points = point_assignment(bad_words)
        user_point_total = add_points(message.author.id, user_gained_points, bad_words)
        if user_point_total > 4:
            self.bot.ban(message.author)
            user_ban_reset(message.author.id)
            #send message saying you banned in pm
        else:
            # send message warning them of their closeness to a ban in a pm
            return

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
    bot.add_cog(MessageEvents(bot))
