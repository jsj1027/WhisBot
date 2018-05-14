# Whisbot by jsj1027/kaloshade

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')
client = discord.Client()

@bot.event
async def on_ready():
    print("Hmmm, training begins now.")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The user's name is: {}".format(user.name))
    await bot.say("The user's ID is: {}".format(user.id))
    await bot.say("The user's status is: {}".format(user.status))
    await bot.say("The user's highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.event
async def on_member_join(member):
        server = member.server
        role = discord.utils.get(server.roles, name="new role")
        fmt = 'Welcome {0.mention} to the training camp! to {1.name}'
        await client.send_message(server, fmt.format(member, server))
        await client.add_roles(member, role)


bot.run("token")
