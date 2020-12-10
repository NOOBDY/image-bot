from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def echo(self, ctx, *args):
        output = " ".join(args)
        await ctx.send(output)

    @commands.command(pass_context=True)
    async def bot(self, ctx, *args):

        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit=1):
            messages.append(message)
        await channel.delete_messages(messages)

        output = " ".join(args)
        await ctx.send(output)


def setup(client):
    client.add_cog(Test(client))
