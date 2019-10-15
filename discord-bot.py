import discord
from discord.ext import commands
import time

TOKEN = "NjIzNTIxODM0NzEyODI1ODY2.XYDs2Q.k7MVPlAocFcDg7zCbQlSVg_HfPs"

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    author = message.author
    print("User [{}] has sent a message".format(author))
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def echo(ctx, *args):
    output = ''
    for word in args:
        output += word
        output += " "
    await ctx.send(output)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
        messages.append(message)
    await channel.delete_messages(messages)
    print("Messages deleted")


client.run(TOKEN)