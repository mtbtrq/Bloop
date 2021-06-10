import discord
from discord.ext import commands

class downloads(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
      aliases = ["download"]
    )
    async def downloads(self, ctx):
      
      downloadembed = discord.Embed(title = "List of Downloads:", color = 0x2f3136)
      
      downloadembed.add_field(name = "❔ Help", value = "Do .{download} for help with that specific download.", inline = False)
      
      downloadembed.add_field(name = 'Hypixel:', value = '``HypixelStatsChecker``', inline = False)
      
      downloadembed.add_field(name = 'Misc:', value = "``AutoClicker``, ``SimpleMousePos``, ``SimpleResolution``", inline = False)
      
      downloadembed.set_footer(text = "The Owner of this bot is not responsible for what you do / how you make use of the downloads.")
      
      await ctx.reply(embed=downloadembed, mention_author = False)

    @commands.command(
      aliases = ["hypixelstatschecker"]
    )
    async def HypixelStatsChecker(self, ctx):
      
      statscheckerembed = discord.Embed(title = 'HypixelStatsChecker', color = 0x2f3136)
      
      statscheckerembed.add_field(name = '❔ Information:', value = 'HypixelStatsChecker is a script made in Python that checks Hypixel stats of a given player. (Currently only supports bw, sw, and duels.)', inline = False)

      statscheckerembed.add_field(name = "Download:", value = "https://github.com/Supelion/Simple-Utils/tree/main/HypixelStats", inline = False)

      await ctx.reply(embed = statscheckerembed, mention_author = False)

    @commands.command(
      aliases = ["mousepos", "SimpleMousePos"]
    )
    async def simplemousepos(self, ctx):
      
      mouseposembed = discord.Embed(title = "SimpleMousePos", color = 0x2f3136)
      
      mouseposembed.add_field(name = "❔Information", value = "SimpleMousePos is a script written in Python that shows you your mouse' position every 2 seconds.", inline = False)

      mouseposembed.add_field(name = 'Download:', value = 'https://github.com/Supelion/Simple-Utils/tree/main/SimpleMousePos', inline = False)

      await ctx.reply(embed = mouseposembed, mention_author = False)

    @commands.command(
      aliases = ["simpleres", "simpleresolution"]
    )
    async def SimpleResolution(self, ctx):

      simpleresembed = discord.Embed(title = 'SimpleResolution', color = 0x2f3136)

      simpleresembed.add_field(name = "❔Information", value = "SimpleResolution is a script made in python that displays your screen's resolution. (Only your primary monitor's as thats the only one pyautogui supports as of writing this.)", inline = False)

      simpleresembed.add_field(name = 'Download:', value = 'https://github.com/Supelion/Simple-Utils/tree/main/SimpleResolution', inline = False)

      await ctx.reply(embed = simpleresembed, mention_author = False)

    @commands.command(
      aliases = ["autoclicker"]
    )
    async def AutoClicker(self, ctx):
      autoclickembed = discord.Embed(title = "AutoClicker", color = 0x2f3136)

      autoclickembed.add_field(name = '❔Information', value = "AutoClicker is a script made in python using the pyautogui lib that clicks wherever your cursor is every 0.5 seconds.", inline = False)

      autoclickembed.add_field(name = "Download:", value = "https://github.com/Supelion/Simple-Utils/tree/main/SimpleAutoClicker", inline = False)

      autoclickembed.set_footer(text = "The Owner of this bot is not responsible for what you do / how you make use of the downloads.")
      
      await ctx.reply(embed = autoclickembed, mention_author = False)

    @commands.command(
      aliases = ["WindowOpener"]
    )
    async def windowopener(self, ctx):

      windowembed = discord.Embed(title = 'WindowOpener', color = 0x2f3136)

      windowembed.add_field(name = "❔ Information", value = "WindowOpener is a Python Application that stores a list of directories / paths to an exe file and runs all of them upon the click of a button.")

      windowembed.add_field(name = 'Download:', value = "https://cdn.discordapp.com/attachments/835071270117834773/851323043434594334/WindowOpener.exe")
      
      await ctx.reply(embed = windowembed, mention_author = False)

def setup(client):
    client.add_cog(downloads(client))