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

    def on_ready(self):
        log_folder = Path(Path.cwd().as_posix() + '/log_files')
        log_folder.mkdir(exist_ok=True)

    def on_message(self, message):



def setup(bot):
    bot.add_cog(RankedLadder(bot))
