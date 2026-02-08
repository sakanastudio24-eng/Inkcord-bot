import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # needed for prefix commands like !ping
intents.members = True          # needed for member join welcome

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (id={bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong 🩸")

bot.run(TOKEN)
