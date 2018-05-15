import discord
from discord.ext import commands
from discord.ext.commands import Bot


class BotCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def ping(self, ctx):
        await self.bot.say(":ping_pong: ping!! xSSS")
        print("user has pinged")

    async def info(self, ctx, user: discord.Member):
        await self.bot.say("The users name is: {}".format(user.name))
        await self.bot.say("The users ID is: {}".format(user.id))
        await self.bot.say("The users status is: {}".format(user.status))
        await self.bot.say("The users highest role is: {}".format(user.top_role))
        await self.bot.say("The user joined at: {}".format(user.joined_at))


def setup(bot):
    bot.add_cog(BotCommands(bot))
