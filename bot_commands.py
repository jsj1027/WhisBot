from discord.ext import commands


class BotCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.command(ame="ping")
    async def ping(self):
        self.bot.wait_until_ready() #might break all the code, check if everything works then delete
        await self.bot.say(":ping_pong: ping!! xSSS")
        print("user has pinged")

    @commands.command(pass_context= True, name="info")
    async def info(self, ctx): #, member: discord.Member):
        self.bot.wait_until_ready() #might break all the code, check if everything works then delete
        user = ctx.message.author
        channel = ctx.message.channel
        role = user.top_role
        if role == "@everyone":
            role = "@ everyone"
        msg = "Oh Ho, Ho, I know a lot about you, young mortal\n"
        msg += f"Your name is {user.name}\n"
        msg += f"Your ID is {user.id}\n"
        msg += f"Your status is {user.status}\n"
        msg += f"Your best role is {role}\n"
        msg += f"And you joined this server on {user.joined_at}\n"
        await self.bot.send_message(channel, msg)
        print(f"The user {user.name}, has requested the following "
              f"Name:{user.name}, ID:{user.id}, Status:{user.status},"
              f" Role:{role}, and Join Date/Time:{user.joined_at}")


def setup(bot):
    bot.add_cog(BotCommands(bot))
