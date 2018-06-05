#import discord
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
server_owner = config['role_name']['server_owner']
admin = config['role_name']['admin']
whis = config['role_name']['whis']


def possible(ctx, user, victim):
    msg = f"{ctx.message.author.mention} you are not allowed to use this on the " \
          f"Omni-King, me, other moderators, or yourself"
    if victim.top_role.name == whis:
        return msg
    elif victim.top_role.name == server_owner:
        return msg
    elif victim.top_role.name == admin:
        return msg
    elif victim == user:
        return msg
    else:
        msg = ''
        return msg


def is_author(ctx):
    user = ctx.message.author.id
    owner = config['id']['author_id']
    if user == owner:
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
        total = sum([is_author(ctx), is_server_owner(ctx)])
        if total > 0:
            return True
        else:
            user = ctx.message.author
            msg = f"{user.mention},only the {server_owner} has access, you can not use this command"
            raise commands.CheckFailure(msg)
    return commands.check(predicate)


def mod_check():
    def predicate(ctx):
        total = sum([is_author(ctx), is_server_owner(ctx), is_mod(ctx)])
        if total > 0:
            return True
        else:
            user = ctx.message.author
            msg = f"{user.mention}, you don't have a power level that can rival the {admin}, much less the" \
                  f" {server_owner}, you can not use this command"
            raise commands.CheckFailure(msg)
    return commands.check(predicate)
