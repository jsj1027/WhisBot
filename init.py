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
    channel = bot.get_channel(config['Main']['bot_test'])
    message = "'Hmmm, training begins now!'\n"
    message += f"'Ho Ho Ho, my name is {bot.user.name}, and this is the realm of the Omni-King!' - Whisbot\n"
    print(message)
    embed = discord.Embed(title='Whis is online', description=message)
    await bot.send_message(destination=channel, embed=embed)

works = [
    'bot_events',
    'bot_commands'
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

bot.run(config['Main']['token'])
