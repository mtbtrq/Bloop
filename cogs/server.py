import discord
import aiohttp
import json
import sys
import random
from discord.ext import commands


class server(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def server(self, ctx, server):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.obsidion-dev.com/api/v1/server/java?server={server}') as serverinforaw:
                serverjson = await serverinforaw.json()

                serverinfoembed = discord.Embed(title = "Server Status", description = f"{server}")
                
                serverinfoembed.add_field(name = "Online:", value = f'{serverjson["players"]["online"]}/{serverjson["players"]["max"]}', inline = False)
                
                serverinfoembed.add_field(name = "Version:", value = f'{serverjson["version"]}', inline = False)
                
                serverinfoembed.add_field(name = "Numerical IP:", value = f'{serverjson["ip"]}', inline = False)
                
                serverinfoembed.set_footer(text = "Courtesy of api.obsidion-dev.com")
                await ctx.send(embed=serverinfoembed)
               

def setup(client):
    client.add_cog(server(client))