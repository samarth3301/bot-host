import os
import discord
from discord.ext import commands
import jishaku

TOKEN = ""  # Enter your discord client's token here

intents = discord.Intents.all()
intents.presences = False

bot = commands.AutoShardedBot(
    command_prefix="-",
    intents=intents,
    owner_ids=["1207107876058046494", "1139950107995934863"]
)

@bot.event
async def on_ready():
    print("Bot is ready")
    await bot.load_extension("jishaku")


bot.run(TOKEN)
