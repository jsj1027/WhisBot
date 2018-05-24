# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
import configparser

#config for token credit to https://github.com/nh-server/Kurisu
config = configparser.ConfigParser()
config.read("config.ini")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    servers =  bot.servers
    server = discord.utils.get(servers, name=config['id']['server_id'])
    channel = discord.utils.get(server.channels, name=config['channel_text']['announcement_channel_text'])
    message = f"'Hmmm, training begins now!'\n " \
              f"'Ho Ho Ho, my name is {bot.user.name}, " \
              f"and this is the realm of the Omni-King!' - Whisbot\n"
    embed = discord.Embed(title='Whis is online', description=message)
    await bot.send_message(destination=channel, embed=embed)
    print(message)

works = [
    'bot_events',
    'bot_commands',
    'mod_commands'
]

failed_works = []

# Credit goes to https://github.com/nh-server/Kurisu/blob/master/run.py
"""
loads the extra files for the bot(commands, event calls, etc).
"""
for work in works:
    try:
        bot.load_extension(work)
    except Exception as x:
        print("{} couldn't make the fight, the OmniKing will not be pleased.\n{}: {}".format(work, type(x).__name__, x))
        failed_works.append([work, type(x).__name__, x])

bot.run(config['token']['token'])
