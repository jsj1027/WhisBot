import discord
from discord.ext import commands
import configparser
from timeout import *
import datetime

config = configparser.ConfigParser()
config.read("config.ini")
server_owner = config['role_name']['server_owner']
admin = config['role_name']['admin']

def server_owner_check(self):
    async def predicate(ctx):
        return ctx.message.author.top_role == server_owner
    return commands.check(predicate)

def mod_check(self):
    async def predicate(ctx):
        return (ctx.message.author.top_role == server_owner or ctx.message.author.top_role == admin)
    return commands.check(predicate)


class ModCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))


    @commands.command(pass_context=True, name="timeout")
    #@mod_check
    async def timeout(self, ctx, *, arg):
        command_string = ''
        command_string, user = user_parse(arg)
        timeout_until = timeout_parse(command_string)
        server = ctx.message.server
        member = discord.utils.get(server.members, id=user)
        print(member)

    """
    @commands.command(name="rest")
    @mod_check
    async def rest(self, ctx,):
        pass

    @rest.error
    @timeout.error
    async def mod_fail(self, ctx, command):
        user = ctx.message.author
        msg = f"{user.mention} you don't have a power level does not rival the {admin}, much less the {server_owner}"
        self.bot.send_message(ctx.message.channel, msg)
        print(f"{user.name} with {user.id} tried to access {command} server owner permission.")

    
    @error.error
    async def server_owner_fail(self, ctx, command):
        user = ctx.message.author
        msg = f"{user.mention} you don't have a power level even close to the {server_owner}"
        self.bot.send_message(ctx.message.channel, msg)
        print(f"{user.name} with {user.id} tried to access {command} server owner permission.")
    """

def setup(bot):
    bot.add_cog(ModCommands(bot))
