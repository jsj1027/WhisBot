import discord
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def is_author(ctx):
    user = ctx.message.author
    owner = ctx.bot.application_info()
    print(type(owner))
    if user is owner:
        return True
    else:
        return False


def is_server_owner(ctx):
    best_role = ctx.message.author.top_role
    if best_role.name == config['role_name']['server_owner']:
        return True
    else:
        return False


def is_mod(ctx):
    best_role = ctx.message.author.top_role
    if best_role.name == config['role_name']['admin']:
        return True
    else:
        return False


def server_owner_check():
    def predicate(ctx):
        return is_author(ctx) or is_server_owner(ctx)
    return commands.check(predicate)


def mod_check():
    def predicate(ctx):
        return is_mod(ctx) or is_server_owner(ctx) or is_author(ctx)
    return commands.check(predicate)
