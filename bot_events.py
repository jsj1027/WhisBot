import discord
from discord.ext import commands
from discord.ext.commands import Bot

class BotEvents:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @bot.event
    async def on_member_join(member):
            server = member.server
            role = discord.utils.get(server.roles, name="new role")
            fmt = 'Welcome {0.mention} to the training camp! to {1.name}'
            try:
                await bot.send_message(server, fmt.format(member, server))
                await bot.add_roles(member, role)
            except discord.Forbidden:
                await bot.send_message(server, "I don't have perms to add roles.")

    @bot.event
    async def on_message(message):
        if ":SuperJJ:" in message.content:
            await bot.send_message(message.channel, "JJ's power is going over 9000!")


def setup(bot):
    bot.add_cog(BotEvents(bot))

