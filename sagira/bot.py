import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

def run_discord_bot():
    TOKEN = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True

    client = commands.Bot(command_prefix='!', intents=intents)

    @client.command()
    async def ping(ctx):
        '''Ping/Pong test message'''
        await ctx.send("pong")

    @client.command()
    async def harass(ctx, arg):
        '''Harass another user'''
        await ctx.send(f"*@{ctx.author} harasses {arg}!*")

    @client.event
    async def on_ready():
        '''Log when session has been established'''
        print(f'logged in as {client.user}')
       
    client.run(TOKEN)
