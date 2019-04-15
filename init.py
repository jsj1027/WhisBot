# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
from log_sys.log_system import *
from initialization import Base_class
from utils.openYaml import getYaml()

Base = Base_class.Base()
config = getYaml()

log_location = Base.get_log_location()

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
        print(ValueError)
    except Exception as x:
        msg = f'{program} failed to come train the champions.' \
              f' The Omni-King will not be pleased.\n{type(x).__name__}: {x}'
        send_log(msg, log_location)
        failed_training_programs.append([program, type(x).__name__, x])

Base.set_failed_training_programs(failed_training_programs)


@bot.event
async def on_ready():
    try:
        guild = bot.get_guild(id=config['ids']['guild'])
        channel = bot.get_channel(
            id=config['textChannels']['announcement'])
        if channel not in guild.channels:
            raise ValueError
        bot_info = await bot.application_info()
        bot_name = bot_info.name
        message = f"'Hmmm, training begins now!'\n 'Ho Ho Ho, my name is {bot_name},"
                  f" and this is the realm of the Omni-King!' - WhisBot\n"
        embed = discord.Embed(title='Whis is online', description=message)
        await channel.send(embed=embed)
        send_log(message, log_location)
    except ValueError:
        send_log(str(f"{channel} not in {guild}"), log_location)
    except Exception:
        send_log(str(Exception), log_location)

bot.run(config['token'])
