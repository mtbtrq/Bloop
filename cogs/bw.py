import discord
import requests
import json
import random
import aiohttp
from discord.ext import commands

with open('./config.json') as jsonload:
    config = json.load(jsonload)

hypixelapikey = config.get('hypixelapikey')

class bw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def bw(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as bwdataraw:
                        bwdata = await bwdataraw.json()
                
                Wins = (bwdata["player"]["stats"]["Bedwars"]["wins_bedwars"])
                Levels = (bwdata["player"]["achievements"]["bedwars_level"])
                FinalDeaths = (bwdata["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
                FinalKills = (bwdata["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
                Kills = (bwdata["player"]["stats"]["Bedwars"]["kills_bedwars"])
                Deaths = (bwdata["player"]["stats"]["Bedwars"]["deaths_bedwars"])
                Coins = (bwdata["player"]["stats"]["Bedwars"]["coins"])
                winstreak = (bwdata["player"]["stats"]["Bedwars"]["winstreak"])
                FKDR = round(float(FinalKills) / float(FinalDeaths), 1) 
                IGN = (mojang_data['name'])

                bwembed = discord.Embed(
                    title='Bedwars Stats', description=f'Bedwars Stats of {IGN}', color=0x2f3136)

                bwembed.add_field(
                    name='Stars', value=f'``{Levels:,}``', inline=True)
                
                bwembed.add_field(
                    name='Wins', value=f'``{Wins:,}``', inline=True)
                
                bwembed.add_field(
                    name='Final Deaths', value=f'``{FinalDeaths:,}``', inline=True)
                
                bwembed.add_field(
                    name='FKDR', value=f'``{FKDR:,}``', inline=True)
                
                bwembed.add_field(
                    name='Coins', value=f'``{Coins:,}``', inline=True)
                
                bwembed.add_field(
                    name='Final Kills', value=f'``{FinalKills:,}``', inline=True)
                
                bwembed.add_field(
                    name='Kills', value=f'``{Kills:,}``', inline=True)
                
                bwembed.add_field(
                    name='Deaths', value=f'``{Deaths:,}``', inline=True)
                
                bwembed.add_field(
                    name='Winstreak', value=f'``{winstreak:,}``', inline=True)
                
                bwembed.set_thumbnail(
                    url='https://media.discordapp.net/attachments/836614888080015381/837749892382326834/logo.png')

                await ctx.reply(embed=bwembed, mention_author=False)


def setup(client):
    client.add_cog(bw(client))