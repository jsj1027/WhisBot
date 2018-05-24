from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
server_owner = config['role_name']['server_owner']
admin = config['role_name']['admin']


def server_owner_check(ctx):
    return ctx.message.author.top_role == server_owner


def mod_check(ctx):
    return (ctx.message.author.top_role == server_owner or ctx.message.author.top_role == admin)

class ModCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    def server_owner_fail(self, ctx, command):
        user = ctx.message.author
        msg = f"{user.mention} you don't have a power level even close to the {server_owner}"
        self.bot.send_message(ctx.message.channel, msg)
        print(f"{user.name} with {user.id} tried to access {command} server owner permission.")

    def mod_fail(self, ctx, command):
        user = ctx.message.author
        msg = f"{user.mention} you don't have a power level does not rival the {admin}, much less the {server_owner}"
        self.bot.send_message(ctx.message.channel, msg)
        print(f"{user.name} with {user.id} tried to access {command} server owner permission.")

    @commands.command(name="timeout")
    @commands.check(mod_check)
    async def timeout(self, user, command):
        pass

def setup(bot):
    bot.add_cog(ModCommands(bot))
