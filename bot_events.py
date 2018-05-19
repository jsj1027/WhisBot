import discord


class BotEvents:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_member_join(self, member):
            server = member.server
            role = discord.utils.get(server.roles, name="Mortals")
            channel = discord.utils.get(server.channels, name="introductions")
            fmt = 'Welcome {0.mention} to the Universe 7 training camp! '
            try:
                await self.bot.send_message(channel, fmt.format(member))
                print('new member joined!')
                await self.bot.add_roles(member, role)
                print('given mortals role')
            except discord.Forbidden:
                await self.bot.send_message(channel, "I don't have perms to add roles.")

    async def on_message(self, message):
        if ":SuperJJ:" in message.content:
            await self.bot.send_message(message.channel, "JJ's power is going over 9000!")
            print("power lvl increasing")


def setup(bot):
    bot.add_cog(BotEvents(bot))

