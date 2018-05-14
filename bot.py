# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("Hmmm, training begins now.")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)

bot.run("NDQzMTE3NDE3MTA4MDc4NTkz.Ddq3sw.XSvf5LsRxRko_1KnzRZa3-Ls_-4")