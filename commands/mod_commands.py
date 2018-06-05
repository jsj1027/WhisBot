import discord
import asyncio
import datetime
from helpers.timeout import *
from permission_check import *
from helpers.command_parse import *

config = configparser.ConfigParser()
config.read("config.ini")
server_owner = config['role_name']['server_owner']
admin = config['role_name']['admin']
whis = config['role_name']['whis']


class ModCommands:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True, name="timeout")
    @mod_check()
    async def timeout(self, ctx, *args):
        self.bot.wait_until_ready()
        victim = ctx.message.mentions
        if len(victim) > 1:
            raise commands.TooManyArguments("Limit use to one person at a time.")
        victim = victim[0]
        server = ctx.message.server
        command_list = command_parse(args)
        timeout_role = discord.utils.get(server.roles, name=config['role_name']['timeout_role'])
        timeout_date = datetime.datetime.now()
        reason = f"You have been deemed an annoyance, but only a minor one, and are being put in stasis. " \
                 f"This was on order of {ctx.message.author}"
        end_reason = f"You are no longer in my stasis field(timeout), try be better this time. " \
                     f"Remember this was on order of {ctx.message.author}"
        msg = possible(ctx, ctx.message.author, victim)
        if msg is not '':
            await self.bot.send_message(ctx.message.channel, msg)
            print(f"{ctx.message.author} tried to use timeout on {victim.name}")
            return
        timeout_until = timeout_parse(command_list)
        await self.bot.add_roles(victim, timeout_role)
        if victim.voice_channel is not None:
            channel = discord.utils.get(server.channels, name=config['channel_voice']['afk_channel'])
            await self.bot.move_member(victim, channel)
        await self.bot.send_message(victim, reason)
        await self.bot.send_message(ctx.message.channel,
                                    f"{victim.mention} was timed out until"
                                    f" {timeout_date+timedelta(seconds=timeout_until)}")
        print(f"{victim.name} was timed out by {ctx.message.author}")
        await asyncio.sleep(timeout_until)
        await self.bot.remove_roles(victim, timeout_role)
        await self.bot.send_message(victim, end_reason)
        await self.bot.send_message(ctx.message.channel, f"{victim.mention} has finished"
                                                         f" their time out, which happened on {timeout_date}")
        print(f"{victim.name} finished their timeout from {ctx.message.author}")

    @timeout.error
    async def mod_check_fail(self, error, ctx):
        if isinstance(error, commands.CheckFailure):
            user = ctx.message.author
            await self.bot.send_message(ctx.message.channel, error)
            print(f"{user.name} with {user.id} tried to access timeout command server owner permission.")
        elif isinstance(error, commands.TooManyArguments):
            await self.bot.send_message(ctx.message.channel, error)
            print(error)


def setup(bot):
    bot.add_cog(ModCommands(bot))
