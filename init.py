# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
import configparser
from log_sys.log_system import *


class Whisbot:
    # config for token credit to https://github.com/nh-server/Kurisu
    config = configparser.ConfigParser()

    log_location = 'initialization'

    bot = commands.Bot(command_prefix="!")

    training_programs = [
        'cogs.events.bot_events',
        'cogs.events.announcement_events',
        'cogs.commands.bot_commands'  # ,
        #  'cogs.mod_commands',
        #  'moderation.message_events'

    ]

    failed_training_programs = []

    def load_config(self, file_location):
        self.config.read(file_location)

#   loads the extra files for the bot(cogs, event calls, etc).
#   Credit goes to https://github.com/nh-server/Kurisu/blob/master/run.py
    def load_works(self):
        for training_program in self.training_programs:
            try:
                self.bot.load_extension(training_program)
            except Exception as x:
                msg = f'{training_program} failed to come train the champions.' \
                      f' The Omni-King will not be pleased.\n{type(x).__name__}: {x}'
                send_log(msg, self.log_location)
                self.failed_training_programs.append([training_program, type(x).__name__, x])

    @bot.event
    async def on_ready(self):
        try:
            guild = self.bot.get_guild(id=int(self.config['id']['guild_id']))
            channel = self.bot.get_channel(id=int(self.config['channel_text']['bot_test_text']))
            if channel not in guild.channels:
                raise ValueError
            bot_info = await self.bot.application_info()
            bot_name = bot_info.name
            message = f"'Hmmm, training begins now!'\n" \
                      f"'Ho Ho Ho, my name is {bot_name}, " \
                      f"and this is the realm of the Omni-King!' - WhisBot\n"
            embed = discord.Embed(title='Whis is online', description=message)
            await channel.send(embed=embed)
            send_log(message, self.log_location)
        except ValueError:
            send_log(str(f"{channel} not in {guild}"), self.log_location)
        except Exception as e:
            send_log(str(e), self.log_location)

    def run(self):
        self.bot.run(self.config['token']['token'])


def main():
    create_log_files()
    whis = Whisbot()
    whis.load_config("config.ini")
    whis.load_works()
    whis.run()
    return


main()
