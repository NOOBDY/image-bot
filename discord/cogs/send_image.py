import os
import discord
from discord.ext import commands

class Image(commands.Cog):
    def __init__(self, client, channel):
        self.client = client
        self.channel = channel

    @commands.command()
    async def image(self, ctx):
        await client.send_file("downloads/apple/1.open_graph_logo.png")

def setup(client):
    client.add_cog(Image(client))