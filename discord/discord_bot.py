import discord
import os
from discord.ext import commands
import time

TOKEN = "NjIzNTIxODM0NzEyODI1ODY2.XeHUOg.pz5ZO4h4JXUWA3nmOS3fG4iVdjo"

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


for filename in os.listdir("./discord/cogs"):
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