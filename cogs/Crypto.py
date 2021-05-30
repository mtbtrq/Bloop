import discord
import aiohttp
import asyncio
from aiohttp import ClientSession
from discord.ext import commands


class Crypto(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(
        aliases=['btc']
    )
    async def bitcoin(self, ctx):
        async with aiohttp.ClientSession() as cs:
         async with cs.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=USD') as bitcoinraw:
          bitcoinjson = await bitcoinraw.json()
          btcprice = bitcoinjson["bitcoin"]["usd"]

        btcembed = discord.Embed(title = f"Bitcoin [BTC]", color=discord.Color.gold())
        btcembed.add_field(
        name='Price', value=f'{btcprice:,} USD', inline=True)
        btcembed.set_footer(text="Courtesy of urmom and CoinGecko API.")
        btcembed.add_field(name='Price Chart' ,value='[CryptoWatch](https://cryptowat.ch/assets/btc)', inline=False)
        btcembed.add_field(name='Conversion' ,value='[CoinGecko](https://www.coingecko.com/en/coins/bitcoin/usd)', inline=False)
        btcembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835071270117834773/844223345776263239/btc_logo.png')
        btcembed.set_footer(text="Courtesy of your mother and the CoinGecko API")
        await ctx.send(embed=btcembed)

    @commands.command(
        aliases=['eth']
    )
    async def ethereum(self, ctx):
        async with aiohttp.ClientSession() as cs:
         async with cs.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=USD') as ethraw:
          ethjson = await ethraw.json()
        ethprice = ethjson["ethereum"]["usd"]
        
        ethembed = discord.Embed(title = f"Ethereum [ETH]", color=discord.Color.purple())
        ethembed.add_field(
        name='Price', value=f'{ethprice:,} USD', inline=True)
        ethembed.set_footer(text="Courtesy of urmom and CoinGecko API.")
        ethembed.add_field(name='Price Chart' ,value='[CryptoWatch](https://cryptowat.ch/assets/eth)', inline=False)
        ethembed.add_field(name='Conversion' ,value='[CoinGecko](https://www.coingecko.com/en/coins/ethereum/usd)', inline=False)
        ethembed.set_footer(text="Courtesy of your mother and the CoinGecko API")
        ethembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835071270117834773/844223342583349248/eth_logo.png')
        await ctx.send(embed=ethembed)

    @commands.command(
        aliases=['doge']
    )
    async def dogecoin(self, ctx):
        async with aiohttp.ClientSession() as cs:
         async with cs.get('https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=USD') as dogeraw:
          dogejson = await dogeraw.json()
          dogeprice = dogejson["dogecoin"]["usd"]
        
        dogeembed = discord.Embed(title = f"DogeCoin [DOGE]", color=discord.Color.gold())
        dogeembed.add_field(
        name='Price', value=f'{dogeprice:,} USD', inline=True)
        dogeembed.set_footer(text="Courtesy of urmom and CoinGecko API.")
        dogeembed.add_field(name='Price Chart' ,value='[CryptoWatch](https://cryptowat.ch/assets/doge)', inline=False)
        dogeembed.add_field(name='Conversion' ,value='[CoinGecko](https://www.coingecko.com/en/coins/dogecoin/usd)', inline=False)
        dogeembed.set_footer(text="Courtesy of your mother and the CoinGecko API")
        dogeembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835071270117834773/844223343854223361/doge_logo.png')
        await ctx.send(embed=dogeembed)

    @commands.command(
        aliases=['ada']
    )
    async def cardano(self, ctx):
        async with aiohttp.ClientSession() as cs:
         async with cs.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=USD') as adaraw:
          adajson = await adaraw.json()
          adaprice = adajson["cardano"]["usd"]

        adaembed = discord.Embed(title = f"Cardano [ADA]", color=discord.Color.blue())
        adaembed.add_field(
        name='Price', value=f'{adaprice:,} USD', inline=False)
        adaembed.set_footer(text="Courtesy of urmom and CoinGecko API.")
        adaembed.add_field(name='Price Chart' ,value='[CryptoWatch](https://cryptowat.ch/assets/ada)', inline=False)
        adaembed.add_field(name='Conversion' ,value='[CoinGecko](https://www.coingecko.com/en/coins/cardano/usd)', inline=False)
        adaembed.set_footer(text="Courtesy of your mother and the CoinGecko API")
        adaembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835071270117834773/844227147806933012/cardano-ada-logo-1024x1024.png')
        await ctx.send(embed=adaembed)

    @commands.command(
        aliases=['bat']
    )
    async def basicattentiontoken(self, ctx):
        async with aiohttp.ClientSession() as cs:
         async with cs.get('https://api.coingecko.com/api/v3/simple/price?ids=basic-attention-token&vs_currencies=USD') as batraw:
          batjson = await batraw.json()
          batprice = batjson["basic-attention-token"]["usd"]

        batembed = discord.Embed(title = f"Basic Attention Token [BAT]", color=discord.Color.orange())
        batembed.add_field(
        name='Price', value=f'{batprice:,} USD', inline=True)
        batembed.set_footer(text="Courtesy of urmom and CoinGecko API.")
        batembed.add_field(name='Price Chart' ,value='[CryptoWatch](https://cryptowat.ch/assets/bat)', inline=False)
        batembed.add_field(name='Conversion' ,value='[CoinGecko](https://www.coingecko.com/en/coins/basic-attention-token/usd)', inline=False)
        batembed.set_footer(text="Courtesy of your mother and the CoinGecko API")
        batembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835071270117834773/844230107140325416/BAT.png')
        await ctx.send(embed=batembed)


def setup(client):
    client.add_cog(Crypto(client))