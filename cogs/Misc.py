import discord
import random
from aiohttp import ClientSession
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
      aboutembed = discord.Embed(title="About", description="Bot made by Supelion#4292 as a side project and as a introduction to python :D", color=discord.Color.blue())
      await ctx.send(embed=aboutembed)

    @commands.command()
    async def discord(self, ctx):
      serverembed = discord.Embed(title="Support Server.", description="SupeBot Support Server: https://discord.gg/CUwrDgCB4W", color=discord.Color.blue())
      await ctx.send(embed=serverembed)

    @commands.command()
    async def src(self, ctx):
      srcembed = discord.Embed(title="Source Code", url="https://github.com/Supelion/SupeBot/releases", description="SupeBot is open source and it's SRC can be found by clicking the title of this embed.", color=discord.Color.blue())
      await ctx.send(embed=srcembed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
      await ctx.channel.purge(limit=amount)
    @clear.error
    async def clear_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are not allowed to clear messages!", delete_after = 3)

    @commands.command(
        name="dadjoke",
        description="Send a dad joke!",
        aliases=['dadjokes']
    )
    async def dadjoke(self, ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': "fcd928e39dmsh8b6706ff61a7661p1d1e02jsn94f1b9f21ad7"
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")



def setup(client):
    client.add_cog(Misc(client))