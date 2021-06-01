import discord
import requests
import json
import random
from discord.ext import commands

hypixelapikey = "INSERT YOUR KEY HERE"

class sw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def sw(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                data = requests.get(
                    f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}").json()

                swlvllmfao = requests.get(f"https://api.slothpixel.me/api/players/{user}").json()
                
                SwWins = (data["player"]["stats"]["SkyWars"]["wins"])
                Heads = (data["player"]["stats"]["SkyWars"]["heads"])
                SwKills = (data["player"]["stats"]["SkyWars"]["kills"])
                SwDeaths = (data["player"]["stats"]["SkyWars"]["deaths"])
                SwLosses = (data["player"]["stats"]["SkyWars"]["losses"])
                SwCoins = (data["player"]["stats"]["SkyWars"]["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                IGN = str(mojang_data['name'])
                SwLvl = round(swlvllmfao["stats"]["SkyWars"]["level"], 1)

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

                await ctx.send(embed=swembed)


def setup(client):
    client.add_cog(sw(client))