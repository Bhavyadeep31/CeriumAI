import os
import asyncio

import discord
from discord.ext import commands

intents = discord.Intents.all()
ceriumAI = commands.Bot(
    command_prefix="<>",
    intents=intents
)

@ceriumAI.event
async def on_ready():
    print("CeriumAI is ready and online!")

@ceriumAI.command()
async def sync(ctx):
    synced = await ceriumAI.tree.sync()
    print(f"Synced {len(synced)} command(s).")

async def loadCogs():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            await ceriumAI.load_extension(f"Cogs.{filename[:-3]}")
            print(f"Loaded the cog: {filename[:-3]}")

async def main():
    await loadCogs()
    await ceriumAI.start(os.getenv("BOT_TOKEN"))

asyncio.run(main())