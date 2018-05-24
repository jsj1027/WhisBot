import discord
from discord.ext import commands


class BotCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.command(ame="ping")
    async def ping(self):
        await self.bot.say(":ping_pong: ping!! xSSS")
        print("user has pinged")

    @commands.command(pass_context= True, name="info")
    async def info(self, cfx): #, member: discord.Member):
        user = cfx.message.author
        channel = cfx.message.channel
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
        print(f"The user {user.name}, has requested the following"
              f"Name:{user.name}, ID:{user.id}, Status:{user.status},"
              f" Role:{role}, and Join Date/Time:{user.joined_at}")
        #Need the to get the name, id, status, top role, and join date

def setup(bot):
    bot.add_cog(BotCommands(bot))
