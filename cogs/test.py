import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def echo(self, ctx, *args):
        output = ''
        for word in args:
            output += word
            output += " "
        await ctx.send(output)

    @commands.command(pass_context=True)
    async def bot(self, ctx, *args):

        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=1):
            messages.append(message)
        await channel.delete_messages(messages)
        await client
        
        o = ""
        for c in args:
            o += c
            o += " "
        await ctx.send(o)

def setup(client):
    client.add_cog(Test(client))