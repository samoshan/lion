import discord
from discord.ext import commands
from utils import checks
from utils import settings

def setup(bot):
    bot.add_cog(Plugin(bot))

def get_plugin(name):
    return settings.PLUGIN_PATH + '.' + name


class Plugin:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load', hidden=True)
    @checks.is_admin()
    async def load_plugin(self, ctx, plugin):
        try:
            self.bot.load_extension(get_plugin(plugin))
        except Exception as e:
            await ctx.send(f"{type(e).__name__} loading plugin: {plugin}")
        else:
            await ctx.send(f"**Loaded plugin:** {plugin}")


    @commands.command(name='unload', hidden=True)
    @checks.is_admin()
    async def unload_plugin(self, ctx, plugin):
        try:
            self.bot.unload_extension(get_plugin(plugin))
        except Exception as e:
            await ctx.send(f"{type(e).__name__} unloading plugin: {plugin}")
        else:
            await ctx.send(f"**Unloaded plugin:** {plugin}")


    @commands.command(name='reload', hidden=True)
    @checks.is_admin()
    async def reload_plugin(self, ctx, plugin):
        try:
            self.bot.unload_extension(get_plugin(plugin))
            self.bot.load_extension(get_plugin(plugin))
        except Exception as e:
            await ctx.send(f"{type(e).__name__} reloading plugin: {plugin}")
        else:
            await ctx.send(f"**Reloaded plugin:** {plugin}")
