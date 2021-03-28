import sys
import traceback
from random import randint

import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.channel import TextChannel

from APIs import image


class Weird(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Exception handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error):
        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, "original", error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.NSFWChannelRequired):
            # NSFW channel error

            embed = discord.Embed(
                title="Dis ain't no NSFW channel, dumbass.",
                description="Try this command again in a NSFW channel",
                color=0xff0000)
            return await ctx.send(embed=embed)

        print('Ignoring exception in command {}:'.format(
            ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command(pass_context=True)
    async def clear(self, ctx: Context, amount=5):
        channel: TextChannel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=amount+1):
            messages.append(message)
        await channel.delete_messages(messages)
        print("Messages deleted")

    @commands.command(aliases=["img"])
    async def image(self, ctx: Context, *args):
        i = randint(1, 10)
        url = image(
            args,
            "off" if ctx.channel.is_nsfw() else "active",
            i
        )

        if url is not None:
            keyword = " ".join(args)
            embed = discord.Embed(
                title=f"Search results for: {keyword}",
                description=url,
                color=0x00ffae)
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="No image found or some error occurred. Please try again."
            )
            ctx.send(embed=embed)

    @commands.command(aliases=["wash"])
    async def eyebleach(self, ctx: Context, num=3):
        num = int(num)
        keywords = ["dogs", "puppy", "kitty",
                    "cute animals", "cute pets"]
        keywords = [i.split(" ") for i in keywords]

        num = num if num <= 5 else 5

        for i in range(num):
            await ctx.send(image(keywords[randint(0, len(keywords) - 1)], "active", randint(1, 10)))


def setup(client: commands.Bot):
    client.add_cog(Weird(client))
