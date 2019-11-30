import discord
import os
from discord.ext import commands
import time
import json

with open("config.json", "r") as read_file:
    config = json.load(read_file)

TOKEN = config["token"]


client = commands.Bot(command_prefix=".")


@client.event
async def on_message(message):
    author = message.author
    print("User [{}] has sent a message".format(author))
    await client.process_commands(message)


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} module")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension} module")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
        messages.append(message)
    await channel.delete_messages(messages)
    print("Messages deleted")


client.run(TOKEN)