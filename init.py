# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
import configparser
from log_sys.log_system import *

# config for token credit to https://github.com/nh-server/Kurisu
config = configparser.ConfigParser()
config.read("config.ini")

log_location = 'initialization'

bot = commands.Bot(command_prefix="!")

create_log_files()
works = [
    'events.bot_events',
    'events.announcement_events',
    'cogs.bot_commands'#,
  #  'cogs.mod_commands',
  #  'moderation.message_events'

]

failed_works = []

# Credit goes to https://github.com/nh-server/Kurisu/blob/master/run.py
"""
loads the extra files for the bot(cogs, event calls, etc).
"""
for work in works:
    try:
        bot.load_extension(work)
    except ValueError:
        print(TypeError)
    except Exception as x:
        msg = f'{work} failed to come train the champions. The Omni-King will not be pleased.\n{type(x).__name__}: {x}'
        send_log(msg, log_location)
        failed_works.append([work, type(x).__name__, x])

@bot.event
async def on_ready():
    try:
        guild = bot.get_guild(id=int(config['id']['guild_id']))
        channel = bot.get_channel(id=int(config['channel_text']['bot_test_text']))
        if channel in guild.channels:
            pass
        else:
            send_log(str(e), log_location)
        bot_info = await bot.application_info()
        bot_name = bot_info.name
        message = f"'Hmmm, training begins now!'\n" \
                  f"'Ho Ho Ho, my name is {bot_name}, " \
                  f"and this is the realm of the Omni-King!' - Whisbot\n"
        embed = discord.Embed(title='Whis is online', description=message)
        await channel.send(embed=embed)
        send_log(message, log_location)
    except Exception as e:
        send_log(str(e), log_location)

bot.run(config['token']['token'])
