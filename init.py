# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
from log_sys.log_system import *
from initialization import Base_class

# config for token credit to https://github.com/nh-server/Kurisu
Base = Base_class.Base()
Base.load_config('config.ini')
config = Base.get_config()


log_location = 'initialization'

bot = commands.Bot(command_prefix="!")

create_log_files()

training_programs = Base.get_training_programs()

failed_training_programs = Base.get_failed_training_programs()

# Credit goes to https://github.com/nh-server/Kurisu/blob/master/run.py
"""
loads the extra files for the bot(cogs, event calls, etc).
"""
for program in training_programs:
    try:
        bot.load_extension(program)
    except ValueError:
        print(TypeError)
    except Exception as x:
        msg = f'{program} failed to come train the champions.' \
              f' The Omni-King will not be pleased.\n{type(x).__name__}: {x}'
        send_log(msg, log_location)
        failed_training_programs.append([program, type(x).__name__, x])


@bot.event
async def on_ready(self):
    try:
        guild = self.bot.get_guild(id=int(self.config['id']['guild_id']))
        channel = self.bot.get_channel(id=int(self.config['channel_text']['bot_test_text']))
        if channel not in guild.channels:
            raise ValueError
        bot_info = await self.bot.application_info()
        bot_name = bot_info.name
        message = f"'Hmmm, training begins now!'\n 'Ho Ho Ho, my name is {bot_name}," \
                  f" and this is the realm of the Omni-King!' - WhisBot\n"
        embed = discord.Embed(title='Whis is online', description=message)
        await channel.send(embed=embed)
        send_log(message, self.log_location)
    except ValueError:
        send_log(str(f"{channel} not in {guild}"), self.log_location)
    except Exception as e:
        send_log(str(e), self.log_location)

bot.run(config['token']['token'])
