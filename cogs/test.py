from discord.ext import commands
from discord.ext.commands import Context
from discord.channel import TextChannel


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def ping(self, ctx: Context):
        await ctx.send("pong")

    @commands.command()
    async def echo(self, ctx: Context, *args):
        output = " ".join(args)
        await ctx.send(output)

    @commands.command(pass_context=True)
    async def bot(self, ctx: Context, *args):
        channel: TextChannel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=1):
            messages.append(message)
        await channel.delete_messages(messages)

        output = " ".join(args)
        await ctx.send(output)


def setup(client: commands.Bot):
    client.add_cog(Test(client))
