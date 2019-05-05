from discord.ext import commands
from log_sys.log_system import *
from utils.message_checker import *
from utils.openYaml import yamlLoader
from database.databaseManager import getDatabase

config = getDatabase("config")
config = yamlLoader('config.yaml').fileObj
whisId = config['ids']['whis']
log_location = "bot_moderation"
destination = "bot_moderation"


class MessageEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.Cog.listener()
    async def on_message(self, message):
        bad_words = check_contents(message)
        if not bad_words:
            return
        user_gained_points = point_assignment(bad_words)
        calculate_user_points(message.author.id, user_gained_points, bad_words)
        userFromModeration = grab_user_from_database(message.author.id)
        user_point_total = userFromModeration[1]
        print(user_point_total)
        if user_point_total >= 4:  # move all this to a function
            msg = (f"You have been banned from {message.guild} due to repeated use of terrible language. No one is"
                   f" required to be a saint here but we do enforce restrictions upon the worst words. If you feel"
                   f" that this was a mistake please send a message to {config['roles']['serverOwner']}")
            await message.author.send(msg)
            send_log(f"{message.author} was banned.", destination)
            user_ban_reset(message.author.id)
            await message.guild.ban(message.author)

        else:
            send_log(f"{message.author} was warned about their use of the word(s) {bad_words}. Their current point"
                     f" total is {user_point_total}", destination)
            msg = (f"You are being warned, your language on {message.guild} "
                   f"will not be tolerated. You have been found saying these "
                   f"word(s) {bad_words}. Please refrain from repeating "
                   f"your mistake, and if you feel this to be a mistake"
                   f" please contact the {config['roles']['admin']} or the"
                   f" {config['roles']['serverOwner']}")
            await message.author.send(msg)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.id == whisId:
            pass
        else:
            log_msg = f"{message.author}, {message.author.id}, deleted their message on {datetime.datetime.now()}.\n" \
                      f"Their message was '{message.content}'."
            send_log(log_msg, log_location)

    @commands.Cog.listener()
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
