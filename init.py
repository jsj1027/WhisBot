# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import configparser

#config for token credit to https://github.com/nh-server/Kurisu
config = configparser.ConfigParser()
config.read("config.ini")

Client = discord.Client()
bot = commands.Bot(command_prefix="!")


def send_client():
    return Client


def send_bot():
    return bot


@bot.event
async def on_ready():
    print("Hmmm, training begins now! Ho Ho Ho ")

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
config.sections()
bot.run(config['Main']['token'])
