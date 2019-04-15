import discord
from pathlib import Path
from log_sys.log_system import send_log
from initialization import Base_class
from utils.user_exp_database_manager import *
from utils.openYaml import getYaml

config = getYaml()

log_location = "user_event"


class RankedLadder(commands.Cog):

    default_experience = 100

    def __init__(self, bot):
        self.bot = bot
        print(f'Work "{self.__class__.__name__}" loaded')

    async def on_ready(self):
        ready()

    async def on_message(self, message):
        userID = message.author.id
        userName = message.author.name
        if not check_user_in_exp_database(userID):
            add_new_user_to_exp_database(userID, userName)
        if not can_user_get_exp(userID):
            return
        user_exp = get_user_exp(userID)
        match = role_matches_current_exp(user.top_role, user_exp)
        if not match:
            return
        change_top_role_here()


def setup(bot):
    bot.add_cog(RankedLadder(bot))
