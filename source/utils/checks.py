import discord
from discord.ext import commands
from discord.utils import find

ADMIN_ROLE = "admin"

def is_admin():
    async def predicate(ctx):
        return find(lambda x: x.name.lower() == ADMIN_ROLE, ctx.author.roles)
    return commands.check(predicate)

def guild_only(ctx = None):
    return ctx.guild is not None
