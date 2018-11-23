import discord
from pathlib import Path
from log_sys.log_system import send_log
from initialization import Base_class

Base = Base_class.Base()
config = Base.config

log_location = "user_event"


class RankedLadder:

    default_experience = 100

    def __init__(self, bot):
        self.bot = bot
        print(f'Work "{self.__class__.__name__}" loaded')

    async def on_ready(self):
        #call ready function of user_exp_database_manager.py

    async def on_message(self, message):
        user = message.author
        user_checked_value = xp_check(user)
        if user_checked_value:
            return
        user_exp = user_exp_return()
        match = role_matches_current_exp(user.top_role, user_exp)
        if not match:
            return
        change_top_role_here()



def setup(bot):
    bot.add_cog(RankedLadder(bot))
