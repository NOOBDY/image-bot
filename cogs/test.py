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


def setup(client):
    client.add_cog(Test(client))