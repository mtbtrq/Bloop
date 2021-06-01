import discord
from discord.ext import commands 


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def about(self, ctx):
      aboutembed = discord.Embed(title="About", description=f"Bot made by Supelion#0001 as a side project and as a introduction to python.", color=discord.Color.blue())
      aboutembed.set_footer(text="SupeBot v1.1 | Supelion#0001")
      await ctx.send(embed=aboutembed)

    @commands.command()
    async def stats(self, ctx):
      statsembed = discord.Embed(title="Bot Stats", description = "SupeBot's stats", color=discord.Color.blue())
      statsembed.add_field(name = f"Users:", value = f"```python\n{len(self.client.users)}```", inline = False)
      statsembed.add_field(name = f"Guilds:", value = f"```python\n{len(self.client.guilds)}```", inline = False)
      statsembed.set_footer(text="SupeBot v1.1 | Supelion#0001")
      await ctx.send(embed=statsembed)

    @commands.command()
    async def support(self, ctx):
      serverembed = discord.Embed(title="Support Server.", description="SupeBot Support Server: https://discord.gg/CUwrDgCB4W", color=discord.Color.blue())
      await ctx.send(embed=serverembed)
      
    @commands.command()
    async def ping(self, ctx):
      await ctx.send(f'{round(self.client.latency*1000)} ms')

    @commands.command()
    async def src(self, ctx):
      srcembed = discord.Embed(title="Source Code", url="https://github.com/Supelion/SupeBot/releases", description="SupeBot's SRC can be found on GitHub by clicking the title of this embed.", color=discord.Color.blue())
      await ctx.send(embed=srcembed)

    @commands.command()
    async def invite(self, ctx):
      invitembed = discord.Embed(color = discord.Color.blue())
      invitembed.add_field(name=f"Invite Link :link:", value = "https://discord.com/api/oauth2/authorize?client_id=835237831412547607&permissions=268762199&scope=bot")
      await ctx.send(embed=invitembed)

  
def setup(client):
    client.add_cog(Misc(client))