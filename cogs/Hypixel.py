import discord
import requests
from discord.ext import commands

class Hypixel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nwlevel(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(data["level"])

    @commands.command()
    async def karma(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["karma"]) +
        " Karma."
        )

    @commands.command()
    async def duelswlr(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["Duels"]["general"]["win_loss_ratio"]) +
        " W/L Ratio."
        )

    @commands.command()
    async def bwwins(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["BedWars"]["wins"]) + 
        " Wins."
        )

    @commands.command()
    async def bwlevel(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["BedWars"]["level"]) + 
        " Stars."
        )

    @commands.command()
    async def bwwlr(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["BedWars"]["w_l"]) + 
        " W/L Ratio."
        )

    @commands.command()
    async def bwfkdr(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["BedWars"]["final_k_d"]) + 
        " FKDR."
        )

    @commands.command()
    async def duelskdr(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["Duels"]["general"]["kd_ratio"]) +
        " KDR."
        )

    @commands.command()
    async def duelswins(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["Duels"]["general"]["wins"]) +
        " Wins."
        )

    @commands.command()
    async def duelskills(self, ctx, user):
        data = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(
        str(data["stats"]["Duels"]["general"]["kills"]) +
        " Kills."
        )


def setup(client):
  client.add_cog(Hypixel(client))