import discord
from discord.ext import commands
from discord.ext.commands import Bot


class BotCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True, name="ping")
    async def ping(self, ctx):
        await self.bot.say(":ping_pong: ping!! xSSS")
        print("user has pinged")

    @commands.command(pass_context=True, name="info")
    async def info(self, ctx, user: discord.Member):

        channel = user.channel
        role = user.top_role.name
        if role == "@everyone":
            role = "@-everyone"
        fmt = 'Welcome {0.name} to the Universe 7 training camp! '
        print("wtfwtfwtwfw/n wtfwtfwtf/n wtfwtfwtfw/n")
        await self.bot.send_message(channel, fmt.format(user))
        #await self.bot.say("The users name is: {0.name}\n").fornat(user)
        """
        await self.bot.say("The users ID is: {}".format(member.id))
        await self.bot.say("The users status is: {}".format(member.status))
        await self.bot.say("The users highest role is: {}".format(member.top_role))
        await self.bot.say("The user joined at: {}".format(member.joined_at))
        """

def setup(bot):
    bot.add_cog(BotCommands(bot))
