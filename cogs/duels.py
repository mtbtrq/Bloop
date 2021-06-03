import discord
import json
import aiohttp
from discord.ext import commands

with open('./config.json') as jsonload:
    config = json.load(jsonload)

hypixelapikey = config.get('hypixelapikey')

class duels(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases = ["duel", "d"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def duels(self, ctx, user=None):
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
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as duelsdataraw:
                        duelsdat4 = await duelsdataraw.json()
                        duels = duelsdat4["player"]["stats"]["Duels"]


                duelsembed = discord.Embed(title = f'Duels Stats', description = f'Duels Stats of {mojang_data["name"]}')
                
                duelsembed.add_field(name = f"Coins", value = f'``{duels["coins"]:,}``', inline=True)

                duelsembed.add_field(name = f'Winstreak', value = f'``{duels["current_winstreak"]:,}``', inline=True)
                
                duelsembed.add_field(name = f'Wins', value = f'``{duels["wins"]:,}``', inline=True)
                
                duelsembed.add_field(name = f'Losses', value = f'``{duels["losses"]:,}``', inline=True)
                
                duelsembed.add_field(name = f'Kills', value = f'``{duels["kills"]:,}``', inline=True)
                
                duelsembed.add_field(name = f'Deaths', value = f'``{duels["deaths"]:,}``', inline=True)
                
                duelsembed.add_field(name = f'Bow Shots', value = f'``{duels["bow_shots"]:,}``', inline=True)

                duelsembed.add_field(name = f'Melee Swings', value = f'``{duels["melee_swings"]:,}``', inline=True)
                
                duelsembed.add_field(name = f'Melee Hits', value = f'``{duels["melee_hits"]:,}``', inline=True)
                
                await ctx.reply(embed=duelsembed, mention_author=False)

def setup(client):
    client.add_cog(duels(client))