import discord
import json
import sys
import aiohttp
from discord.ext import commands

with open('./config.json') as jsonload:
    config = json.load(jsonload)

hypixelapikey = config.get('hypixelapikey')

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
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as mojangdataraw:
                    
                    try:
                      mojang_data = await mojangdataraw.json()
                    except aiohttp.client_exceptions.ContentTypeError:
                      pass

            if not mojang_data:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after=3)
            else:
                    async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as profiledataraw:
                        profiledata = await profiledataraw.json()
                    rank = profiledata["rank"]
                    
                    async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}') as guilddataraw:
                        guilddata = await guilddataraw.json()

                    if guilddata["guild"] == None:
                      guild = "None"
                    else:
                      guild = guilddata["guild"]["name"]
                      

                    if rank == "MVP_PLUS_PLUS":
                      rank = "MVP++"
                    elif rank == "MVP_PLUS":
                      rank = "MVP+"
                    elif rank == "VIP_PLUS":
                      rank = "VIP+"
                    elif rank == "NONE":
                      rank = "Non"
                    else:
                      rank = profiledata["rank"]
                    
                    
                    profileembed = discord.Embed(
                        title=f'Profile of [{rank}] {profiledata["username"]}')
                    
                    profileembed.add_field(
                        name="Karma:", value=f'{profiledata["karma"]:,}', inline=False)
                    
                    profileembed.add_field(
                        name="Network Level:", value=f'{profiledata["level"]}', inline=False)
                    
                    profileembed.add_field(
                        name="Quests completed:", value=f'{profiledata["quests_completed"]:,}', inline=False)
                    
                    profileembed.add_field(
                        name="Most Recent Game:", value=f'{profiledata["last_game"]}', inline=False)

                    profileembed.add_field(name = "Guild:", value = f'{guild}')
                    
                    profileembed.set_footer(
                        text=f"This command uses the Slothpixel API, which is slow at updating.")
                    
                    await ctx.reply(embed=profileembed, mention_author=False)


def setup(client):
    client.add_cog(profile(client))