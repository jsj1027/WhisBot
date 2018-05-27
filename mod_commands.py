import discord
from discord.ext import commands
import configparser
from timeout import *
import asyncio
from permission_check import *

config = configparser.ConfigParser()
config.read("config.ini")
server_owner = config['role_name']['server_owner']
admin = config['role_name']['admin']

def possible(ctx, user, victim):
    server = ctx.message.server
    if victim.top_role.name == server_owner:
        return False
    elif victim.top_role.name == admin:
        return False
    elif victim == user:
        return False
    else:
        return True

class ModCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))


    @commands.command(pass_context=True, name="timeout")
    @mod_check()
    async def timeout(self, ctx, *, arg):
        self.bot.wait_until_ready()
        command_string, user = user_parse(arg)
        timeout_until = timeout_parse(command_string)
        server = ctx.message.server
        member = discord.utils.get(server.members, id=user)
        if not possible(ctx, ctx.message.author, member):
            await self.bot.send_message(ctx.message.channel,
                                        f"{ctx.message.author.mention} you are not allowed to use this on the Omni-King,"
                                        f" other moderators, or yourself")
            print(f"{ctx.message.author} tried to use timeout on {member.name}")
            return
        timeout_role = discord.utils.get(server.roles, name=config['role_name']['timeout_role'])
        reason = f"You have been deemed an annoyance, but only a minor one, and are being put in stasis. " \
                 f"This was on order of {ctx.message.author}"
        timeout_date = datetime.datetime.now()
        await self.bot.add_roles(member, timeout_role)
        if member.voice_channel == None:
            pass
        else:
            channel = discord.utils.get(server.channels, name=config['channel_voice']['afk_channel'])
            await self.bot.move_member(member, channel)
        await self.bot.send_message(member, reason)
        await self.bot.send_message(ctx.message.channel,
                                    f"{member.mention} was timed out until {timeout_date+timedelta(seconds=timeout_until)}")
        print(f"{member.name} was timed out by {ctx.message.author}")
        await asyncio.sleep(timeout_until)
        end_reason = f"{member.name} are no longer in my stasis field, try be better this time. " \
                     f"Remember this was on order of {ctx.message.author}"
        await self.bot.remove_roles(member, timeout_role)
        await self.bot.send_message(member, end_reason)
        await self.bot.send_message(ctx.message.channel,
                                    f"{member.mention} has finished their time out, which happened on {timeout_date}")
        print(f"{member.name} finished their timeout from {ctx.message.author}")


    """
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
