import discord
from discord.ext import commands 


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client
      
    @commands.command(aliases = ["ms", "latency"])
    async def ping(self, ctx):
      
      ping = round(self.client.latency*1000)
      
      pingembed = discord.Embed(color = 0x2f3136)
      
      pingembed.add_field(name = "Pong!", value = f"{ping} ms")
      
      await ctx.reply(embed=pingembed, mention_author=False)

    @commands.command()
    async def src(self, ctx):
      
      srcembed = discord.Embed(title="Source Code", url = "https://github.com/Supelion/Bloop", description="Bloop's SRC can be found on GitHub by clicking the title of this embed,\nor by [clicking here](http://tiny.cc/rfx2uz)", color = 0x2f3136)
      
      await ctx.reply(embed=srcembed, mention_author=False)

    @commands.command()
    async def invite(self, ctx):
      invitembed = discord.Embed(color = 0x2f3136)

      invitembed.add_field(name=f"Invite Link :link:", value = "https://discord.com/api/oauth2/authorize?client_id=835237831412547607&permissions=378944&scope=bot")
      
      await ctx.reply(embed=invitembed, mention_author=False)

  
def setup(client):
    client.add_cog(Misc(client))