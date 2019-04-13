import discord
from discord.ext import commands
from initialization import Base_class
from log_sys.log_system import *
from helpers.counters import updatePotatoCount

Base = Base_class.Base()
config = Base.config

log_location = "user_event"


class BotEvents(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if u"\U0001F954" in message.content:
                updatePotatoCount()
            elif ":iamjjSuperJJ:457429491766001664" in message.content:
                await message.channel.send(
                    content="JJ's power is going over 9000!")
                log_msg = f"{message.author} triggered bot_events.on_message\
                     event on {datetime.datetime.now()}"
                send_log(log_msg, log_location)
        except Exception as e:
            send_log(str(e), log_location)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            guild = member.guild
            role = guild.get_role(int(config['role_name']['mortals']))
            channel = self.bot.get_channel(
                int(config['channel_text']['introduction_channel_text']))
            msg = f'Welcome {member.mention} to the Universe 7 training camp! '
            await channel.send(msg)
            new_mem_msg = f'{member.name} joined {guild.name} \
                on {datetime.datetime.now()}'
            send_log(new_mem_msg, log_location)
            await member.add_roles(role, reason=f"User\
                 joined the guild {guild.name}")
            await channel.send(content="You are\
                 now recognized by the Omni-King as a mortal wishing to social\
                     , grow, and most importantly train in his realm!\
                          Enjoy your stay, I will be watching over you")
            given_role_msg = f"{member.name}\
                 given Mortal role in {guild.name}\
                      on {datetime.datetime.now()}"
            send_log(given_role_msg, log_location)
        except discord.Forbidden:
            send_log("I don't have permission to add roles.", log_location)
        except Exception as e:
            send_log(str(e), log_location)


def setup(bot):
    bot.add_cog(BotEvents(bot))
