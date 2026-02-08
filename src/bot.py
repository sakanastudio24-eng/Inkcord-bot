import os
import asyncio
import logging
from datetime import datetime
from typing import Optional, Literal
import random
import discord
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError("DISCORD_TOKEN is not set in .env")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.command(name="ping")
async def ping(ctx: commands.Context) -> None:
    await ctx.send("Pong!")


@bot.command(name="hello")
async def hello(ctx: commands.Context) -> None:
    await ctx.send("Hello!")


bot.run(token)
