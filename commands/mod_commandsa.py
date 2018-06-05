import discord
from helpers.timeout import *
import asyncio
from permission_check import *

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
    async def timeout(self, ctx, *, arg):
        print(ctx.message.mentions)
        users = ctx.message.mentions
        self.bot.wait_until_ready()
        command_string, user = user_parse(arg)
        server = ctx.message.server
        member = discord.utils.get(server.members, id=user)
        if not possible(ctx.message.author, member):
            await self.bot.send_message(ctx.message.channel,
                                        f"{ctx.message.author.mention} you are not allowed to use this on the"
                                        f" Omni-King, me, other moderators, or yourself")
            print(f"{ctx.message.author} tried to use timeout on {member.name}")
            return
        timeout_until = timeout_parse(command_string)
        timeout_role = discord.utils.get(server.roles, name=config['role_name']['timeout_role'])
        reason = f"You have been deemed an annoyance, but only a minor one, and are being put in stasis. " \
                 f"This was on order of {ctx.message.author}"
        timeout_date = datetime.datetime.now()
        await self.bot.add_roles(member, timeout_role)
        if member.voice_channel is None:
            pass
        else:
            channel = discord.utils.get(server.channels, name=config['channel_voice']['afk_channel'])
            await self.bot.move_member(member, channel)
        await self.bot.send_message(member, reason)
        await self.bot.send_message(ctx.message.channel,
                                    f"{member.mention} was timed out until"
                                    f" {timeout_date+timedelta(seconds=timeout_until)}")
        print(f"{member.name} was timed out by {ctx.message.author}")
        await asyncio.sleep(timeout_until)
        end_reason = f"{member.name} are no longer in my stasis field, try be better this time. " \
                     f"Remember this was on order of {ctx.message.author}"
        await self.bot.remove_roles(member, timeout_role)
        await self.bot.send_message(member, end_reason)
        await self.bot.send_message(ctx.message.channel,
                                    f"{member.mention} has finished their time out, which happened on {timeout_date}")
        print(f"{member.name} finished their timeout from {ctx.message.author}")

    @timeout.error
    async def mod_check_fail(self, error, ctx):
        if isinstance(error, commands.CheckFailure):
            user = ctx.message.author
            print(f"{user.name} with {user.id} tried to access timeout command server owner permission.")
            await self.bot.send_message(ctx.message.channel, error)


def setup(bot):
    bot.add_cog(ModCommands(bot))
