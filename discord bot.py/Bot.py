import discord
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix = "<")
client.remove_command('help')

@client.event
async def on_ready():
    print ("Bot Is Ready!")

@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send('Pong!')

@client.command(pass_context=True)
async def help(ctx):
    await ctx.send('<Ping is the only command at the moment! :shrug:')


client.run(TOKEN)