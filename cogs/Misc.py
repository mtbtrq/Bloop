import discord
import random
from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        choices = ("Tails", "Heads")
        rancoin = random.choice(choices)
        await ctx.send(rancoin)

    @commands.command()
    async def about(self, ctx):

        await ctx.send("Bot made by Supelion#4292 as a side project and as a introduction to python :D")

    @commands.command()
    async def src(self, ctx):

        await ctx.send("SupeBot is open source and can be found at: https://github.com/Supelion/SupeBot")


def setup(client):
    client.add_cog(Misc(client))
