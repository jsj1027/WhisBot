from discord.ext import commands
import datetime
from log_sys.log_system import send_log
from utils.counters import getPotatoCount

log_location = "user_command"


class BotCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

# Tells the user hello!
    @commands.command(name='hello')
    async def hello(self, ctx):
        try:
            await ctx.send(content=f'Hello young {ctx.author.top_role}, how are you today?')
        except Exception as error:
            send_log(str(error), log_location)

# Pings the user, not a latency command
    @commands.command(name="ping")
    async def ping(self, ctx):
        try:
            await ctx.send(content=":ping_pong: Ooo, I believe they call this game table tennis, I would love to play")
            log_message = f"{ctx.message.author} used ping command on {datetime.datetime.now()}"
            send_log(log_message, log_location)
        except Exception as error:
            send_log(str(error), log_location)

# Shows how many times chat has spammed potato
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.channel)
    @commands.command(name="potato")
    async def potato(self, ctx):
        try:
            await ctx.send(content=f"Even the Omni-King messes up!"
                                   f" Currently the audience potato count is"
                                   f" {getPotatoCount()}")
        except Exception as error:
            send_log(str(error), log_location)

# Shows user their generic discord user info
    @commands.command(pass_context=True, name="info")
    async def info(self, ctx):
        try:
            user = ctx.author
            role = user.top_role
            if role is "@everyone":
                role = "@ everyone"
            msg = f"Oh Ho, Ho, I know a lot about you, young {role}\n " \
                  f"Your name is {user.name}\n " \
                  f"Your ID is {user.id}\n " \
                  f"Your status is {user.status}\n " \
                  f"Your best role is {role}\n " \
                  f"And you joined this server on {user.joined_at}\n"
            await ctx.send(content=msg)
            log_message = f"The user {user.name}, has requested the following " \
                          f"Name:{user.name}, ID:{user.id}, Status:{user.status}," \
                          f" Role:{role}, and Join Date/Time:{user.joined_at}, on {datetime.datetime.now()}"
            send_log(log_message, log_location)
        except Exception as error:
            send_log(str(error), log_location)


def setup(bot):
    bot.add_cog(BotCommands(bot))
