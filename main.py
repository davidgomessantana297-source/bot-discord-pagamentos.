
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado: {bot.user}")

@bot.command()
async def teste(ctx):
    await ctx.reply("Estou funcionando! 🚀")

token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError("Token do Discord não configurado.")

bot.run(token)
