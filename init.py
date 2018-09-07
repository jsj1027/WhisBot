# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
import configparser
from log_sys.log_system import *

# config for token credit to https://github.com/nh-server/Kurisu
config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix="!")


works = [
    'events.bot_events',
   # 'events.announcement_events',
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
    except Exception as x:
        print("{} couldn't make the fight, the OmniKing will not be pleased.\n{}: {}".format(work, type(x).__name__, x))
        failed_works.append([work, type(x).__name__, x])

@bot.event
async def on_ready():
    guild = bot.get_guild(id=int(config['id']['guild_id']))
    channel = bot.get_channel(id=int(config['channel_text']['bot_test_text']))
    if channel in guild.channels:
        pass
    else:
        print(Exception)
    bot_info= await bot.application_info()
    bot_name = bot_info.name
    message = f"'Hmmm, training begins now!'\n" \
              f"'Ho Ho Ho, my name is {bot_name}, " \
              f"and this is the realm of the Omni-King!' - Whisbot\n"
    embed = discord.Embed(title='Whis is online', description=message)
    await channel.send(embed=embed)
    create_log_files()
    send_log(message, "initialization")


bot.run(config['token']['token'])


