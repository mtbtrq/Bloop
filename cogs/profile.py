import discord
import requests
import json
import sys
import random
from discord.ext import commands

hypixelapikey = "INSERT YOUR KEY HERE"

class profile(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
      aliases = ["p"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def profile(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after=3)
        else:
            mojang_data = requests.get(
                f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()

            if not mojang_data:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after=3)
            else:
                    profiledata = requests.get(
                        f"https://api.slothpixel.me/api/players/{user}").json()
                    guildinfo = requests.get(
                        f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}').json()
                    guild = guildinfo["guild"]["name"]
                    rank = profiledata["rank"]

                    if not guildinfo:
                      guild = None
                    else:
                      guild = guildinfo["guild"]["name"]

                    if rank == "MVP_PLUS_PLUS":
                      rank = "MVP++"
                    elif rank == "MVP_PLUS":
                      rank = "MVP+"
                    elif rank == "VIP_PLUS":
                      rank = "VIP+"
                    elif rank == None:
                      rank = "Non"
                    else:
                      rank = profiledata["data"]
                    
                    
                    profileembed = discord.Embed(
                        title=f'Profile of {profiledata["username"]}')
                    profileembed.add_field(
                        name="Rank:", value=f'{profiledata["rank"]}', inline=False)
                    profileembed.add_field(
                        name="Karma:", value=f'{profiledata["karma"]:,}', inline=False)
                    profileembed.add_field(
                        name="Network Level:", value=f'{profiledata["level"]}', inline=False)
                    profileembed.add_field(
                        name="Quests completed:", value=f'{profiledata["quests_completed"]:,}', inline=False)
                    profileembed.add_field(
                        name="Most Recent Game:", value=f'{profiledata["last_game"]}', inline=False)
                    profileembed.add_field(
                        name="Guild:", value=f'{guildinfo["guild"]["name"]}')
                    profileembed.set_footer(
                        text=f"This command uses the Slothpixel API, which is slow at updating.")
                    await ctx.send(embed=profileembed)
               

def setup(client):
    client.add_cog(profile(client))