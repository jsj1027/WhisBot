from log_sys.log_system import *
from utils.message_checker import *
from utils.openYaml import yamlLoader
from database.databaseManager import getDatabase

config = getDatabase("config")
config = yamlLoader('config.yaml').fileObj
whisId = config['ids']['whis']
log_location = "bot_moderation"
destination = "bot_moderation"


class MessageEvents:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_message(self, message):
        bad_words = check_contents(message)
        if not bad_words:
            return
        user_gained_points = point_assignment(bad_words)
        user_point_total = add_points(
            message.author.id, user_gained_points, bad_words)
        if user_point_total >= 4:
            await self.bot.ban(message.author)
            send_log(f"{message.author} was banned.", destination)
            user_ban_reset(message.author.id)
            msg = f"You have been banned from {message.server} due to repeated use of terrible language. No one is"
            f" required to be a saint here but we do enforce restrictions upon the worst words. If you feel"
            f" that this was a mistake please send a message to {config['roles']['serverOwner']}"
            await self.bot.send_message(message.author, msg)
        else:
            send_log(f"{message.author} was warned about their use of the word(s) {bad_words}. Their current point"
                     f" total is {user_point_total}", destination)
            msg = f"You are being warned that your language on {message.server} will not be tolerated. You have been"
            f" found saying these word(s) {bad_words}. Please refrain from repeating your this, and if you feel"
            f" this to be a mistake please contact"
            f" {config['roles']['serverOwner']} or {config['ids']['author']}"
            await self.bot.send_message(message.author, msg)

    async def on_message_delete(self, message):
        if message.author.id == whisId:
            pass
        else:
            log_msg = f"{message.author}, {message.author.id}, deleted their message on {datetime.datetime.now()}.\n" \
                      f"Their message was '{message.content}'."
            send_log(log_msg, log_location)

    async def on_message_edit(self, before, after):
        if before.author.id == whisId:
            pass
        else:
            log_msg = f"{before.author} changed their message.\n" \
                      f"Their message was '{before.content}'\n ,now it is " \
                f" '{after.content}' on {datetime.datetime.now()}"
            send_log(log_msg, log_location)
            print("message was edited")


def setup(bot):
    bot.add_cog(MessageEvents(bot))
