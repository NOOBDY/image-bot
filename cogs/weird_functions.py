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
        keyword, title, url, thumb = pornhub(args, randint(0, 9))
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
        keyword, url, img = rule34(args, randint(0, 9))
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

    @commands.command()
    async def winnie(self, ctx: Context):
        keywords = dedent("""
            动态网自由门 天安門 天安门 法輪功 李洪志 Free Tibet
            六四天安門事件 The Tiananmen Square protests of 1989
            天安門大屠殺 The Tiananmen Square Massacre 反右派鬥爭
            The Anti-Rightist Struggle 大躍進政策 The Great Leap Forward
            文化大革命 The Great Proletarian Cultural Revolution 人權
            Human Rights 民運 Democratization 自由 Freedom
            獨立 Independence 多黨制 Multi-party system 台灣 臺灣
            Taiwan Formosa 中華民國 Republic of China 西藏 土伯特 唐古特
            Tibet 達賴喇嘛 Dalai Lama 法輪功 Falun Dafa 新疆維吾爾自治區
            The Xinjiang Uyghur Autonomous Region 諾貝爾和平獎
            Nobel Peace Prize 劉暁波 Liu Xiaobo 民主 言論 思想
            反共 反革命 抗議 運動 騷亂 暴亂 騷擾 擾亂 抗暴 平反 維權
            示威游行 李洪志 法輪大法 大法弟子 強制斷種 強制堕胎 民族淨化
            人體實驗 肅清 胡耀邦 趙紫陽 魏京生 王丹 還政於民 和平演變
            激流中國 北京之春 大紀元時報 九評論共産黨 獨裁 專制 壓制 統一
            監視 鎮壓 迫害 侵略 掠奪 破壞 拷問 屠殺 活摘器官 誘拐 買賣人口
            遊進 走私 毒品 賣淫 春畫 賭博 六合彩 天安門 天安门
            法輪功 李洪志 Winnie the Pooh 劉曉波动态网自由门
        """)

        await ctx.send(keywords)


def setup(client: commands.Bot):
    client.add_cog(Weird(client))
