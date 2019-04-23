import discord
import asyncio
import datetime
from utils.time_parse import *
from permission_check import *
from utils.command_parse import *
from log_sys.log_system import send_log
from utils.openYaml import yamlLoader

config = yamlLoader('config.yaml').fileObj
server_owner = config['roles']['serverOwner']
admin = config['roles']['admin']
whis = config['ids']['whis']

log_location = "mod_command"


class ModCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True, name="timeout")
    @mod_check()
    async def timeout(self, ctx, *args):
        victim = ctx.message.mentions
        if len(victim) > 1:
            raise commands.TooManyArguments("Limit use to one person at a time.")
        victim = victim[0]
        command_list = command_parse(args)
        timeout_role = discord.utils.get(ctx.message.server.roles, name=config['roles']['timeoutRole'])
        timeout_date = datetime.datetime.now()
        reason = f"You have been deemed an annoyance, but only a minor one, and are being put in stasis. " \
                 f"This was on order of {ctx.message.author}"
        end_reason = f"You are no longer in my stasis field(timeout), try be better this time. " \
                     f"Remember this was on order of {ctx.message.author}"
        msg = possible(ctx, ctx.message.author, victim)
        if msg is not '':
            await self.bot.send_message(ctx.message.channel, msg)
            log_msg = f"{ctx.message.author} tried to use timeout on {victim.name} on {datetime.datetime.now()}"
            print(log_msg)
            send_log(log_msg, log_location)
            return
        timeout_until = time_parse(command_list)
        await self.bot.add_roles(victim, timeout_role)
        if victim.voice_channel is not None:
            channel = discord.utils.get(ctx.message.server.channels, name=config['voiceChannels']['afk'])
            await self.bot.move_member(victim, channel)
        await self.bot.send_message(victim, reason)
        log_msg = f"{victim.mention} was timed out until {timeout_date+timedelta(seconds=timeout_until)}, by {ctx.message.author},  on {datetime.datetime.now()}"
        await self.bot.send_message(ctx.message.channel, log_msg)
        print(log_msg)
        send_log(log_msg, log_location)
        await asyncio.sleep(timeout_until)
        await self.bot.remove_roles(victim, timeout_role)
        await self.bot.send_message(victim, end_reason)
        log_msg = f"{victim.mention} has finished their time out, which happened on {timeout_date}, by {ctx.message.author}"
        send_log(log_msg, log_location)
        await self.bot.send_message(ctx.message.channel, log_msg)
        print(f"{victim.name} finished their timeout from {ctx.message.author}")

    @commands.command(pass_context=True, name='kick')
    @mod_check()
    async def kick(self, ctx, *args):
        counter = 0
        victim = ctx.message.mentions
        if len(victim) > 1:
            raise commands.TooManyArguments("Limit use to one person at a time.")
        victim = victim[0]
        server = ctx.message.server
        command_list = command_parse(args)
        kick_date = datetime.datetime.now()
        msg = possible(ctx, ctx.message.author, victim)
        if msg is not '':
            await self.bot.send_message(ctx.message.channel, msg)
            print(f"{ctx.message.author} tried to use kick on {victim.name}")
            return
        kick_until = time_parse(command_list)
        print(f"{victim.name} was kicked by {ctx.message.author} on {kick_date}")
        await self.bot.kick(victim)
        while counter < kick_until:
            if victim in server.members:
                await self.bot.kick(victim)
                print(f"{victim.name} rejoined too early and was auto kicked")
            counter += 60
            await asyncio.sleep(60)
        print(f"{victim.name} finished their kick time from {ctx.message.author}")

    @timeout.error
    @kick.error
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
