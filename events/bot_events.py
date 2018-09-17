import discord
import configparser
from log_sys.log_system import *
from helpers.counters import *

config = configparser.ConfigParser()
config.read("config.ini")

log_location = "user_event"


class BotEvents:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_ready(self):
        load_potato_count()

    async def on_member_join(self, member):
        guild = member.guild
        role = discord.utils.get(guild.roles, name="Mortals")
        channel = self.bot.get(id=config['channel_text']['introduction_channel_text'])
        msg = f'Welcome {member.mention} to the Universe 7 training camp! '
        try:
            await channel.send(msg)
            new_mem = f'{member.name} joined {member.server} on {datetime.datetime.now()}'
            send_log(new_mem, log_location)
            await member.add_roles(role, reason=f"User joined the guild {guild}")
            await channel.send(content="You are now recognized by the Omni-King as a mortal wishing to social, grow, and"
                                       "most importantly train in his realm! "
                                       "Enjoy your stay, I will be watching over you")
            give_role = f"{member.name} given Mortal role in {member.server} on {datetime.datetime.now()}"
            send_log(give_role, log_location)
        except discord.Forbidden:
            await self.bot.send_message(channel, "I don't have perms to add roles.")

    async def on_message(self, message):
        if ":iamjjSuperJJ:" in message.content:
            await message.channel.send(content="JJ's power is going over 9000!")
            log_msg = f"{message.author} triggered bot_events.on_message event on {datetime.datetime.now()}"
            send_log(log_msg, log_location)
        if ":potato:" in message.content:
            update_potato_count()


def setup(bot):
    bot.add_cog(BotEvents(bot))
