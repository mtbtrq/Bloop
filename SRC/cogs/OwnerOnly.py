import discord
import json
import os
import aiohttp
from discord.ext import commands

class owner(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def cringe(self, ctx):
      await ctx.message.delete()
      await ctx.send('https://tenor.com/view/dies-of-cringe-cringe-gif-20747133')

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, *, msg):
      await ctx.message.delete()
      await ctx.send(f'{msg}')
      
    @commands.command()
    @commands.is_owner()
    async def bruh(self, ctx):
      await ctx.message.delete()
      await ctx.send('https://tenor.com/view/bruh-really-tell-me-more-no-way-wth-gif-21239271')

    @commands.command()
    @commands.is_owner()
    async def yes(self, ctx):
      await ctx.message.delete()
      await ctx.send('https://tenor.com/view/noob-gif-19688701')

    @commands.command(
      aliases = ["gg"]
    )
    @commands.is_owner()
    async def ggez(self, ctx):
      await ctx.message.delete()
      await ctx.send('https://tenor.com/view/gg-ez-gg-ez-gg-noobs-gg-noob-gif-17962280')

    @commands.command()
    @commands.is_owner()
    async def nice(self, ctx):
      await ctx.message.delete()
      await ctx.send('https://tenor.com/view/nice-gta-tenpenny-officer-cop-gif-16264228')

    @commands.command()
    @commands.is_owner()
    async def wtf(self, ctx):
      await ctx.message.delete()
      await ctx.send('https://tenor.com/view/wtf-is-going-on-what-stare-gif-13010497')

    @commands.command(
      aliases = ["off"]
    )
    @commands.is_owner()
    async def shutdown(self, ctx):
      await ctx.send('Bot is shutting down...')
      await self.client.close()
      print('Bot Shut Down!')

    @commands.command()
    @commands.is_owner()
    async def opinion(self, ctx):
      await ctx.message.delete()
      await ctx.send('https://tenor.com/view/an-opinion-an-opinion-is-that-an-opinion-bruh-gif-21053118')
      
    @commands.command()
    @commands.is_owner()
    async def add(self, ctx, num1 : float, num2 : float):
      ans = num1 + num2
      await ctx.send(f'**Answer:** {ans:,}')
      
    @commands.command()
    @commands.is_owner()
    async def sub(self, ctx, num1 : float, num2 : float):
      ans = num1 - num2
      await ctx.send(f"**Answer:** {ans:,}")
      
    @commands.command()
    @commands.is_owner()
    async def div(self, ctx, num1 : float, num2 : float):
      ans = num1 / num2
      await ctx.send(f"**Answer:** {ans:,}")
      
    @commands.command()
    @commands.is_owner()
    async def mult(self, ctx, num1 : float, num2 : float):
      ans = num1 * num2
      await ctx.send(f"**Answer:** {ans:,}")

    @commands.command()
    @commands.is_owner()
    async def encode(self, ctx, *, msg):
      raw = msg
      encodedMessage = ' '.join(format(ord(x), 'b') for x in raw)
      await ctx.send(encodedMessage)

    @commands.command(
      aliases = ["oh"]
    )
    @commands.is_owner()
    async def ownerhelp(self, ctx):
      
      ownerhelpembed = discord.Embed(
        color = 0xa60000
      )
      
      ownerhelpembed.add_field(name = "Misc:", value = "``opinion``, ``bruh``, ``cringe``, ``gg``, ``yes``, ``nice``, ``wtf``, ``say``, ``encode``", inline = False)
      
      ownerhelpembed.add_field(name = "Math", value = "``add``, ``sub``, ``mult``, ``div``")
      
      ownerhelpembed.add_field(name = ":no_entry: DANGEROUS: :no_entry:", value = '``shutdown``', inline = False)

      await ctx.reply(embed = ownerhelpembed)

def setup(client):
    client.add_cog(owner(client))