import json
import aiohttp
import io
from datetime import datetime
from io import BytesIO
from discord.ext import commands

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

    @commands.command(
      aliases = ["bed", "bedwarz", "bedwars", "bedworz", "bedwar"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def bw(self, ctx, user=None):
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.bw {IGN}``")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                try:
                  async with aiohttp.ClientSession() as cs:
                        async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as bwdataraw:
                          bwdata = await bwdataraw.json()
                  
                  Wins = (bwdata["player"]["stats"]["Bedwars"]["wins_bedwars"])
                  Levels = (bwdata["player"]["achievements"]["bedwars_level"])
                  FinalDeaths = (bwdata["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
                  FinalKills = (bwdata["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
                  Kills = (bwdata["player"]["stats"]["Bedwars"]["kills_bedwars"])
                  Deaths = (bwdata["player"]["stats"]["Bedwars"]["deaths_bedwars"])
                  Coins = (bwdata["player"]["stats"]["Bedwars"]["coins"])
                  winstreak = (bwdata["player"]["stats"]["Bedwars"]["winstreak"])
                  FKDR = round(float(FinalKills) / float(FinalDeaths), 1) 
                  IGN = (mojang_data['name'])

                  bwembed = discord.Embed(title='Bedwars Stats', description=f'Overall | {IGN}', color=0x2f3136)

                  bwembed.add_field(name='Stars', value=f'``{Levels:,}``', inline=True)
                  
                  bwembed.add_field(name='Wins', value=f'``{Wins:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Deaths', value=f'``{FinalDeaths:,}``', inline=True)
                  
                  bwembed.add_field(name='FKDR', value=f'``{FKDR:,}``', inline=True)
                  
                  bwembed.add_field(name='Coins', value=f'``{Coins:,}``', inline=True)
                  
                  bwembed.add_field(name='Final Kills', value=f'``{FinalKills:,}``', inline=True)
                  
                  bwembed.add_field(name='Kills', value=f'``{Kills:,}``', inline=True)
                  
                  bwembed.add_field(name='Deaths', value=f'``{Deaths:,}``', inline=True)
                  
                  bwembed.add_field(name='Winstreak', value=f'``{winstreak:,}``', inline=True)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, seconds = divmod(remainder, 60)

                  bwembed.set_footer(text = f'Time taken to complete response: {seconds} s.')

                  await ctx.reply(embed=bwembed, mention_author=False)
                except:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
    
    @commands.command(
      aliases = ["skywars", "skywar", "skywor", "skiwar", "skiwor"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def sw(self, ctx, user=None):
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.sw {IGN}``")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as mojangraw:
                        mojang_data = await mojangraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
              try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as swdataraw:
                        swdata = await swdataraw.json()

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                          swlvldata = await swlvldataraw.json()
                
                SwWins = (swdata["player"]["stats"]["SkyWars"]["wins"])
                Heads = (swdata["player"]["stats"]["SkyWars"]["heads"])
                SwKills = (swdata["player"]["stats"]["SkyWars"]["kills"])
                SwDeaths = (swdata["player"]["stats"]["SkyWars"]["deaths"])
                SwLosses = (swdata["player"]["stats"]["SkyWars"]["losses"])
                SwCoins = (swdata["player"]["stats"]["SkyWars"]["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                IGN = str(mojang_data['name'])
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                swembed = discord.Embed(title='Skywars Stats', description=f'Overall | {IGN}', color=0x2f3136)

                swembed.add_field(name = 'Stars', value = f"``{SwLvl}``", inline = True)

                swembed.add_field(name='Wins', value=f'``{SwWins:,}``', inline = True)
                
                swembed.add_field(name='Losses', value=f'``{SwLosses:,}``', inline = True)
                
                swembed.add_field(name='WLR', value=f'``{SwWLR:,}``', inline = True)
                
                swembed.add_field(name='Heads', value=f'``{Heads:,}``', inline = True)
                
                swembed.add_field(name='Kills', value=f'``{SwKills:,}``', inline = True)
                
                swembed.add_field(name='Deaths', value=f'``{SwDeaths:,}``', inline = True)
                
                swembed.add_field(name='KDR', value=f'``{SwKDR:,}``', inline = True)
                
                swembed.add_field(name='Coins', value=f'``{SwCoins:,}``', inline = True)

                response_time = datetime.utcnow() - start
                hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                minutes, seconds = divmod(remainder, 60)

                swembed.set_footer(text = f'Time taken to complete response: {seconds} s.')

                await ctx.reply(embed=swembed, mention_author=False)
              except:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)

    @commands.command(
      aliases = ["duels", "d"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def duel(self, ctx, user=None):
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.d {IGN}``")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
              try:
                  async with aiohttp.ClientSession() as cs:
                        async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as duelsdataraw:
                          duelsdat4 = await duelsdataraw.json()
                  
                  
                  duels = duelsdat4["player"]["stats"]["Duels"]
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


                  duelsembed = discord.Embed(title = f'Duels Stats', description = f'Overall | {mojang_data["name"]}', color = 0x2f3136)
                  
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
                  minutes, seconds = divmod(remainder, 60)

                  duelsembed.set_footer(text = f'Time taken to complete response: {seconds} s.')
                  
                  await ctx.reply(embed=duelsembed, mention_author=False)
              except:
                errorembed = discord.Embed()
                errorembed.add_field(name = 'Error!', value = f'\n{mojang_data["name"]} has not played this gamemode!')
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)

    @commands.command()
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def p(self, ctx, gamemode = None, player = None):
        if player is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.p {gamemode} {IGN}``")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            errorembed.set_footer(text = 'Gamemode can be bedwars, skywars or duels')
            await ctx.send(embed = errorembed)
        elif gamemode is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.p {gamemode} {IGN}``")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{player}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{player}`", delete_after = 3)
            else:
              async with ctx.typing():
                img = Image.open("bw.png")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Minecraftia.ttf",
                                          40)
                fontbig = ImageFont.truetype("Minecraftia.ttf",
                                             40)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as apiraw:
                        api = await apiraw.json()

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

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}') as guilddataraw:
                        guilddata = await guilddataraw.json()

                if guilddata["guild"] == None:
                  guild = "None" 
                else:
                  guild = guilddata["guild"]["name"]

                if rank == "MVP_PLUS_PLUS":
                  rank = "MVP++"
                elif rank == "MVP_PLUS":
                  rank = "MVP+"
                elif rank == "VIP_PLUS":
                  rank = "VIP+"
                elif rank == None:
                  rank = "Non"
                elif rank == "YOUTUBER":
                  rank = "YOUTUBE"
                elif rank == "MODERATOR":
                  rank = "MOD"
                else:
                  rank = profiledata["rank"]
                
                if gamemode == "bedwars":
                  try:
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
                    IGN = (mojang_data['name'])
                    
                    if rank == "VIP+":
                      draw.text((200, 150), f"[VIP+] {IGN} [{guild}]", self.green, font=fontbig)
                    elif rank == "VIP":
                      draw.text((200, 150), f"[VIP] {IGN} [{guild}]", self.green, font=fontbig)
                    elif rank == "MVP":
                      draw.text((200, 150), f"[MVP] {IGN} [{guild}]", self.aqua, font=fontbig)
                    elif rank == "MVP+":
                      draw.text((200, 150), f"[MVP+] {IGN} [{guild}]", self.aqua, font=fontbig)
                    elif rank == "MVP++":
                      draw.text((200, 150), f"[MVP++] {IGN} [{guild}]", self.gold, font=fontbig)
                    elif rank == "YOUTUBE":
                      draw.text((200, 150), f"[YOUTUBE] {IGN} [{guild}]", self.light_red, font=fontbig)
                    elif rank == "ADMIN":
                      draw.text((200, 150), f"[ADMIN] {IGN} [{guild}]", self.red, font=fontbig)
                    elif rank == "MOD":
                      draw.text((200, 150), f"[MOD] {IGN} [{guild}]", self.dark_green, font=fontbig)
                    else:
                      draw.text((200, 150), f"[{rank}] {IGN} [{guild}]", self.orangey, font=fontbig)

                    draw.text((920, 270), f"{Levels:,}", self.white, font=font)
                    draw.text((470, 270), f"{winstreak:,}", self.white, font=font)
                    draw.text((1350, 270), f"{coins:,}", self.white, font=font)

                    draw.text((465, 396), f"{FinalKills:,}", self.white, font=font)
                    draw.text((535, 466), f"{FinalDeaths:,}", self.white, font=font)
                    draw.text((350, 536), f"{FKDR:,}", self.white, font=font)
                    
                    draw.text((880, 396), f"{Kills:,}", self.white, font=font)
                    draw.text((950, 466), f"{Deaths:,}", self.white, font=font)
                    draw.text((870, 536), f"{KDR:,}", self.white, font=font)
                    

                    draw.text((450, 797), f"{void_kdr:,}", self.white, font=font)
                    draw.text((900, 800), f"{BBLR:,}", self.white, font=font)
                    draw.text((1570, 800), f"{games:,}", self.white, font=font)
                    
                    draw.text((1320, 396), f"{Wins:,}", self.white, font=font)
                    draw.text((1420, 466), f"{Losses:,}", self.white, font=font)
                    draw.text((1320, 536), f"{WLR:,}", self.white, font=font)

                    with io.BytesIO() as image_binary:
                        img.save(image_binary, 'PNG')
                        image_binary.seek(0)
                        await ctx.reply(file=discord.File(fp=image_binary, filename='image.png'), mention_author = False)

                  except:
                    errorembed = discord.Embed()
                    errorembed.add_field(name = 'Error!', value = f'{mojang_data["name"]} has not played this gamemode!')
                    errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                    await ctx.send(embed = errorembed)
                
                elif gamemode == "skywars":
                  try:
                    img = Image.open("sw.png")
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("Minecraftia.ttf",
                                              40)
                    fontbig = ImageFont.truetype("Minecraftia.ttf",
                                                40)
                    
                    SwWins = (api["player"]["stats"]["SkyWars"]["wins"])
                    Heads = (api["player"]["stats"]["SkyWars"]["heads"])
                    SwKills = (api["player"]["stats"]["SkyWars"]["kills"])
                    SwDeaths = (api["player"]["stats"]["SkyWars"]["deaths"])
                    lastmode = (api["player"]["stats"]["SkyWars"]["lastMode"])
                    SwLosses = (api["player"]["stats"]["SkyWars"]["losses"])
                    SwCoins = (api["player"]["stats"]["SkyWars"]["coins"])
                    SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                    SwWLR = round(float(SwWins) / float(SwLosses), 1)
                    IGN = (mojang_data['name'])
                    SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                    if rank == "VIP+":
                      draw.text((200, 150), f"[VIP+] {IGN} [{guild}]", self.green, font=fontbig)
                    elif rank == "VIP":
                      draw.text((200, 150), f"[VIP] {IGN} [{guild}]", self.green, font=fontbig)
                    elif rank == "MVP":
                      draw.text((200, 150), f"[MVP] {IGN} [{guild}]", self.aqua, font=fontbig)
                    elif rank == "MVP+":
                      draw.text((200, 150), f"[MVP+] {IGN} [{guild}]", self.aqua, font=fontbig)
                    elif rank == "MVP++":
                      draw.text((200, 150), f"[MVP++] {IGN} [{guild}]", self.gold, font=fontbig)
                    elif rank == "YOUTUBE":
                      draw.text((200, 150), f"[YOUTUBE] {IGN} [{guild}]", self.light_red, font=fontbig)
                    elif rank == "ADMIN":
                      draw.text((200, 150), f"[ADMIN] {IGN} [{guild}]", self.red, font=fontbig)
                    elif rank == "MOD":
                      draw.text((200, 150), f"[MOD] {IGN} [{guild}]", self.dark_green, font=fontbig)
                    else:
                      draw.text((200, 150), f"[{rank}] {IGN} [{guild}]", self.orangey, font=fontbig)


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

                elif gamemode == "duels":
                  try:
                    img = Image.open("duels.png")
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("Minecraftia.ttf",
                                              40)
                    fontbig = ImageFont.truetype("Minecraftia.ttf",
                                                40)
                    
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
                    IGN = str(mojang_data['name'])

                    if rank == "MVP_PLUS_PLUS":
                      rank = "MVP++"
                    elif rank == "MVP_PLUS":
                      rank = "MVP+"
                    elif rank == "VIP_PLUS":
                      rank = "VIP+"
                    elif rank == None:
                      rank = "Non"
                    elif rank == "YOUTUBER":
                      rank = "YOUTUBE"
                    elif rank == "MODERATOR":
                      rank = "MOD"
                    else:
                      rank = profiledata["rank"]
                    
                    if rank == "VIP+":
                      draw.text((200, 150), f"[VIP+] {IGN} [{guild}]", self.green, font=fontbig)
                    elif rank == "VIP":
                      draw.text((200, 150), f"[VIP] {IGN} [{guild}]", self.green, font=fontbig)
                    elif rank == "MVP":
                      draw.text((200, 150), f"[MVP] {IGN} [{guild}]", self.aqua, font=fontbig)
                    elif rank == "MVP+":
                      draw.text((200, 150), f"[MVP+] {IGN} [{guild}]", self.aqua, font=fontbig)
                    elif rank == "MVP++":
                      draw.text((200, 150), f"[MVP++] {IGN} [{guild}]", self.gold, font=fontbig)
                    elif rank == "YOUTUBE":
                      draw.text((200, 150), f"[YOUTUBE] {IGN} [{guild}]", self.light_red, font=fontbig)
                    elif rank == "ADMIN":
                      draw.text((200, 150), f"[ADMIN] {IGN} [{guild}]", self.red, font=fontbig)
                    elif rank == "MOD":
                      draw.text((200, 150), f"[MOD] {IGN} [{guild}]", self.dark_green, font=fontbig)
                    else:
                      draw.text((200, 150), f"[{rank}] {IGN} [{guild}]", self.orangey, font=fontbig)


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


    @commands.command()
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def server(self, ctx, server : str = None):
        start = datetime.utcnow()
        if server is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.server {server ip}``")
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
                      
                    serverinfoembed.add_field(name = "Version:", value = f'{serverjson["version"]}', inline = False)
                      
                    serverinfoembed.add_field(name = "Numerical IP:", value = f'{serverjson["ip"]}', inline = False)
                      
                    response_time = datetime.utcnow() - start
                    hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                    minutes, seconds = divmod(remainder, 60)

                    serverinfoembed.set_footer(text = f'Time taken to complete response: {seconds} s.')
                    
                    await ctx.reply(embed=serverinfoembed, mention_author =  False)

          except:
            errorembed = discord.Embed()
            errorembed.add_field(name = 'Error!', value = f'{server} is not a valid server IP!')
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
      
    @commands.command(
      aliases = ["socials", "s", "connections"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def social(self, ctx, user=None):
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.s {username}``")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
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
                    minutes, seconds = divmod(remainder, 60)

                    socialembed.set_footer(text = f'Time taken to complete response: {seconds} s.')
                    
                    await ctx.reply(embed=socialembed, mention_author=False)
    
    @commands.command(
      aliases = ["wd", "wdr"]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def watchdog(self, ctx):
      start = datetime.utcnow()
      async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.slothpixel.me/api/bans') as watchdograw:
                  watchdog = await watchdograw.json()

                  watchdogembed = discord.Embed(title = "Watchdog Bans", color = 0x2f3136)
                  
                  watchdogembed.add_field(name = "Last Minute:", value = f'{watchdog["watchdog"]["last_minute"]:,}', inline = False)
                  
                  watchdogembed.add_field(name = "Daily:", value = f'{watchdog["watchdog"]["daily"]:,}', inline = False)
                  
                  watchdogembed.add_field(name = "Total:", value = f'{watchdog["watchdog"]["total"]:,}', inline = False)

                  response_time = datetime.utcnow() - start
                  hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                  minutes, seconds = divmod(remainder, 60)

                  watchdogembed.set_footer(text = f'Time taken to complete response: {seconds} s.')

                  await ctx.reply(embed = watchdogembed, mention_author = False)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uuid(self, ctx, user = None):
      start = datetime.utcnow()
      if user is None:
        errorembed = discord.Embed(title = 'Invalid Command Usage!')
        errorembed.add_field(name = 'Usage:', value = "``.uuid {username}``")
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as mojangdataraw:
                    
                    try:
                      mojang_data = await mojangdataraw.json()
                    except aiohttp.client_exceptions.ContentTypeError:
                      pass

            if not mojang_data:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after=3)
            else:
              embed = discord.Embed(title = 'UUID Converter', color = 0x2f3136)
              embed.add_field(name = 'Username', value = f'``{mojang_data["name"]}``', inline = False)
              embed.add_field(name = 'UUID', value = f'``{mojang_data["id"]}``', inline = False)
              await ctx.send(embed = embed)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def skin(self, ctx, user = None):
      start = datetime.utcnow()
      if user is None:
        errorembed = discord.Embed(title = 'Invalid Command Usage!', color = 0x2f3136)
        errorembed.add_field(name = 'Usage:', value = "``.skin {username}``")
        errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
        await ctx.send(embed = errorembed)
      else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as mojangdataraw:
                    
                    try:
                      mojang_data = await mojangdataraw.json()
                    except aiohttp.client_exceptions.ContentTypeError:
                      pass

            if not mojang_data:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after=3)
            else:
              async with ctx.typing():
                async with aiohttp.ClientSession() as cs:
                  async with cs.get(f'https://mc-heads.net/body/{mojang_data["id"]}/right') as skin:
                    sk1n = await skin.read()
                    
                    myurl = str(skin.url)
                    
                    embed = discord.Embed(title = f'{mojang_data["name"]}\'s Skin:', color = 0x2f3136)
                    
                    embed.set_image(url=myurl)
                    
                    response_time = datetime.utcnow() - start
                    hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                    minutes, seconds = divmod(remainder, 60)

                    embed.set_footer(text = f'Time taken to complete response: {seconds} s.')
                    
                    await ctx.reply(embed = embed, mention_author = False)
                  
      
    
    @commands.command()
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def profile(self, ctx, user=None):
        start = datetime.utcnow()
        if user is None:
            errorembed = discord.Embed(title = 'Invalid Command Usage!')
            errorembed.add_field(name = 'Usage:', value = "``.s {username}``")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
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
                        

                      if rank == "MVP_PLUS_PLUS":
                        rank = "MVP++"
                      elif rank == "MVP_PLUS":
                        rank = "MVP+"
                      elif rank == "VIP_PLUS":
                        rank = "VIP+"
                      elif rank == None:
                        rank = "Non"
                      elif rank == "YOUTUBER":
                        rank = "YOUTUBE"
                      elif rank == "MODERATOR":
                        rank = "MOD"
                      else:
                        rank = profiledata["rank"]
                      
                      
                      profileembed = discord.Embed(title=f'Profile of [{rank}] {profiledata["username"]}', color = 0x2f3136)
                      
                      profileembed.add_field(name="Karma:", value=f'{profiledata["karma"]:,}', inline=False)
                      
                      profileembed.add_field(name="Network Level:", value=f'{profiledata["level"]}', inline=False)
                      
                      profileembed.add_field(name="Quests completed:", value=f'{profiledata["quests_completed"]:,}', inline=False)
                      
                      profileembed.add_field(name="Most Recent Game:", value=f'{profiledata["last_game"]}', inline=False)

                      profileembed.add_field(name = "Guild:", value = f'{guild}', inline=False)

                      profileembed.add_field(name = "Status:", value = f'{status}', inline=False)

                      response_time = datetime.utcnow() - start
                      hours, remainder = divmod(float(response_time.total_seconds()), 3600)
                      minutes, seconds = divmod(remainder, 60)

                      profileembed.set_footer(text = f'Time taken to complete response: {seconds} s.')
                        
                      await ctx.reply(embed=profileembed, mention_author=False)

def setup(client):
    client.add_cog(minecraft(client))