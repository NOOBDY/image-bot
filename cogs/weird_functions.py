import os
import discord
from discord.ext import commands
import sys
from random import randint
from APIs.image import image
from APIs.pornhub import pornhub
import traceback

class Weird(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Exception handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, "original", error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.NSFWChannelRequired):
            embed = discord.Embed(
                title="Dis ain't no NSFW channel, dumbass.",
                description="Try this command again in a NSFW channel",
                color=0xff0000)
            return await ctx.send(embed=embed)
        
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


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
                color=0x00ffae)
            embed.set_image(url=url)
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def porn(self, ctx, *args):
        keyword, titles, urls, thumbs = pornhub(args)
        i = randint(0, len(urls) - 1)

        title = titles[i]
        url = urls[i]
        thumb = thumbs[i]

        embed = discord.Embed(
            title=title,
            description=url,
            color=0xff8000)
        embed.set_author(name=f"Search results for: {keyword}")
        embed.set_thumbnail(url=thumb)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Weird(client))
