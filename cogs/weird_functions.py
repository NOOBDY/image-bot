import discord
from discord.ext import commands

from random import randint
from APIs import (image, pornhub, rule34)

import os
import sys
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
            # NFSW channel error

            embed = discord.Embed(
                title="Dis ain't no NSFW channel, dumbass.",
                description="Try this command again in a NSFW channel",
                color=0xff0000)
            return await ctx.send(embed=embed)

        print('Ignoring exception in command {}:'.format(
            ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command(aliases=["img"])
    async def image(self, ctx, *args):
        if ctx.channel.is_nsfw():
            url = image(args, "off", randint(1, 10))
        else:
            url = image(args, "active", randint(1, 10))

        if url is not None:
            keyword = " ".join(args)
            embed = discord.Embed(
                title=f"Search results for: {keyword}",
                description=url,
                color=0x00ffae)
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        else:
            ctx.send("No image found or some error occured. Please try again.")

    @commands.command(aliases=["wash"])
    async def eyebleach(self, ctx, num=3):
        num = int(num)
        keywords = ["dogs", "puppy", "kitty",
                    "cute animals", "cute pets"]
        keywords = [i.split(" ") for i in keywords]

        num = num if num <= 5 else 5

        for i in range(num):
            await ctx.send(image(keywords[randint(0, len(keywords) - 1)], "active", randint(1, 10)))

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def porn(self, ctx, *args):
        keyword, title, url, thumb = pornhub(args, randint(1, 10))
        if url is not None:
            # formatting and sending embed
            embed = discord.Embed(
                title=title,
                description=url,
                color=0xff8000)
            embed.set_author(name=f"Search results for: {keyword}")
            embed.set_image(url=thumb)
            await ctx.send(embed=embed)
        else:
            # returns no results message if not relevant results are found
            embed = discord.Embed(
                title="No results found",
                description="Try a more common keyword!",
                color=0xff8000)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=["r34"])
    @commands.is_nsfw()
    async def rule34(self, ctx, *args):
        keyword, url, img = rule34(args, randint(1, 10))
        if url is not None:
            embed = discord.Embed(
                title=f"Search results for: {keyword}",
                description=url
            )
            embed.set_image(url=img)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="No results found",
                description="Try a more common keyword"
            )
            await ctx.send(embed)


def setup(client):
    client.add_cog(Weird(client))
