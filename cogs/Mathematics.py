import discord
import json
import math
from asyncio import sleep
import random
import requests
import pprint
import os
import cogs
from discord.ext import commands


class Mathematics(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready():
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('.help for help'))
        print('Ready.')

    def add(n: float, n2: float):
        return n + n2

    def sub(n: float, n2: float):
        return n - n2

    def rando(n: int, n2: int):
        return random.randint(n, n2)

    def div(n: float, n2: float):
        return n / n2

    def sqrt(n: float):
        return math.sqrt(n)

    def mult(n: float, n2: float):
        return n * n2

    @commands.command()
    async def mathadd(ctx, x: float, y: float):
        try:
            result = add(x, y)
            await ctx.send(result)

        except:
            pass

    @commands.command()
    async def mathsub(ctx, x: float, y: float):
        try:
            result = sub(x, y)
            await ctx.send(result)

        except:
            pass

    @commands.command()
    async def mathrando(ctx, x: int, y: int):
        try:
            result = rando(x, y)
            await ctx.send(result)

        except:
            pass

    @commands.command()
    async def mathdiv(ctx, x: float, y: float):
        try:
            result = div(x, y)
            await ctx.send(result)

        except:
            pass

    @commands.command()
    async def mathmult(ctx, x: float, y: float):
        try:
            result = mult(x, y)
            await ctx.send(result)

        except:
            pass

    @commands.command()
    async def mathsqrt(ctx, x: float):
        try:
            result = sqrt(x)
            await ctx.send(result)

        except:
            pass


def setup(client):
    client.add_cog(Mathematics(client))