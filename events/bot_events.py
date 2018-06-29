import discord
import configparser
from log_sys.log_system import *

config = configparser.ConfigParser()
config.read("config.ini")

log_location = "user_event"


class BotEvents:

    def __init__(self, bot):
        self.bot = bot
        print('Work "{}" loaded'.format(self.__class__.__name__))

    async def on_ready(self):
        create_log_files()

    async def on_member_join(self, member):
        self.bot.wait_until_ready()
        server = member.server
        role = discord.utils.get(server.roles, name="Mortals")
        channel = discord.utils.get(server.channels, name=config['channel_text']['introduction_channel_text'])
        fmt = 'Welcome {0.mention} to the Universe 7 training camp! '
        try:
            await self.bot.send_message(channel, fmt.format(member))
            new_mem = f'{member.name} joined {member.server} on {datetime.datetime.now()}'
            send_log(new_mem, log_location)
            print(new_mem)
            await self.bot.add_roles(member, role)
            await self.bot.send_message(channel, "You are now a mortal!")
            give_role = f"{member.name} given Mortal role in {member.server} on {datetime.datetime.now()}"
            print(give_role)
            send_log(give_role, log_location)
        except discord.Forbidden:
            await self.bot.send_message(channel, "I don't have perms to add roles.")

    async def on_message(self, message):
        self.bot.wait_until_ready()
        if ":SuperJJ:" in message.content:
            await self.bot.send_message(message.channel, "JJ's power is going over 9000!")
            await self.bot.process_commands(message)
            log_msg = f"{message.author} triggered bot_events.on_message event on {datetime.datetime.now()}"
            send_log(log_msg, log_location)
            print(log_msg)


def setup(bot):
    bot.add_cog(BotEvents(bot))