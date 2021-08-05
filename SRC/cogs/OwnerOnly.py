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
    async def add(self, ctx, num1 : float, num2 : float, *nums : float):
        result = num1 + num2
        for num in nums:
            result += num
        await ctx.send(result)
      
    @commands.command()
    @commands.is_owner()
    async def sub(self, ctx, num1 : float, num2 : float, *nums : float):
        result = num1 - num2
        for num in nums:
            result -= num
        await ctx.send(result)
      
    @commands.command()
    @commands.is_owner()
    async def div(self, ctx, num1 : float, num2 : float, *nums : float):
        result = num1 / num2
        for num in nums:
            result /= num
        await ctx.send(result)
    
    @commands.command()
    @commands.is_owner()
    async def round(self, ctx, num : float):
      ans = round(num)
      await ctx.send(ans)
      
    @commands.command()
    @commands.is_owner()
    async def mult(self, ctx, num1 : float, num2 : float, *nums : float):
        result = num1 * num2
        for num in nums:
            result *= num
        await ctx.send(result)

    @commands.command()
    @commands.is_owner()
    async def encode(self, ctx, *, msg):
      encodeMapping = {
        ord("a"): "h",
        ord("b"): "g",
        ord("c"): "q",
        ord("d"): "l",
        ord("e"): "a",
        ord("f"): "r",
        ord("g"): "v",
        ord("h"): "w",
        ord("i"): "f",
        ord("j"): "m",
        ord("k"): "b",
        ord("l"): "c",
        ord("m"): "z",
        ord("n"): "u",
        ord("o"): "x",
        ord("p"): "o",
        ord("q"): "p",
        ord("r"): "j",
        ord("s"): "d",
        ord("t"): "e",
        ord("u"): "i",
        ord("v"): "k",
        ord("w"): "n",
        ord("x"): "s",
        ord("y"): "t",
        ord("z"): "y"
      }
      await ctx.send(input.translate(encodeMapping))

    @commands.command()
    @commands.is_owner()
    async def decode(self, ctx, input):
      decodeMapping = {
        ord("h"): "a",
        ord("g"): "b",
        ord("q"): "c",
        ord("l"): "d",
        ord("a"): "e",
        ord("r"): "f",
        ord("v"): "g",
        ord("w"): "h",
        ord("f"): "i",
        ord("m"): "j",
        ord("b"): "k",
        ord("c"): "l",
        ord("z"): "m",
        ord("u"): "n",
        ord("x"): "o",
        ord("o"): "p",
        ord("p"): "q",
        ord("j"): "r",
        ord("d"): "s",
        ord("e"): "t",
        ord("i"): "u",
        ord("k"): "v",
        ord("n"): "w",
        ord("s"): "x",
        ord("t"): "y",
        ord("y"): "z"
      }
      await ctx.send(input.translate(decodeMapping))

    @commands.command(
      aliases = ["oh"]
    )
    @commands.is_owner()
    async def ownerhelp(self, ctx):
      
      ownerhelpembed = discord.Embed(
        color = 0xa60000
      )
      
      ownerhelpembed.add_field(name = "Misc:", value = "``opinion``, ``bruh``, ``cringe``, ``gg``, ``yes``, ``nice``, ``wtf``, ``say``, ``encode``", inline = False)
      
      ownerhelpembed.add_field(name = "Math", value = "``add``, ``sub``, ``mult``, ``div``, ``round``")
      
      ownerhelpembed.add_field(name = ":no_entry: DANGEROUS: :no_entry:", value = '``shutdown``', inline = False)

      await ctx.reply(embed = ownerhelpembed)

def setup(client):
    client.add_cog(owner(client))