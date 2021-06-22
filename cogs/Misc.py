import discord
from discord.ext import commands 


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stats(self, ctx):
      statsembed = discord.Embed(title="Bloop's Stats", color = 0x2f3136)
      statsembed.add_field(name = f"Users:", value = f"```python\n{len(self.client.users)}```", inline = False)
      statsembed.add_field(name = f"Guilds:", value = f"```python\n{len(self.client.guilds)}```", inline = False)
      statsembed.set_footer(text="Bloop v1.7 | Supelion#4275")
      await ctx.reply(embed=statsembed, mention_author=False)

    @commands.command()
    async def support(self, ctx):
      
      serverembed = discord.Embed(color = 0x2f3136)
      
      serverembed.add_field(name = "Support Server:", value = f'https://discord.gg/CUwrDgCB4W')
      
      serverembed.add_field(name = "Website:", value = f'bloopbot.ddns.net', inline = False)
      await ctx.reply(embed=serverembed, mention_author=False)

    @commands.Cog.listener()
    async def on_command(self, ctx):
      channel = self.client.get_channel(854985071639265321)
      await channel.send(f'{ctx.author.name}#{ctx.author.discriminator} executed the command ``{ctx.command}``')
      
    @commands.command(
      aliases = ["ms", "latency"]
    )
    async def ping(self, ctx):
      ping = round(self.client.latency*1000)
      pingembed = discord.Embed(
        color = 0x2f3136
      )
      pingembed.add_field(name = "Pong!", value = f"{ping} ms")
      await ctx.reply(embed=pingembed, mention_author=False)

    @commands.command()
    async def src(self, ctx):
      srcembed = discord.Embed(title="Source Code", url="https://github.com/Supelion/SupeBot/releases", description="Bloop's SRC can be found on GitHub by clicking the title of this embed.", color = 0x2f3136)
      await ctx.reply(embed=srcembed, mention_author=False)

    @commands.command()
    async def invite(self, ctx):
      invitembed = discord.Embed(color = 0x2f3136)
      invitembed.add_field(name=f"Invite Link :link:", value = "https://discord.com/api/oauth2/authorize?client_id=835237831412547607&permissions=268762199&scope=bot")
      await ctx.reply(embed=invitembed, mention_author=False)

  
def setup(client):
    client.add_cog(Misc(client))