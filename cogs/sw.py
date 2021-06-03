import discord
import aiohttp
import json
import asyncio
from discord.ext import commands


with open('./config.json') as jsonload:
    config = json.load(jsonload)

hypixelapikey = config.get('hypixelapikey')

class sw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases = ["skywars", "skywar"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def sw(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as mojangraw:
                        mojang_data = await mojangraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as swdataraw:
                        swdata = await swdataraw.json()

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                          swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["player"]["stats"]["SkyWars"]["wins"])
                Heads = (swdata["player"]["stats"]["SkyWars"]["heads"])
                SwKills = (swdata["player"]["stats"]["SkyWars"]["kills"])
                SwDeaths = (swdata["player"]["stats"]["SkyWars"]["deaths"])
                SwLosses = (swdata["player"]["stats"]["SkyWars"]["losses"])
                SwCoins = (swdata["player"]["stats"]["SkyWars"]["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                IGN = str(mojang_data['name'])
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(
                    title='Skywars Stats', description=f'Skywars Stats of {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}``", inline = True)

                swembed.add_field(
                    name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(
                    name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(
                    name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(
                    name='Heads', value=f'``{Heads:,}``', inline = True)
                
                swembed.add_field(
                    name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(
                    name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(
                    name='KDR', value=f'``{SwKDR:,}``', inline = True)
                
                swembed.add_field(
                    name='Coins', value=f'``{SwCoins:,}``', inline = True)
                
                swembed.set_thumbnail(
                    url='https://media.discordapp.net/attachments/836614888080015381/837749892382326834/logo.png')

                await ctx.reply(embed=swembed, mention_author=False)


def setup(client):
    client.add_cog(sw(client))