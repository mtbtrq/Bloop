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
      print("The Ping Command was executed!")

    @commands.command()
    async def src(self, ctx):
      
      srcembed = discord.Embed(title="Source Code", url = "https://github.com/Supelion/Bloop", description="Bloop's SRC can be found on GitHub by clicking the title of this embed,\nor by [clicking here](http://tiny.cc/rfx2uz)", color = 0x2f3136)
      
      await ctx.reply(embed=srcembed, mention_author=False)
      print("The SRC Command was executed!")

    @commands.command()
    @commands.cooldown(1, 500,commands.BucketType.user)
    async def suggest(self, ctx, *, message):
      embed = discord.Embed()
      embed.add_field(name = "Suggestion added!", value = f"{message}")
      
      await ctx.reply(embed = embed, mention_author = False)
      print("The Suggest Command was executed!")

      channel = self.client.get_channel(837363032321294367)
      lolembed = discord.Embed(title = "New Suggestion")
      lolembed.add_field(name = f"From: {ctx.author}", value = f"Suggestion: {message}")
      await channel.send(embed = lolembed)

    @commands.command()
    async def invite(self, ctx):
      invitembed = discord.Embed(color = 0x2f3136)

      invitembed.add_field(name=f"Invite Link :link:", value = "https://bit.ly/bloopBot")
      
      await ctx.reply(embed=invitembed, mention_author=False)
      print("The Skin Command was executed!")

  
def setup(client):
    client.add_cog(Misc(client))