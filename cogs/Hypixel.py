import discord
import requests
import aiohttp
from discord.ext import commands


class Hypixel(commands.Cog):

    def __init__(self, client):
        self.client = client

    import discord
import requests
import aiohttp
from discord.ext import commands


class Hypixel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bw(self, ctx, user):
        data = requests.get(
            f"https://api.slothpixel.me/api/players/{user}").json()

        Wins = str(data["stats"]["BedWars"]["wins"])
        Levels = str(data["stats"]["BedWars"]["level"])
        Finalkd = str(data["stats"]["BedWars"]["final_k_d"])
        wlr = str(data["stats"]["BedWars"]["w_l"])
        BedsBroken = str(data["stats"]["BedWars"]["beds_broken"])
        BedsLost = str(data["stats"]["BedWars"]["beds_lost"])
        BBLR = str(data["stats"]["BedWars"]["bed_ratio"])
        FinalDeaths = str(data["stats"]["BedWars"]["final_deaths"])
        FinalKills = str(data["stats"]["BedWars"]["final_kills"])
        IGN = str(data["username"])
        

        bwembed = discord.Embed(
        title='BedWars Stats', description=f'Bedwars Stats of {IGN}', color=ctx.author.color)

        bwembed.add_field(
        name='Stars', value=f'``{Levels}``', inline=True)
        bwembed.add_field(
        name='Wins', value=f'``{Wins}``', inline=True)
        bwembed.add_field(
        name='WLR', value=f'``{wlr}``', inline=True)
        bwembed.add_field(
        name='BBLR', value=f'``{BBLR}``', inline=True)
        bwembed.add_field(
        name='Beds Broken', value=f'``{BedsBroken}``', inline=True)
        bwembed.add_field(
        name='Beds Lost', value=f'``{BedsLost}``', inline=True)
        bwembed.add_field(
        name='FKDR', value=f'``{Finalkd}``', inline=True)
        bwembed.add_field(
        name='Final Deaths', value=f'``{FinalDeaths}``', inline=True)
        bwembed.add_field(
        name='Final Kills', value=f'``{FinalKills}``', inline=True)
        bwembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/836614888080015381/837749892382326834/logo.png')

        await ctx.send(embed=bwembed)


def setup(client):
    client.add_cog(Hypixel(client))