import os
import discord
from discord.ext import commands
import sys
from random import randint
from APIs.image import image
from APIs.pornhub import pornhub

class Weird(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def image(self, ctx, *args):
        keyword, urls = image(args)
        if urls is None:
            ctx.send("No image found or some error occured. Please try again.")
        else:
            url = urls[randint(0, len(urls) - 1)]
            embed = discord.Embed(
                title=f"Search results for: {keyword}",
                description=url,
                color=0xff8000)
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def porn(self, ctx, *args):
        keyword, titles, urls, thumbs = pornhub(args)
        i = randint(0, len(urls) - 1)

        title = titles[i]
        url = urls[i]
        thumb = thumbs[i]

        embed = discord.Embed(title=title, description=url)
        embed.set_author(name=f"Search results for: {keyword}")
        embed.set_thumbnail(url=thumb)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Weird(client))
