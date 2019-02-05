import os
import traceback
import discord
from discord.ext import commands
from utils import settings
from utils import checks
from plugins import help_menu


bot = commands.Bot(command_prefix=settings.PREFIX, fetch_offline_members=False)

# executed before plugins loaded
def init():
    bot.remove_command('help')


def start():
    init()
    load_plugins()
    bot.add_check(checks.guild_only)
    bot.run(load_token())


def load_plugins():
    loadCount = 0
    for plugin in [f.replace('.py','') for f in os.listdir(settings.PLUGIN_PATH) \
        if os.path.isfile(os.path.join(settings.PLUGIN_PATH, f))]:
        
        if plugin == "__init__":
            continue

        try:
            bot.load_extension(settings.PLUGIN_PATH + '.' + plugin)
            loadCount += 1
        except:
            print(f"Error loading plugin: {plugin}")
            traceback.print_exc()

    print(f"Loaded {loadCount} plugins")


def load_token():
    """Load the Discord API authentication token."""
    with open(settings.TOKEN_FILE, "r") as token_file:
        return token_file.read().strip()


@bot.event
async def on_ready():
    print("Ready")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        # pylint: disable=E1101
        await help_menu.Plugin.command_help_menu.invoke(ctx)


start()
