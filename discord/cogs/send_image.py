import os
import discord
from discord.ext import commands
import sys
from random import randint

sys.path.insert(1, "D:/Users/user/Desktop/Coding/image-bot/")

from download import download

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def image(self, ctx, *args):
        keyword = ""
        for word in args:
            keyword += word
            keyword += " "
        
        x = 0
        while x < 2:
            limit = 10
            urls = download(keyowrd=keyword, limit=limit)
            if len(urls) > 0:
                url = urls[randint(0, limit-1)]
                embed = discord.Embed(title=f"Search results for: {keyword}", description=url, color=0xff8000)
                embed.set_image(url=url)
                await ctx.send(embed=embed)
                break
            else:
                x += 1
        else:
            ctx.send("No image found or some error occured. Please try again.")


def setup(client):
    client.add_cog(Image(client))
