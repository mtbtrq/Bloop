import json
import aiohttp
import io
import asyncio
import tracemalloc
from datetime import datetime

from utils import hywrap

import time

import discord
from discord.ext import commands

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

with open('./config.json') as jsonload:
  config = json.load(jsonload)

hypixelapikey = config.get('hypixelapikey')

class minecraft(commands.Cog):

    def __init__(self, client):
      self.client = client
      self.orangey = 246, 76, 114
      self.white = 255, 255, 255
      self.green = 34, 227, 82
      self.red = 255, 0, 34
      self.dark_green = 0, 170, 0
      self.gold = 255, 170, 0
      self.red = 170, 0, 0
      self.aqua = 85, 255, 255
      self.light_red = 255, 85, 85

    @commands.command(aliases = ["bed", "bedwarz", "bedwars", "bedworz", "bedwar"])
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def bw(self, ctx, user : str = None, gamemode : str = 'overall'):
        print("The BW Command was executed!")
        start = datetime.utcnow()
        mode = gamemode.lower()
        if user is None:
            errorembed = discord.Embed(title = 'Bedwars')
            errorembed.add_field(name = 'Usage:', value = "``.bw {IGN} {mode}``", inline = False)
            errorembed.add_field(name = '❔', value = 'Returns the BedWars stats of a specified player.', inline = False)
            errorembed.add_field(name = 'Aliases:', value = '``bw, bed, bedwarz, bedwars, bedworz, bedwar``', inline = False)
            errorembed.set_footer(text = 'Valid Modes: Overall, Solo, Doubles, Threes, Fours')
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                  async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                    mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`")

            IGN = mojang_data["name"]

            if mode == 'overall':
                try:
                  bwdata = await hywrap.bedwars(mojang_data["id"], hypixelapikey)
                  profiledata = await hywrap.player(mojang_data["id"], hypixelapikey)

                  wins = 0
                  Kills = 0
                  deaths = 0
                  deathsVoid = 0
                  killsVoid = 0
                  brokenBeds = 0
                  lostBeds = 0
                  losses = 0
                  stars = 0
                  DeathsFinal = 0
                  KillsFinal = 0
                  winstreak = 0

                  wins += int(bwdata["wins_bedwars"])
                  Kills += int(bwdata["kills_bedwars"])
                  deaths += int(bwdata["deaths_bedwars"])
                  deathsVoid += int(bwdata["void_deaths_bedwars"])
                  killsVoid += int(bwdata["void_kills_bedwars"])
                  brokenBeds += int(bwdata["beds_broken_bedwars"])
                  lostBeds += int(bwdata["beds_lost_bedwars"])
                  losses += int(bwdata["losses_bedwars"])
                  stars += int(profiledata["player"]["achievements"]["bedwars_level"])
                  DeathsFinal += int(bwdata["final_deaths_bedwars"])
                  KillsFinal += int(bwdata["final_kills_bedwars"])
                  winstreak += int(bwdata["winstreak"])
                  
                  FKDR = round(float(KillsFinal) / float(DeathsFinal), 1)
                  WLR = round(float(wins) / float(losses), 1)
                  BBLR = round(float(brokenBeds) / float(lostBeds), 1)
                  KDR = round(float(Kills) / float(deaths), 1)
                  void_kdr = round(float(killsVoid) / float(deathsVoid), 1)

                  bwembed = discord.Embed(title='Bedwars Stats <:bw:850964476109914112>', description=f'Overall | {IGN}', color=0x2f3136)

                  bwembed.add_field(name='Stars', value=f'``{stars:,}✫``', inline=True)

                  bwembed.add_field(name='Winstreak', value=f'``{winstreak:,}``', inline=True)
                  
                  bwembed.add_field(name='BBLR', value=f'``{BBLR:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Kills', value=f'``{KillsFinal:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Deaths', value=f'``{DeathsFinal:,}``', inline=True)
                  
                  bwembed.add_field(name='FKDR', value=f'``{FKDR:,}``', inline=True)
                  
                  bwembed.add_field(name='Kills', value=f'``{Kills:,}``', inline=True)
                  
                  bwembed.add_field(name='Deaths', value=f'``{deaths:,}``', inline=True)

                  bwembed.add_field(name = 'KDR', value=f'``{KDR:,}``')

                  bwembed.add_field(name = 'Wins', value=f'``{wins:,}``')

                  bwembed.add_field(name = 'Losses', value=f'``{losses:,}``')

                  bwembed.add_field(name = 'WLR',  value = f'``{WLR:,}``')

                  bwembed.add_field(name = 'Void Kills', value=f'``{killsVoid:,}``')

                  bwembed.add_field(name = 'Void Deaths', value = f'``{deathsVoid:,}``')

                  bwembed.add_field(name = 'Void KDR', value = f'``{void_kdr:,}``')

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  bwembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                  await ctx.reply(embed=bwembed, mention_author=False)
                except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print("Error in bw overall command: " + str(e))

            elif mode == "fours":
                try:
                  bwdata = await hywrap.bedwars(mojang_data["id"], hypixelapikey)
                  profiledata = await hywrap.player(mojang_data["id"], hypixelapikey)
                  
                  Wins = (bwdata["four_four_wins_bedwars"])
                  Kills = (bwdata["four_four_kills_bedwars"])
                  Deaths = (bwdata["four_four_deaths_bedwars"])
                  voiddeaths = (bwdata["four_four_void_final_deaths_bedwars"])
                  voidkills = (bwdata["four_four_void_kills_bedwars"])
                  bedsbroken = bwdata["four_four_beds_broken_bedwars"]
                  bedslost = bwdata["four_four_beds_lost_bedwars"]
                  Losses = (bwdata["four_four_losses_bedwars"])
                  stars = (profiledata["player"]["achievements"]["bedwars_level"])
                  FinalDeaths = (bwdata["four_four_final_deaths_bedwars"])
                  FinalKills = (bwdata["four_four_final_kills_bedwars"])
                  winstreak = (bwdata["four_four_winstreak"])
                  FKDR = round(float(FinalKills) / float(FinalDeaths), 1)
                  WLR = round(float(Wins) / float(Losses), 1)
                  BBLR = round(float(bedsbroken) / float(bedslost), 1)
                  KDR = round(float(Kills) / float(Deaths), 1)
                  void_kdr = round(float(voidkills) / float(voiddeaths), 1)

                  bwembed = discord.Embed(title='Bedwars Stats <:bw:850964476109914112>', description=f'Fours | {IGN}', color=0x2f3136)

                  bwembed.add_field(name='Stars', value=f'``{stars:,}✫``', inline=True)

                  bwembed.add_field(name='Winstreak', value=f'``{winstreak:,}``', inline=True)
                  
                  bwembed.add_field(name='BBLR', value=f'``{BBLR:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Kills', value=f'``{FinalKills:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Deaths', value=f'``{FinalDeaths:,}``', inline=True)
                  
                  bwembed.add_field(name='FKDR', value=f'``{FKDR:,}``', inline=True)
                  
                  bwembed.add_field(name='Kills', value=f'``{Kills:,}``', inline=True)
                  
                  bwembed.add_field(name='Deaths', value=f'``{Deaths:,}``', inline=True)

                  bwembed.add_field(name = 'KDR', value=f'``{KDR:,}``')

                  bwembed.add_field(name = 'Wins', value=f'``{Wins:,}``')

                  bwembed.add_field(name = 'Losses', value=f'``{Losses:,}``')

                  bwembed.add_field(name = 'WLR',  value = f'``{WLR:,}``')

                  bwembed.add_field(name = 'Void Kills', value=f'``{voidkills:,}``')

                  bwembed.add_field(name = 'Void Deaths', value = f'``{voiddeaths:,}``')

                  bwembed.add_field(name = 'Void KDR', value = f'``{void_kdr:,}``')

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  bwembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                  await ctx.reply(embed=bwembed, mention_author=False)
                except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f'There was an error in command bw in fours: {e}')

            elif mode == 'doubles':
                try:
                  bwdata = await hywrap.bedwars(mojang_data["id"], hypixelapikey)
                  profiledata = await hywrap.player(mojang_data["id"], hypixelapikey)
                  
                  Wins = (bwdata["eight_two_wins_bedwars"])
                  Kills = (bwdata["eight_two_kills_bedwars"])
                  Deaths = (bwdata["eight_two_deaths_bedwars"])
                  voiddeaths = (bwdata["eight_two_void_final_deaths_bedwars"])
                  voidkills = (bwdata["eight_two_void_kills_bedwars"])
                  bedsbroken = bwdata["eight_two_beds_broken_bedwars"]
                  bedslost = bwdata["eight_two_beds_lost_bedwars"]
                  Losses = (bwdata["eight_two_losses_bedwars"])
                  stars = (profiledata["player"]["achievements"]["bedwars_level"])
                  FinalDeaths = (bwdata["eight_two_final_deaths_bedwars"])
                  FinalKills = (bwdata["eight_two_final_kills_bedwars"])
                  winstreak = (bwdata["eight_two_winstreak"])
                  FKDR = round(float(FinalKills) / float(FinalDeaths), 1)
                  WLR = round(float(Wins) / float(Losses), 1)
                  BBLR = round(float(bedsbroken) / float(bedslost), 1)
                  KDR = round(float(Kills) / float(Deaths), 1)
                  void_kdr = round(float(voidkills) / float(voiddeaths), 1)

                  bwembed = discord.Embed(title='Bedwars Stats <:bw:850964476109914112>', description=f'Doubles | {IGN}', color=0x2f3136)

                  bwembed.add_field(name='Stars', value=f'``{stars:,}✫``', inline=True)

                  bwembed.add_field(name='Winstreak', value=f'``{winstreak:,}``', inline=True)
                  
                  bwembed.add_field(name='BBLR', value=f'``{BBLR:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Kills', value=f'``{FinalKills:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Deaths', value=f'``{FinalDeaths:,}``', inline=True)
                  
                  bwembed.add_field(name='FKDR', value=f'``{FKDR:,}``', inline=True)
                  
                  bwembed.add_field(name='Kills', value=f'``{Kills:,}``', inline=True)
                  
                  bwembed.add_field(name='Deaths', value=f'``{Deaths:,}``', inline=True)

                  bwembed.add_field(name = 'KDR', value=f'``{KDR:,}``')

                  bwembed.add_field(name = 'Wins', value=f'``{Wins:,}``')

                  bwembed.add_field(name = 'Losses', value=f'``{Losses:,}``')

                  bwembed.add_field(name = 'WLR',  value = f'``{WLR:,}``')

                  bwembed.add_field(name = 'Void Kills', value=f'``{voidkills:,}``')

                  bwembed.add_field(name = 'Void Deaths', value = f'``{voiddeaths:,}``')

                  bwembed.add_field(name = 'Void KDR', value = f'``{void_kdr:,}``')

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  bwembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                  await ctx.reply(embed=bwembed, mention_author=False)
                except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f'There was an error in command bw in doubles: {e}')
              
            elif mode == 'solo':
                try:
                  bwdata = await hywrap.bedwars(mojang_data["id"], hypixelapikey)
                  profiledata = await hywrap.player(mojang_data["id"], hypixelapikey)
                  
                  Wins = (bwdata["eight_one_wins_bedwars"])
                  Kills = (bwdata["eight_one_kills_bedwars"])
                  Deaths = (bwdata["eight_one_deaths_bedwars"])
                  voiddeaths = (bwdata["eight_one_void_final_deaths_bedwars"])
                  voidkills = (bwdata["eight_one_void_kills_bedwars"])
                  bedsbroken = bwdata["eight_one_beds_broken_bedwars"]
                  bedslost = bwdata["eight_one_beds_lost_bedwars"]
                  Losses = (bwdata["eight_one_losses_bedwars"])
                  stars = (profiledata["player"]["achievements"]["bedwars_level"])
                  FinalDeaths = (bwdata["eight_one_final_deaths_bedwars"])
                  FinalKills = (bwdata["eight_one_final_kills_bedwars"])
                  winstreak = (bwdata["eight_one_winstreak"])
                  FKDR = round(float(FinalKills) / float(FinalDeaths), 1)
                  WLR = round(float(Wins) / float(Losses), 1)
                  BBLR = round(float(bedsbroken) / float(bedslost), 1)
                  KDR = round(float(Kills) / float(Deaths), 1)
                  void_kdr = round(float(voidkills) / float(voiddeaths), 1)

                  bwembed = discord.Embed(title='Bedwars Stats <:bw:850964476109914112>', description=f'Solo | {IGN}', color=0x2f3136)

                  bwembed.add_field(name='Stars', value=f'``{stars:,}✫``', inline=True)

                  bwembed.add_field(name='Winstreak', value=f'``{winstreak:,}``', inline=True)
                  
                  bwembed.add_field(name='BBLR', value=f'``{BBLR:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Kills', value=f'``{FinalKills:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Deaths', value=f'``{FinalDeaths:,}``', inline=True)
                  
                  bwembed.add_field(name='FKDR', value=f'``{FKDR:,}``', inline=True)
                  
                  bwembed.add_field(name='Kills', value=f'``{Kills:,}``', inline=True)
                  
                  bwembed.add_field(name='Deaths', value=f'``{Deaths:,}``', inline=True)

                  bwembed.add_field(name = 'KDR', value=f'``{KDR:,}``')

                  bwembed.add_field(name = 'Wins', value=f'``{Wins:,}``')

                  bwembed.add_field(name = 'Losses', value=f'``{Losses:,}``')

                  bwembed.add_field(name = 'WLR',  value = f'``{WLR:,}``')

                  bwembed.add_field(name = 'Void Kills', value=f'``{voidkills:,}``')

                  bwembed.add_field(name = 'Void Deaths', value = f'``{voiddeaths:,}``')

                  bwembed.add_field(name = 'Void KDR', value = f'``{void_kdr:,}``')

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  bwembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                  await ctx.reply(embed=bwembed, mention_author=False)
                except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f'There was an error in command bw in solos: {e}')
              
            elif mode == 'threes':
                try:
                  bwdata = await hywrap.bedwars(mojang_data["id"], hypixelapikey)
                  profiledata = await hywrap.player(mojang_data["id"], hypixelapikey)
                  
                  Wins = (bwdata["four_three_wins_bedwars"])
                  Kills = (bwdata["four_three_kills_bedwars"])
                  Deaths = (bwdata["four_three_deaths_bedwars"])
                  voiddeaths = (bwdata["four_three_void_final_deaths_bedwars"])
                  voidkills = (bwdata["four_three_void_kills_bedwars"])
                  bedsbroken = bwdata["four_three_beds_broken_bedwars"]
                  bedslost = bwdata["four_three_beds_lost_bedwars"]
                  Losses = (bwdata["four_three_losses_bedwars"])
                  stars = (profiledata["player"]["achievements"]["bedwars_level"])
                  FinalDeaths = (bwdata["four_three_final_deaths_bedwars"])
                  FinalKills = (bwdata["four_three_final_kills_bedwars"])
                  winstreak = (bwdata["four_three_winstreak"])
                  FKDR = round(float(FinalKills) / float(FinalDeaths), 1)
                  WLR = round(float(Wins) / float(Losses), 1)
                  BBLR = round(float(bedsbroken) / float(bedslost), 1)
                  KDR = round(float(Kills) / float(Deaths), 1)
                  void_kdr = round(float(voidkills) / float(voiddeaths), 1)

                  bwembed = discord.Embed(title='Bedwars Stats <:bw:850964476109914112>', description=f'Threes | {IGN}', color=0x2f3136)

                  bwembed.add_field(name='Stars', value=f'``{stars:,}✫``', inline=True)

                  bwembed.add_field(name='Winstreak', value=f'``{winstreak:,}``', inline=True)
                  
                  bwembed.add_field(name='BBLR', value=f'``{BBLR:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Kills', value=f'``{FinalKills:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Deaths', value=f'``{FinalDeaths:,}``', inline=True)
                  
                  bwembed.add_field(name='FKDR', value=f'``{FKDR:,}``', inline=True)
                  
                  bwembed.add_field(name='Kills', value=f'``{Kills:,}``', inline=True)
                  
                  bwembed.add_field(name='Deaths', value=f'``{Deaths:,}``', inline=True)

                  bwembed.add_field(name = 'KDR', value=f'``{KDR:,}``')

                  bwembed.add_field(name = 'Wins', value=f'``{Wins:,}``')

                  bwembed.add_field(name = 'Losses', value=f'``{Losses:,}``')

                  bwembed.add_field(name = 'WLR',  value = f'``{WLR:,}``')

                  bwembed.add_field(name = 'Void Kills', value=f'``{voidkills:,}``')

                  bwembed.add_field(name = 'Void Deaths', value = f'``{voiddeaths:,}``')

                  bwembed.add_field(name = 'Void KDR', value = f'``{void_kdr:,}``')

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  bwembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                  await ctx.reply(embed=bwembed, mention_author=False)
                except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f'There was an error in command bw in threes: {e}')
            else:
              errorembed = discord.Embed(title = 'Invalid Command Usage!')
              errorembed.add_field(name = 'Usage:', value = "``.bw {IGN} {mode}``", inline = False)
              errorembed.set_footer(text = 'Valid Modes: Overall, Solo, Doubles, Threes, Fours')
              errorembed.add_field(name = 'Aliases:', value = '``bw, bed, bedwarz, bedwars, bedworz, bedwar``', inline = False)
              errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
              await ctx.send(embed = errorembed)

    
    @commands.command(aliases = ["skywars", "skywar", "skywor", "skiwar", "skiwor"])
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def sw(self, ctx, user : str = None, *, gamemode : str = 'overall'):
        print("The SW Command was executed!")
        start = datetime.utcnow()
        mode = gamemode.lower()
        if user is None:
            errorembed = discord.Embed(title = 'Skywars')
            errorembed.add_field(name = 'Usage:', value = "``.sw {IGN} {mode}``", inline = False)
            errorembed.add_field(name = '❔', value = 'Returns the SkyWars stats of a specified player.', inline = False)
            errorembed.add_field(name = 'Aliases:', value = '``sw, skywars, skywar, skywor, skiwar, skiwor``')
            errorembed.set_footer(text = 'Valid Modes: Solo Insane, Solo Normal, Teams Insane, Teams Normal and Ranked.')
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                  async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                    mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`")
        
        IGN = str(mojang_data['name'])

        if mode == 'overall':
            try:
                swdata = await hywrap.skywars(mojang_data["id"], hypixelapikey)

                async with aiohttp.ClientSession() as cs:
                  async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                    swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["wins"])
                Heads = (swdata["heads"])
                SwKills = (swdata["kills"])
                SwDeaths = (swdata["deaths"])
                SwLosses = (swdata["losses"])
                SwCoins = (swdata["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(title='Skywars Stats <:sw:850964475544731689>', description=f'Overall | {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}✫``", inline = True)

                swembed.add_field(name='Coins', value=f'``{SwCoins:,}``', inline = True)

                swembed.add_field(name='Heads', value=f'``{Heads:,}``', inline = True)

                swembed.add_field(name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(name='KDR', value=f'``{SwKDR:,}``', inline = True)
                
                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                swembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                await ctx.reply(embed=swembed, mention_author=False)
            except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'\n{IGN} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f"Error in Skywars Command in Overall: {e}")

        elif mode == 'solo insane':
            try:
                swdata = await hywrap.skywars(mojang_data["id"], hypixelapikey)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                          swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["wins_solo_insane"])
                Heads = (swdata["heads"])
                SwKills = (swdata["kills_solo_insane"])
                SwDeaths = (swdata["deaths_solo_insane"])
                SwLosses = (swdata["losses_solo_insane"])
                SwCoins = (swdata["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(title='Skywars Stats <:sw:850964475544731689>', description=f'Solo Insane | {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}✫``", inline = True)

                swembed.add_field(name='Coins', value=f'``{SwCoins:,}``', inline = True)

                swembed.add_field(name='Heads', value=f'``{Heads:,}``', inline = True)

                swembed.add_field(name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(name='KDR', value=f'``{SwKDR:,}``', inline = True)

                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                swembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                await ctx.reply(embed=swembed, mention_author=False)
            except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'\n{IGN} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f"Error in Skywars Command in Solo Insane: {e}")

        elif mode == 'solo normal':
            try:
                swdata = await hywrap.skywars(mojang_data["id"], hypixelapikey)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                          swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["wins_solo_normal"])
                Heads = (swdata["heads"])
                SwKills = (swdata["kills_solo_normal"])
                SwDeaths = (swdata["deaths_solo_normal"])
                SwLosses = (swdata["losses_solo_normal"])
                SwCoins = (swdata["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(title='Skywars Stats <:sw:850964475544731689>', description=f'Solo Normal | {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}✫``", inline = True)

                swembed.add_field(name='Coins', value=f'``{SwCoins:,}``', inline = True)

                swembed.add_field(name='Heads', value=f'``{Heads:,}``', inline = True)

                swembed.add_field(name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(name='KDR', value=f'``{SwKDR:,}``', inline = True)

                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                swembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                await ctx.reply(embed=swembed, mention_author=False)
            except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'\n{IGN} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f"Error in Skywars Command in Solo Normal: {e}")

        elif mode == 'teams normal':
            try:
                swdata = await hywrap.skywars(mojang_data["id"], hypixelapikey)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                          swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["wins_team_normal"])
                Heads = (swdata["heads"])
                SwKills = (swdata["kills_team_normal"])
                SwDeaths = (swdata["deaths_team_normal"])
                SwLosses = (swdata["losses_team_normal"])
                SwCoins = (swdata["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(title='Skywars Stats <:sw:850964475544731689>', description=f'Teams Normal | {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}✫``", inline = True)

                swembed.add_field(name='Coins', value=f'``{SwCoins:,}``', inline = True)

                swembed.add_field(name='Heads', value=f'``{Heads:,}``', inline = True)

                swembed.add_field(name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(name='KDR', value=f'``{SwKDR:,}``', inline = True)

                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                swembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                await ctx.reply(embed=swembed, mention_author=False)
            except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'\n{IGN} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f"Error in Skywars Command in Teams Normal: {e}")

        elif mode == 'teams insane':
            try:
                swdata = await hywrap.skywars(mojang_data["id"], hypixelapikey)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                          swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["wins_team_insane"])
                Heads = (swdata["heads"])
                SwKills = (swdata["kills_team_insane"])
                SwDeaths = (swdata["deaths_team_insane"])
                SwLosses = (swdata["losses_team_insane"])
                SwCoins = (swdata["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(title='Skywars Stats <:sw:850964475544731689>', description=f'Teams Insane | {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}✫``", inline = True)

                swembed.add_field(name='Coins', value=f'``{SwCoins:,}``', inline = True)

                swembed.add_field(name='Heads', value=f'``{Heads:,}``', inline = True)

                swembed.add_field(name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(name='KDR', value=f'``{SwKDR:,}``', inline = True)

                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                swembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                await ctx.reply(embed=swembed, mention_author=False)
            except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'\n{IGN} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f"Error in Skywars Command in Teams Insane: {e}")

        elif mode == 'ranked':
            try:
                swdata = await hywrap.skywars(mojang_data["id"], hypixelapikey)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                          swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["wins_ranked"])
                Heads = (swdata["heads"])
                SwKills = (swdata["kills_ranked"])
                SwDeaths = (swdata["deaths_ranked"])
                SwLosses = (swdata["losses_ranked"])
                SwCoins = (swdata["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(title='Skywars Stats <:sw:850964475544731689>', description=f'Ranked | {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}✫``", inline = True)

                swembed.add_field(name='Coins', value=f'``{SwCoins:,}``', inline = True)

                swembed.add_field(name='Heads', value=f'``{Heads:,}``', inline = True)

                swembed.add_field(name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(name='KDR', value=f'``{SwKDR:,}``', inline = True)

                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                swembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

                await ctx.reply(embed=swembed, mention_author=False)
            except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'\n{IGN} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(f"Error in Skywars Command in Ranked: {e}")
                    
        else:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.sw {IGN} {mode}``", inline = False)
            errorembed.add_field(name = 'Aliases:', value = '``sw, skywars, skywar, skywor, skiwar, skiwor``')
            errorembed.set_footer(text = 'Valid Modes: Solo Insane, Solo Normal, Teams Insane, Teams Normal and Ranked.')
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)

    @commands.command(aliases = ["duels", "d"])
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def duel(self, ctx, user : str = None, *, gamemode : str = 'overall'):
        print("The Duels Command was executed!")
        start = datetime.utcnow()
        mode = gamemode.lower()
        if user is None:
            errorembed = discord.Embed(title = 'Duels')
            errorembed.add_field(name = 'Usage:', value = "``.d {IGN}``")
            errorembed.add_field(name = '❔', value = 'Returns the Duels Stats of a specified player.', inline = False)
            errorembed.add_field(name = 'Aliases', value = '``d, duels, duel``', inline = False)
            errorembed.set_footer(text = 'Valid Modes: Bridge, Classic, UHC, Combo, SkyWars, Sumo, NoDebuff, Bow Duels, OP Duels')
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                  async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                    mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`")

            IGN = str(mojang_data["name"])

            if mode == 'overall':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  ws = duels["current_winstreak"]
                  coins = duels["coins"]
                  bow_shots = duels["bow_shots"]
                  wins = duels["wins"]
                  losses = duels["losses"]
                  kills = duels["kills"]
                  deaths = duels["deaths"]
                  melee_swings = duels["melee_swings"]
                  melee_hits = duels["melee_hits"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)
                  accuracy = round(float(melee_hits) / float(melee_swings), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Overall | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)

                  duelsembed.add_field(name = f'Bow Shots', value = f'``{bow_shots:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  duelsembed.add_field(name = f'Melee Swings', value = f'``{melee_swings:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Melee Hits', value = f'``{melee_hits:,}``', inline=True)

                  duelsembed.add_field(name = f'Accuracy', value = f'``{accuracy:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'{IGN} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Overall: {e}")

            elif mode == 'bridge':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  ws = duels["current_bridge_winstreak"]
                  coins = duels["coins"]
                  wins = duels["bridge_duel_wins"]
                  losses = duels["bridge_duel_losses"]
                  kills = duels["bridge_kills"]
                  goals = duels["bridge_duel_goals"]
                  deaths = duels["bridge_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Bridge Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Goals", value = f'``{goals:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'{IGN} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Bridge: {e}")

            elif mode == 'classic':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  ws = duels["current_classic_winstreak"]
                  coins = duels["coins"]
                  wins = duels["classic_duel_wins"]
                  losses = duels["classic_duel_losses"]
                  kills = duels["classic_duel_kills"]
                  games = duels["classic_duel_rounds_played"]
                  deaths = duels["classic_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Classic Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'{IGN} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Classic: {e}")

            elif mode == 'uhc':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  
                  ws = duels["current_uhc_winstreak"]
                  coins = duels["coins"]
                  wins = duels["uhc_duel_wins"]
                  losses = duels["uhc_duel_losses"]
                  kills = duels["uhc_duel_kills"]
                  games = duels["uhc_duel_rounds_played"]
                  deaths = duels["uhc_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'UHC Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'{IGN} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in UHC: {e}")

            elif mode == 'combo':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  
                  ws = duels["current_combo_winstreak"]
                  coins = duels["coins"]
                  wins = duels["combo_duel_wins"]
                  losses = duels["combo_duel_losses"]
                  kills = duels["combo_duel_kills"]
                  games = duels["combo_duel_rounds_played"]
                  deaths = duels["combo_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Combo Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Combo: {e}")

            elif mode == 'skywars':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  
                  ws = duels["current_skywars_winstreak"]
                  coins = duels["coins"]
                  wins = duels["sw_duel_wins"]
                  losses = duels["sw_duel_losses"]
                  kills = duels["sw_duel_kills"]
                  games = duels["sw_duel_rounds_played"]
                  deaths = duels["sw_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Skywars Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Skywars: {e}")
            
            elif mode == 'sumo':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  ws = duels["current_winstreak_mode_sumo_duel"]
                  coins = duels["coins"]
                  wins = duels["sumo_duel_wins"]
                  losses = duels["sumo_duel_losses"]
                  kills = duels["sumo_duel_kills"]
                  games = duels["sumo_duel_rounds_played"]
                  deaths = duels["sumo_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Sumo Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Sumo: {e}")

            elif mode == 'nodebuff':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  
                  ws = duels["current_no_debuff_winstreak"]
                  coins = duels["coins"]
                  wins = duels["potion_duel_wins"]
                  losses = duels["potion_duel_losses"]
                  kills = duels["potion_duel_kills"]
                  games = duels["potion_duel_rounds_played"]
                  deaths = duels["potion_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Potion Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Nodebuff: {e}")

            elif mode == 'bow duels':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  
                  ws = duels["current_winstreak_mode_bow_duel"]
                  coins = duels["coins"]
                  wins = duels["bow_duel_wins"]
                  losses = duels["bow_duel_losses"]
                  kills = duels["bow_duel_kills"]
                  games = duels["bow_duel_rounds_played"]
                  deaths = duels["bow_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'Bow Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Bow Duels: {e}")

            elif mode == 'op duels':
              try:
                  duels = await hywrap.duels(mojang_data["id"], hypixelapikey)
                  
                  
                  ws = duels["current_winstreak_mode_op_duel"]
                  coins = duels["coins"]
                  wins = duels["op_duel_wins"]
                  losses = duels["op_duel_losses"]
                  kills = duels["op_duel_kills"]
                  games = duels["op_duel_rounds_played"]
                  deaths = duels["op_duel_deaths"]
                  kdr = round(float(kills) / float(deaths), 1)
                  wlr = round(float(wins) / float(losses), 1)


                  duelsembed = discord.Embed(title = f'Duels Stats <:duels:850964475937816586>', description = f'OP Duels | {mojang_data["name"]}', color = 0x2f3136)
                  
                  duelsembed.add_field(name = f'Winstreak', value = f'``{ws:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Coins", value = f'``{coins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f"Games Played", value = f'``{games:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Wins', value = f'``{wins:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Losses', value = f'``{losses:,}``', inline=True)

                  duelsembed.add_field(name = f'WLR', value = f'``{wlr:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Kills', value = f'``{kills:,}``', inline=True)
                  
                  duelsembed.add_field(name = f'Deaths', value = f'``{deaths:,}``', inline=True)

                  duelsembed.add_field(name = f'KDR', value = f'``{kdr:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, secS = divmod(remainder, 60)
                  seconds = round(secS, 1)

                  duelsembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
                print(f"Error in Duels Command in Overall: {e}")

            else:
              errorembed = discord.Embed(title = 'Invalid Command Usage!')
              errorembed.add_field(name = 'Usage:', value = "``.d {IGN}``")
              errorembed.add_field(name = 'Aliases', value = '``d, duels, duel``', inline = False)
              errorembed.set_footer(text = 'Valid Modes: Bridge, Classic, UHC, Combo, SkyWars, Sumo, NoDebuff, Bow Duels, OP Duels')
              errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
              await ctx.send(embed = errorembed)
              
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def compare(self, ctx, player1 : str = None, player2 : str = None):
      print("The Compare Command was executed!")
      if player1 is None:
        errorembed = discord.Embed(title = 'Compare')
        errorembed.add_field(name = 'Usage:', value = "``.compare {Player 1} {Player 2}``")
        errorembed.add_field(name = '❔', value = 'Compares two players\' BedWars stats.', inline = False)
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
        return
      if player2 is None:
        errorembed = discord.Embed(title = 'Compare')
        errorembed.add_field(name = 'Usage:', value = "``.compare {Player 1} {Player 2}``")
        errorembed.add_field(name = '❔', value = 'Compares two players\' BedWars stats.', inline = False)
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
        return

      try:
        async with aiohttp.ClientSession() as cs:
              async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{player1}') as mojang1:
                mojangplayer1 = await mojang1.json()

        async with aiohttp.ClientSession() as cs:
          async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojangplayer1['id']}") as apiraw:
            player1api = await apiraw.json()
      
      except:
        errorembed = discord.Embed()
        errorembed.add_field(name = 'Error!', value = "Invalid Player 1 username")
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      
      try:
        async with aiohttp.ClientSession() as cs:
              async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{player2}') as mojang2:
                mojangplayer2 = await mojang2.json()

        async with aiohttp.ClientSession() as cs:
          async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojangplayer2['id']}") as apiraw:
            player2api = await apiraw.json()

        async with aiohttp.ClientSession() as cs:
          async with cs.get(f'https://i.imgur.com/jA86X4R.png') as crownraw:
            crown_read = await crownraw.read()
            crown_image_bytesio = io.BytesIO(crown_read)
      
      except:
        errorembed = discord.Embed()
        errorembed.add_field(name = 'Error!', value = "Invalid Player 2 username")
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      
      async with ctx.typing():
        
        oWins = (player1api["player"]["stats"]["Bedwars"]["wins_bedwars"])
        oLosses = (player1api["player"]["stats"]["Bedwars"]["losses_bedwars"])
        ostars = int(player1api["player"]["achievements"]["bedwars_level"])
        oFinalDeaths = (player1api["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
        oFinalKills = (player1api["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
        oFKDR = round(float(oFinalKills) / float(oFinalDeaths), 1)
        oWLR = round(float(oWins) / float(oLosses), 1)
        oIndex = round(ostars * oFKDR * oFKDR / 10)

        tWins = (player2api["player"]["stats"]["Bedwars"]["wins_bedwars"])
        tLosses = (player2api["player"]["stats"]["Bedwars"]["losses_bedwars"])
        tstars = int(player2api["player"]["achievements"]["bedwars_level"])
        tFinalDeaths = (player2api["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
        tFinalKills = (player2api["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
        tFKDR = round(float(tFinalKills) / float(tFinalDeaths), 1)
        tWLR = round(float(tWins) / float(tLosses), 1)
        tIndex = round(tstars * tFKDR * tFKDR / 10)

        player1points = 0
        player2points = 0

        player1ign = mojangplayer1["name"]
        player2ign = mojangplayer2["name"]
        img = Image.open("overall.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Minecraftia.ttf",
                                  40)
        fontbig = ImageFont.truetype("Minecraftia.ttf",
                                      50)
                                      
        draw.text((200, 200), f"{player1ign}", self.white, font=fontbig)
        draw.text((1200, 200), f"{player2ign}", self.white, font=fontbig)
        
        if oFinalKills > tFinalKills:
          draw.text((200, 400), f"Final Kills: {oFinalKills:,}", self.green, font=font)
          draw.text((1200, 400), f"Final Kills: {tFinalKills:,}", self.light_red, font=font)
          player1points += 1

        elif oFinalKills < tFinalKills:
          draw.text((200, 400), f"Final Kills: {oFinalKills:,}", self.light_red, font=font)
          draw.text((1200, 400), f"Final Kills: {tFinalKills:,}", self.green, font=font)
          player2points += 1

        else:
          draw.text((200, 400), f"Final Kills: {oFinalKills:,}", self.white, font=font)
          draw.text((1200, 400), f"Final Kills: {tFinalKills:,}", self.white, font=font)

        if oFinalDeaths > tFinalDeaths:
          draw.text((200, 470), f"Final Deaths: {oFinalDeaths:,}", self.light_red, font=font)
          draw.text((1200, 470), f"Final Deaths: {tFinalDeaths:,}", self.green, font=font)
          player2points += 1 # Yes this is intentional

        elif oFinalDeaths < tFinalDeaths:
          draw.text((200, 470), f"Final Deaths: {oFinalDeaths:,}", self.green, font=font)
          draw.text((1200, 470), f"Final Deaths: {tFinalDeaths:,}", self.light_red, font=font)
          player1points += 1 # Yes this is intentional

        else:
          draw.text((200, 470), f"Final Deaths: {oFinalDeaths:,}", self.white, font=font)
          draw.text((1200, 470), f"Final Deaths: {tFinalDeaths:,}", self.white, font=font)
        
        if oFKDR > tFKDR:
          draw.text((200, 540), f"FKDR: {oFKDR:,}", self.green, font=font)
          draw.text((1200, 540), f"FKDR: {tFKDR:,}", self.light_red, font=font)
          player1points += 1

        elif oFKDR < tFKDR:
          draw.text((200, 540), f"FKDR: {oFKDR:,}", self.light_red, font=font)
          draw.text((1200, 540), f"FKDR: {tFKDR:,}", self.green, font=font)
          player2points += 1

        else:
          draw.text((200, 540), f"FKDR: {oFKDR:,}", self.white, font=font)
          draw.text((1200, 540), f"FKDR: {tFKDR:,}", self.white, font=font)

        if oWins > tWins:
          draw.text((200, 610), f"Wins: {oWins:,}", self.green, font=font)
          draw.text((1200, 610), f"Wins: {tWins:,}", self.light_red, font=font)
          player1points += 1

        elif oWins < tWins:
          draw.text((200, 610), f"Wins: {oWins:,}", self.light_red, font=font)
          draw.text((1200, 610), f"Wins: {tWins:,}", self.green, font=font)
          player2points += 1

        else:
          draw.text((200, 610), f"Wins: {oWins:,}", self.white, font=font)
          draw.text((1200, 610), f"Wins: {tWins:,}", self.white, font=font)

        if oLosses > tLosses:
          draw.text((200, 680), f"Losses: {oLosses:,}", self.light_red, font=font)
          draw.text((1200, 680), f"Losses: {tLosses:,}", self.green, font=font)
          player2points += 1

        elif oLosses < tLosses:
          draw.text((200, 680), f"Losses: {oLosses:,}", self.green, font=font)
          draw.text((1200, 680), f"Losses: {tLosses:,}", self.light_red, font=font)
          player1points += 1

        else:
          draw.text((200, 680), f"Losses: {oLosses:,}", self.white, font=font)
          draw.text((1200, 680), f"Losses: {tLosses:,}", self.white, font=font)

        if oWLR > tWLR:
          draw.text((200, 750), f"WLR: {oWLR:,}", self.green, font=font)
          draw.text((1200, 750), f"WLR: {tWLR:,}", self.light_red, font=font)
          player1points += 1

        elif oWLR < tWLR:
          draw.text((200, 750), f"WLR: {oWLR:,}", self.light_red, font=font)
          draw.text((1200, 750), f"WLR: {tWLR:,}", self.green, font=font)
          player2points += 1

        else:
          draw.text((200, 750), f"WLR: {oWLR:,}", self.white, font=font)
          draw.text((1200, 750), f"WLR: {tWLR:,}", self.white, font=font)

        if oIndex > tIndex:
          draw.text((200, 820), f"Treat Index: {oIndex:,}", self.green, font=font)
          draw.text((1200, 820), f"Threat Index: {tIndex:,}", self.light_red, font=font)
          player1points += 1
        
        elif oIndex < tIndex:
          draw.text((200, 820), f"Threat Index: {oIndex:,}", self.light_red, font=font)
          draw.text((1200, 820), f"Threat Index: {tIndex:,}", self.green, font=font)
          player2points += 1

        else:
          draw.text((200, 820), f"Threat Index: {oIndex:,}", self.white, font=font)
          draw.text((1200, 820), f"Threat Index: {tIndex:,}", self.white, font=font)

        if ostars > tstars:
          draw.text((200, 330), f"Stars: {ostars:,}", self.green, font=font)
          draw.text((1200, 330), f"Stars: {tstars:,}", self.light_red, font=font)
          player1points += 1
        
        elif ostars > tstars:
          draw.text((200, 330), f"Stars: {ostars:,}", self.light_red, font=font)
          draw.text((1200, 330), f"Stars: {tstars:,}", self.green, font=font)
          player2points += 1
        
        else:
          draw.text((200, 330), f"Stars: {ostars:,}", self.white, font=font)
          draw.text((1200, 330), f"Stars: {tstars:,}", self.white, font=font)

        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.reply(file=discord.File(fp=image_binary, filename='image.png'), mention_author = False)

    @commands.command()
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def p(self, ctx, mode : str = None, player : str = None):
        print("The P Command was executed!")
        gamemode = mode.lower()
        if player is None:
            errorembed = discord.Embed(title = 'Pictured Stats')
            errorembed.add_field(name = 'Usage:', value = "``.p {gamemode} {IGN}``")
            errorembed.add_field(name = '❔', value = 'Returns the SkyWars / BedWars / Duels stats of a specified player in picture format.', inline = False)
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            errorembed.set_footer(text = 'Gamemode can be bedwars, skywars or duels')
            await ctx.send(embed = errorembed)
        elif gamemode is None:
            errorembed = discord.Embed(title = 'Pictured Stats')
            errorembed.add_field(name = 'Usage:', value = "``.p {gamemode} {IGN}``")
            errorembed.add_field(name = '❔', value = 'Returns the SkyWars / BedWars / Duels stats of a specified player in picture format.', inline = False)
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{player}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{player}`")
            else:
              async with ctx.typing():

                api = await hywrap.player(mojang_data["id"], hypixelapikey)

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f"https://api.slothpixel.me/api/players/{player}") as profiledataraw:
                        profiledata = await profiledataraw.json()
                        rank = profiledata["rank"]

                async with aiohttp.ClientSession() as cs:
                  async with cs.get(f'https://mc-heads.net/body/{mojang_data["id"]}/right') as skin:
                    skin_read = await skin.read()
                    image_bytesio = io.BytesIO(skin_read)
                
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f"https://api.slothpixel.me/api/players/{player}") as swlvldataraw:
                        swlvldata = await swlvldataraw.json()

                if rank == "MVP_PLUS_PLUS":
                  rank = "[MVP++]"
                elif rank == "MVP_PLUS":
                  rank = "[MVP+]"
                elif rank == "VIP_PLUS":
                  rank = "[VIP+]"
                elif rank == None:
                  rank = "[Non]"
                elif rank == "YOUTUBER":
                  rank = "[YOUTUBE]"
                elif rank == "MODERATOR":
                  rank = "[MOD]"
                else:
                  rank = f'[{profiledata["rank"]}]'

                IGN = mojang_data["name"]
                
                if gamemode == "bedwars":
                  try:
                    img = Image.open("bw.png")
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("Minecraftia.ttf",
                                              40)
                    fontbig = ImageFont.truetype("Minecraftia.ttf",
                                                50)

                    Wins = (api["player"]["stats"]["Bedwars"]["wins_bedwars"])
                    Kills = (api["player"]["stats"]["Bedwars"]["kills_bedwars"])
                    Deaths = (api["player"]["stats"]["Bedwars"]["deaths_bedwars"])
                    coins = (api["player"]["stats"]["Bedwars"]["coins"])
                    voiddeaths = (api["player"]["stats"]["Bedwars"]["void_deaths_bedwars"])
                    voidkills = (api["player"]["stats"]["Bedwars"]["void_kills_bedwars"])
                    games = (api["player"]["stats"]["Bedwars"]["games_played_bedwars"])
                    bedsbroken = api["player"]["stats"]["Bedwars"]["beds_broken_bedwars"]
                    bedslost = api["player"]["stats"]["Bedwars"]["beds_lost_bedwars"]
                    Losses = (api["player"]["stats"]["Bedwars"]["losses_bedwars"])
                    Levels = (api["player"]["achievements"]["bedwars_level"])
                    FinalDeaths = (api["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
                    FinalKills = (api["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
                    winstreak = (api["player"]["stats"]["Bedwars"]["winstreak"])
                    coins = (api["player"]["stats"]["Bedwars"]["coins"])
                    FKDR = round(float(FinalKills) / float(FinalDeaths), 1)
                    WLR = round(float(Wins) / float(Losses), 1)
                    BBLR = round(float(bedsbroken) / float(bedslost), 1)
                    KDR = round(float(Kills) / float(Deaths), 1)
                    void_kdr = KDR = round(float(voidkills) / float(voiddeaths), 1)

                    if rank == "VIP+":
                      draw.text((200, 150), f"VIP+ {IGN}", self.green, font=fontbig)
                    elif rank == "VIP":
                      draw.text((200, 150), f"VIP {IGN}", self.green, font=fontbig) 
                    elif rank == "MVP":
                      draw.text((200, 150), f"MVP {IGN}", self.aqua, font=fontbig)
                    elif rank == "MVP+":
                      draw.text((200, 150), f"MVP+ {IGN}", self.aqua, font=fontbig)
                    elif rank == "MVP++":
                      draw.text((200, 150), f"MVP++ {IGN}", self.gold, font=fontbig)
                    elif rank == "YOUTUBE":
                      draw.text((200, 150), f"YOUTUBE {IGN}", self.light_red, font=fontbig)
                    elif rank == "ADMIN":
                      draw.text((200, 150), f"ADMIN {IGN}", self.red, font=fontbig)
                    elif rank == "MOD":
                      draw.text((200, 150), f"MOD {IGN}", self.dark_green, font=fontbig)
                    else:
                      draw.text((200, 150), f"{rank} {IGN}", self.orangey, font=fontbig)

                    draw.text((750, 270), f"Stars: {Levels:,}", self.white, font=font)
                    draw.text((200, 270), f"Winstreak: {winstreak:,}", self.white, font=font)

                    draw.text((200, 400), f"Final Kills: {FinalKills:,}", self.white, font=font)
                    draw.text((200, 470), f"Final Deaths: {FinalDeaths:,}", self.white, font=font)
                    draw.text((200, 540), f"FKDR: {FKDR:,}", self.white, font=font)
                    
                    draw.text((750, 400), f"Wins: {Wins:,}", self.white, font=font)
                    draw.text((750, 470), f"Losses: {Losses:,}", self.white, font=font)
                    draw.text((750, 540), f"WLR: {WLR:,}", self.white, font=font)

                    draw.text((200, 800), f"Coins: {coins:,}", self.white, font=font)
                    draw.text((750, 800), f"BBLR: {BBLR:,}", self.white, font=font)

                    draw.text((1200, 400), f"Void Kills: {voidkills:,}", self.white, font=font)
                    draw.text((1200, 470), f"Void Deaths: {voiddeaths:,}", self.white, font=font)
                    draw.text((1200, 540), f"Void KDR: {void_kdr:,}", self.white, font=font)

                    draw.text((1200, 800), f"KDR: {KDR:,}", self.white, font=font)
                    draw.text((1200, 270), f"Games Played: {games:,}", self.white, font=font)

                    with io.BytesIO() as image_binary:
                        img.save(image_binary, 'PNG')
                        image_binary.seek(0)
                        await ctx.reply(file=discord.File(fp=image_binary, filename='image.png'), mention_author = False)

                  except Exception as e:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                    print(e)
                
                elif gamemode == "skywars":
                  try:
                    img = Image.open("sw.png")
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("Minecraftia.ttf",
                                              40)
                    fontbig = ImageFont.truetype("Minecraftia.ttf",
                                                50)
                    
                    SwWins = (api["player"]["stats"]["SkyWars"]["wins"])
                    Heads = (api["player"]["stats"]["SkyWars"]["heads"])
                    SwKills = (api["player"]["stats"]["SkyWars"]["kills"])
                    SwDeaths = (api["player"]["stats"]["SkyWars"]["deaths"])
                    lastmode = (api["player"]["stats"]["SkyWars"]["lastMode"])
                    SwLosses = (api["player"]["stats"]["SkyWars"]["losses"])
                    SwCoins = (api["player"]["stats"]["SkyWars"]["coins"])
                    SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                    SwWLR = round(float(SwWins) / float(SwLosses), 1)
                    SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                    if rank == "VIP+":
                      draw.text((200, 150), f"VIP+ {IGN}", self.green, font=fontbig)
                    elif rank == "VIP":
                      draw.text((200, 150), f"VIP {IGN}", self.green, font=fontbig)
                    elif rank == "MVP":
                      draw.text((200, 150), f"MVP {IGN}", self.aqua, font=fontbig)
                    elif rank == "MVP+":
                      draw.text((200, 150), f"MVP+ {IGN}", self.aqua, font=fontbig)
                    elif rank == "MVP++":
                      draw.text((200, 150), f"MVP++ {IGN}", self.gold, font=fontbig)
                    elif rank == "YOUTUBE":
                      draw.text((200, 150), f"YOUTUBE {IGN}", self.light_red, font=fontbig)
                    elif rank == "ADMIN":
                      draw.text((200, 150), f"ADMIN {IGN}", self.red, font=fontbig)
                    elif rank == "MOD":
                      draw.text((200, 150), f"MOD {IGN}", self.dark_green, font=fontbig)
                    else:
                      draw.text((200, 150), f"{rank} {IGN}", self.orangey, font=fontbig)

                    draw.text((800, 270), f"Stars: {SwLvl:,}", self.white, font=font)
                    draw.text((200, 270), f"Heads: {Heads:,}", self.white, font=font)

                    draw.text((200, 400), f"Kills: {SwKills:,}", self.white, font=font)
                    draw.text((200, 470), f"Deaths: {SwDeaths:,}", self.white, font=font)
                    draw.text((200, 540), f"KDR: {SwKDR:,}", self.white, font=font)
                    
                    draw.text((800, 400), f"Wins: {SwWins:,}", self.white, font=font)
                    draw.text((800, 470), f"Losses {SwLosses:,}", self.white, font=font)
                    draw.text((800, 540), f"WLR {SwWLR:,}", self.white, font=font)

                    draw.text((200, 800), f"Coins: {SwCoins:,}", self.white, font=font)
                    draw.text((800, 800), f"Last Mode: {lastmode}", self.white, font=font)

                    skin_img = Image.open(image_bytesio)
                    skin_img.thumbnail((500, 500))
                    img.paste(skin_img, (1400, 300), mask = skin_img)

                    with io.BytesIO() as image_binary:
                      img.save(image_binary, 'PNG')
                      image_binary.seek(0)
                      await ctx.reply(file = discord.File(fp = image_binary, filename='image.png'), mention_author = False)
                  
                  except:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)

                elif gamemode == "duels":
                  try:
                    img = Image.open("duels.png")
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("Minecraftia.ttf",
                                              40)
                    fontbig = ImageFont.truetype("Minecraftia.ttf",
                                                50)
                    
                    duels = api["player"]["stats"]["Duels"]

                    ws = (duels["current_winstreak"])
                    best_ws = (duels["best_overall_winstreak"])
                    hits = (duels["melee_hits"])
                    swings = (duels["melee_swings"])
                    accuracy = round(float(hits) / float(swings), 1)
                    wins = (duels["wins"])
                    losses = (duels["losses"])
                    WLR = round(float(wins) / float(losses), 1)
                    coins = (duels["coins"])
                    games = (duels["games_played_duels"])

                    if rank == "VIP+":
                      draw.text((200, 150), f"VIP+ {IGN}", self.green, font=fontbig)
                    elif rank == "VIP":
                      draw.text((200, 150), f"VIP {IGN}", self.green, font=fontbig)
                    elif rank == "MVP":
                      draw.text((200, 150), f"MVP {IGN}", self.aqua, font=fontbig)
                    elif rank == "MVP+":
                      draw.text((200, 150), f"MVP+ {IGN}", self.aqua, font=fontbig)
                    elif rank == "MVP++":
                      draw.text((200, 150), f"MVP++ {IGN}", self.gold, font=fontbig)
                    elif rank == "YOUTUBE":
                      draw.text((200, 150), f"YOUTUBE {IGN}", self.light_red, font=fontbig)
                    elif rank == "ADMIN":
                      draw.text((200, 150), f"ADMIN {IGN}", self.red, font=fontbig)
                    elif rank == "MOD":
                      draw.text((200, 150), f"MOD {IGN}", self.dark_green, font=fontbig)
                    else:
                      draw.text((200, 150), f"{rank} {IGN}", self.orangey, font=fontbig)

                    draw.text((800, 270), f"Games Played: {games:,}", self.white, font=font)
                    draw.text((200, 270), f"Coins: {coins:,}", self.white, font=font)

                    draw.text((200, 400), f"Wins: {wins:,}", self.white, font=font)
                    draw.text((200, 470), f"Losses: {losses:,}", self.white, font=font)
                    draw.text((200, 540), f"WLR: {WLR:,}", self.white, font=font)
                    
                    draw.text((800, 400), f"Swings: {swings:,}", self.white, font=font)
                    draw.text((800, 470), f"Hits: {hits:,}", self.white, font=font)
                    draw.text((800, 540), f"Accuracy: {accuracy:,}", self.white, font=font)

                    draw.text((200, 800), f"Winstreak: {ws:,}", self.white, font=font)
                    draw.text((800, 800), f"Best Winstreak: {best_ws:,}", self.white, font=font)

                    skin_img = Image.open(image_bytesio)
                    skin_img.thumbnail((500, 500))
                    img.paste(skin_img, (1400, 400), mask = skin_img)
                    

                    with io.BytesIO() as image_binary:
                      img.save(image_binary, 'PNG')
                      image_binary.seek(0)
                      await ctx.reply(file=discord.File(fp=image_binary, filename='image.png'), mention_author = False)
                  except:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)

                else:
                  errorembed = discord.Embed(title = 'Invalid Command Usage!')
                  errorembed.add_field(name = 'Usage:', value = "``.p {gamemode} {player}``")
                  errorembed.set_footer(text = 'Gamemode can be bedwars, skywars or duels')
                  errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                  await ctx.send(embed = errorembed)

    @commands.command(aliases = ["a", "ach"])
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def achievement(self, ctx, item : str = None, title : str = None, *, text : str = None):
      print("The Achievement Command was executed!")
      start = datetime.utcnow()
      if item is None:
        errorembed = discord.Embed(title = 'Achievement')
        errorembed.add_field(name = 'Usage:', value = "``.achievement {item} {title} {text}``")
        errorembed.add_field(name = '❔', value = 'Generates a image of a minecraft achievement using parameters provided by the user.', inline = False)
        errorembed.set_footer(text = 'Gamemode can be bedwars, skywars or duels')
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      elif title is None:
        errorembed = discord.Embed(title = 'Achievement')
        errorembed.add_field(name = 'Usage:', value = "``.achievement {item} {title} {text}``")
        errorembed.add_field(name = '❔', value = 'Generates a image of a minecraft achievement using parameters provided by the user.', inline = False)
        errorembed.set_footer(text = 'Gamemode can be bedwars, skywars or duels')
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      elif text is None:
        errorembed = discord.Embed(title = 'Achievement')
        errorembed.add_field(name = 'Usage:', value = "``.achievement {item} {title} {text}``")
        errorembed.add_field(name = '❔', value = 'Generates a image of a minecraft achievement using parameters provided by the user.', inline = False)
        errorembed.set_footer(text = 'Gamemode can be bedwars, skywars or duels')
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      else:
        try:
          async with ctx.typing():
            async with aiohttp.ClientSession() as cs:
              async with cs.get(f'https://api.obsidion-dev.com/api/v1/images/advancement?item={item}&title={title}&text={text}&title_color=%23defa3c&text_color=%23ffffff') as achievementRaw:

                url = str(achievementRaw.url)

                embed = discord.Embed(title = 'Achievement Maker')
                embed.set_image(url = f'{url}')
                
                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                embed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                
                await ctx.reply(embed = embed, mention_author = False)

        except Exception as e:
          errorembed = discord.Embed(title = 'Error!')
          errorembed.add_field(name = 'Something went wrong!', value = f"{e}")
          errorembed.set_footer(text = 'Be sure to only use one word as the title!')
          errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
          await ctx.send(embed = errorembed)
                

    @commands.command()
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def server(self, ctx, server : str = None):
        print("The Server Stats Command was executed!")
        start = datetime.utcnow()
        if server is None:
            errorembed = discord.Embed(title = 'Server')
            errorembed.add_field(name = 'Usage:', value = "``.server {server ip}``")
            errorembed.add_field(name = '❔', value = 'Returns the server status of a specified server IP.', inline = False)
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
          try:
            async with ctx.typing():
              async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.obsidion-dev.com/api/v1/server/java?server={server}') as serverinforaw:
                    serverjson = await serverinforaw.json()

                    serverinfoembed = discord.Embed(title = "Server Status", description = f"{server}", color = 0x2f3136)
                      
                    serverinfoembed.add_field(name = "Online:", value = f'{serverjson["players"]["online"]}/{serverjson["players"]["max"]}', inline = False)

                    serverinfoembed.set_thumbnail(url = f"https://api.obsidion-dev.com/api/v1/server/javaicon?server={server}")
                      
                    serverinfoembed.add_field(name = "Version:", value = f'{serverjson["version"]}', inline = False)
                      
                    serverinfoembed.add_field(name = "Numerical IP:", value = f'{serverjson["ip"]}', inline = False)
                      
                    response_time = datetime.utcnow() - start
                    hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                    minutes, secS = divmod(remainder, 60)
                    seconds = round(secS, 1)

                    serverinfoembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                    
                    await ctx.reply(embed=serverinfoembed, mention_author =  False)

          except:
            errorembed = discord.Embed()
            errorembed.add_field(name = 'Error!', value = f'{server} is not a valid server IP!')
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)

    @commands.command(aliases = ["socials", "s", "connections"])
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def social(self, ctx, user : str = None):
        print("The Socials Command was executed!")
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Socials')
            errorembed.add_field(name = 'Usage:', value = "``.s {username}``")
            errorembed.add_field(name = '❔', value = 'Returns the socials linked to a player\'s minecraft account on Hypixel.', inline = False)
            errorembed.add_field(name = 'Aliases:', value = '``socials, s, connections, social``')
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`")
            else:
              async with ctx.typing():
                    async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.slothpixel.me/api/players/{mojang_data["name"]}') as socialinforaw:
                        socialinfojson = await socialinforaw.json()

                    if socialinfojson["links"]["TWITTER"] == None:
                        twitter = "Not Linked"
                    else:
                        twitter = socialinfojson["links"]["TWITTER"]
                    
                    if socialinfojson["links"]["YOUTUBE"] == None:
                        youtube = "Not Linked"
                    else:
                        youtube =  socialinfojson["links"]["YOUTUBE"]
                    
                    if socialinfojson["links"]["INSTAGRAM"] == None:
                        instagram = "Not Linked"
                    else:
                        instagram = socialinfojson["links"]["INSTAGRAM"]
                    
                    if socialinfojson["links"]["TWITCH"] == None:
                        twitch = "Not Linked"
                    else:
                        twitch = socialinfojson["links"]["TWITCH"]
                    
                    if socialinfojson["links"]["DISCORD"] == None:
                        disc0rd = "Not Linked"
                    else:
                        disc0rd = socialinfojson["links"]["DISCORD"]
                    
                    if socialinfojson["links"]["HYPIXEL"] == None:
                        forums = "Not Linked"
                    else:
                        forums = socialinfojson["links"]["HYPIXEL"]
                    
                    socialembed = discord.Embed(title=f'Socials of {mojang_data["name"]}', color = 0x2f3136)
                    
                    socialembed.add_field(name="Discord:", value=f'{disc0rd}', inline=False)
                    
                    socialembed.add_field(name="Twitch:", value=f'{twitch}', inline=False)
                    
                    socialembed.add_field(name="Forums:", value=f'{forums}', inline=False)
                    
                    socialembed.add_field(name="Instagram:", value=f'{instagram}', inline=False)

                    socialembed.add_field(name = "YouTube:", value = f'{youtube}', inline=False)

                    socialembed.add_field(name = "Twitter:", value = f'{twitter}', inline=False)

                    response_time = datetime.utcnow() - start
                    hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                    minutes, secS = divmod(remainder, 60)
                    seconds = round(secS, 1)

                    socialembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                    
                    await ctx.reply(embed=socialembed, mention_author=False)
    
    @commands.command(aliases = ["wd", "wdr"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def watchdog(self, ctx):
      print("The WDR Command was executed!")
      start = datetime.utcnow()
      watchdog = await hywrap.watchdogStats(hypixelapikey)

      watchdogembed = discord.Embed(title = "Watchdog Bans", color = 0x2f3136)
      
      watchdogembed.add_field(name = "Last Minute:", value = f'{watchdog["watchdog_lastMinute"]:,}', inline = False)
      
      watchdogembed.add_field(name = "Daily:", value = f'{watchdog["watchdog_rollingDaily"]:,}', inline = False)
      
      watchdogembed.add_field(name = "Total:", value = f'{watchdog["watchdog_total"]:,}', inline = False)

      response_time = datetime.utcnow() - start
      hours, remainder = divmod(float(response_time.total_seconds()), 3600)
      minutes, secS = divmod(remainder, 60)
      seconds = round(secS, 1)

      watchdogembed.set_footer(text = f'Time taken to complete request: {seconds} s.')

      await ctx.reply(embed = watchdogembed, mention_author = False)

    """ WIP
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def leaderboards(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://api.hypixel.net/leaderboards?key={hypixelapikey}') as lbsRaw:
            lb = await lbsRaw.json()

            embed = discord.Embed(title = "Bedwars Leaderboards")
    """

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uuid(self, ctx, user : str = None):
      print("The UUID Command was executed!")
      start = datetime.utcnow()
      if user is None:
        errorembed = discord.Embed(title = 'UUID')
        errorembed.add_field(name = 'Usage:', value = "``.uuid {username}``")
        errorembed.add_field(name = '❔', value = 'Returns the UUID of a specified player.', inline = False)
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as mojangdataraw:
              try:
                mojang_data = await mojangdataraw.json()
              except aiohttp.client_exceptions.ContentTypeError:
                pass

              except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after=3)
            
              else:
                embed = discord.Embed(title = 'UUID Converter', color = 0x2f3136)
                
                embed.add_field(name = 'Username', value = f'``{mojang_data["name"]}``', inline = False)
                
                embed.add_field(name = 'UUID', value = f'``{mojang_data["id"]}``', inline = False)
                
                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, secS = divmod(remainder, 60)
                seconds = round(secS, 1)

                embed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                
                await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cape(self, ctx, user : str = None):
        print("The Cape Command was executed!")
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Cape')
            errorembed.add_field(name = 'Usage:', value = "``.profile {username}``")
            errorembed.add_field(name = '❔', value = 'Returns the optifine cape of a player.', inline = False)
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`")
            else:
              try:
                async with ctx.typing():
                  async with aiohttp.ClientSession() as cs:
                    async with cs.get(f'http://s.optifine.net/capes/{mojang_data["name"]}.png') as cape:
                      
                      embed = discord.Embed(title = f'{mojang_data["name"]}\'s Cape:', color = 0x2f3136)
                      
                      embed.set_image(url=cape.url)
                      
                      response_time = datetime.utcnow() - start
                      hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                      minutes, secS = divmod(remainder, 60)
                      seconds = round(secS, 1)

                      embed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                      
                      await ctx.reply(embed = embed, mention_author = False)
              except Exception as e:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} does not have a optifine cape!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def skin(self, ctx, user : str = None):
        print("The Skin Command was executed!")
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Skin')
            errorembed.add_field(name = 'Usage:', value = "``.skin {IGN}``", inline = False)
            errorembed.add_field(name = '❔', value = 'Returns the minecraft skin of a specified player.', inline = False)
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`")
            else:
                async with ctx.typing():
                  async with aiohttp.ClientSession() as cs:
                    async with cs.get(f'https://mc-heads.net/body/{mojang_data["id"]}/right') as skin:
                      
                      myurl = str(skin.url)
                      
                      embed = discord.Embed(title = f'{mojang_data["name"]}\'s Skin:', color = 0x2f3136)
                      
                      embed.set_image(url=myurl)

                      embed.add_field(name = 'Links', value = f'[NameMC](https://namemc.com/profile/{mojang_data["name"]})\n[Crafty.gg](https://crafty.gg/players/{mojang_data["name"]})')
                      
                      response_time = datetime.utcnow() - start
                      hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                      minutes, secS = divmod(remainder, 60)
                      seconds = round(secS, 1)

                      embed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                      
                      await ctx.reply(embed = embed, mention_author = False)

    @commands.command()
    @commands.cooldown(1, 2,commands.BucketType.user)
    async def profile(self, ctx, user : str = None):
        print("The Profile Command was executed!")
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Profile')
            errorembed.add_field(name = 'Usage:', value = "``.profile {username}``")
            errorembed.add_field(name = '❔', value = 'Returns the user\'s general Hypixel stats.', inline = False)
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`")
            else:
              async with ctx.typing():
                      async with aiohttp.ClientSession() as cs:
                        async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as profiledataraw:
                          profiledata = await profiledataraw.json()
                          rank = profiledata["rank"]
                      
                      async with aiohttp.ClientSession() as cs:
                        async with cs.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}') as guilddataraw:
                          guilddata = await guilddataraw.json()

                      if guilddata["guild"] == None:
                        guild = "None"
                      else:
                        guild = guilddata["guild"]["name"]

                      if profiledata["online"] == False:
                        status = "Offline <:offline:850325400180883487>"
                      else:
                        status = "Online <:online:850325400605425684>"

                      first_login = int(profiledata["first_login"])
                      first_login /= 1000

                      firstLogin = datetime.utcfromtimestamp(first_login).strftime('%Y-%m-%d %H:%M:%S')

                      last_logout = int(profiledata["last_logout"])
                      last_logout /= 1000

                      lastLogout = datetime.utcfromtimestamp(last_logout).strftime('%Y-%m-%d %H:%M:%S')

                      if rank == "MVP_PLUS_PLUS":
                        rank = "MVP++"
                      elif rank == "MVP_PLUS":
                        rank = "MVP+"
                      elif rank == "VIP_PLUS":
                        rank = "VIP+"
                      elif rank == None:
                        rank = "Non"
                      elif rank == "NONE":
                        rank = "Non"
                      elif rank == "YOUTUBER":
                        rank = "YOUTUBE"
                      elif rank == "MODERATOR":
                        rank = "MOD"
                      else:
                        rank = profiledata["rank"]
                      
                      
                      profileembed = discord.Embed(title=f'Profile of [{rank}] {profiledata["username"]}', color = 0x2f3136)
                      
                      profileembed.add_field(name="Karma:", value=f'{profiledata["karma"]:,}', inline = False)
                      
                      profileembed.add_field(name="Network Level:", value=f'{profiledata["level"]}', inline = False)
                      
                      profileembed.add_field(name="Quests completed:", value=f'{profiledata["quests_completed"]:,}', inline = False)
                      
                      profileembed.add_field(name="Most Recent Game:", value=f'{profiledata["last_game"]}', inline = False)

                      profileembed.add_field(name="First Login:", value=f'{firstLogin}', inline = False)
                      
                      profileembed.add_field(name="Last Logout:", value=f'{lastLogout}', inline = False)

                      profileembed.add_field(name = "Guild:", value = f'{guild}', inline = False)

                      profileembed.add_field(name = "Status:", value = f'{status}', inline = False)

                      response_time = datetime.utcnow() - start
                      hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                      minutes, secS = divmod(remainder, 60)
                      seconds = round(secS, 1)

                      profileembed.set_footer(text = f'Time taken to complete request: {seconds} s.')
                        
                      await ctx.reply(embed=profileembed, mention_author=False)

def setup(client):
    client.add_cog(minecraft(client))