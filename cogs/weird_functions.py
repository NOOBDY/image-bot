import sys
import traceback
from random import randint
from textwrap import dedent

import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.channel import TextChannel

from APIs import image, pornhub, rule34


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

    @commands.command(pass_context=True)
    @commands.is_nsfw()
    async def porn(self, ctx: Context, *args):
        keyword = " ".join(args)
        result = pornhub(args, randint(0, 9))
        if result is not None:
            # formatting and sending embed
            embed = discord.Embed(
                title=result["title"],
                description=result["url"],
                color=0xff8000
            )
            embed.set_author(name=f"Search results for: {keyword}")
            embed.set_image(url=result["thumbnail"])

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
        keyword = " ".join(args)
        result = rule34(args, randint(0, 9))

        if result["url"] is not None:
            embed = discord.Embed(
                title=f"Search results for: {keyword}",
                description=result["url"]
            )
            embed.set_image(url=result["img"])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="No results found",
                description="Try a more common keyword"
            )
            await ctx.send(embed)

    @commands.command()
    async def winnie(self, ctx: Context):
        keywords = dedent("""
            动态网自由门 天安门 天安门 法轮功 李洪志 Free Tibet
            六四天安门事件 The Tiananmen Square protests of 1989
            天安门大屠杀 The Tiananmen Square Massacre 反右派斗争
            The Anti-Rightist Struggle 大跃进政策 The Great Leap Forward
            文化大革命 The Great Proletarian Cultural Revolution 人权
            Human Rights 民运 Democratization 自由 Freedom
            独立 Independence 多党制 Multi-party system 台湾 台湾
            Taiwan Formosa 中华民国 Republic of China 西藏 土伯特 唐古特
            Tibet 达赖喇嘛 Dalai Lama 法轮功 Falun Dafa 新疆维吾尔自治区
            The Xinjiang Uyghur Autonomous Region 诺贝尔和平奖
            Nobel Peace Prize 刘暁波 Liu Xiaobo 民主 言论 思想
            反共 反革命 抗议 运动 骚乱 暴乱 骚扰 扰乱 抗暴 平反 维权
            示威游行 李洪志 法轮大法 大法弟子 强制断种 强制堕胎 民族净化
            人体实验 肃清 胡耀邦 赵紫阳 魏京生 王丹 还政于民 和平演变
            激流中国 北京之春 大纪元时报 九评论共产党 独裁 专制 压制 统一
            监视 镇压 迫害 侵略 掠夺 破坏 拷问 屠杀 活摘器官 诱拐 买卖人口
            游进 走私 毒品 卖淫 春画 赌博 六合彩 天安门 天安门
            法轮功 李洪志 Winnie the Pooh 刘晓波动态网自由门
        """)

        await ctx.send(keywords)


def setup(client: commands.Bot):
    client.add_cog(Weird(client))
