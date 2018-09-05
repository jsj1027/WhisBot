from discord.ext import commands
import datetime
from log_sys.log_system import send_log

log_location = "user_command"


class BotCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True, name="ping")
    async def ping(self, ctx):
        await self.bot.wait_until_ready()
        await self.bot.send_message(destination=ctx.message.channel, content=":ping_pong: ping!! xSSS, lol whis would "
                                                                             "never say this")
        log_message = f"{ctx.message.author} used ping command on {datetime.datetime.now()}"
        send_log(log_message, log_location)

    @commands.command(pass_context=True, name="info")
    async def info(self, ctx):
        await self.bot.wait_until_ready()
        user = ctx.message.author
        channel = ctx.message.channel
        role = user.top_role
        if role == "@everyone":
            role = "@ everyone"
        msg = f"Oh Ho, Ho, I know a lot about you, young mortal\n Your name is {user.name}\n Your ID is {user.id}\n " \
              f"Your status is {user.status}\n Your best role is {role}\n " \
              f"And you joined this server on {user.joined_at}\n"
        await self.bot.send_message(channel, msg)
        log_message = f"The user {user.name}, has requested the following " \
                      f"Name:{user.name}, ID:{user.id}, Status:{user.status}," \
                      f" Role:{role}, and Join Date/Time:{user.joined_at}, on {datetime.datetime.now()}"
        send_log(log_message, log_location)


def setup(bot):
    bot.add_cog(BotCommands(bot))
