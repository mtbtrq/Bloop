import json
import aiohttp
import io
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
        self.white = 255, 255, 255
        self.somecoloridklmfao = 246, 76, 114

    @commands.command(
      aliases = ["bed", "bedwarz", "bedwars", "bedworz", "bedwar"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def bw(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                img = Image.open("bw.png")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Minecraftia.ttf",
                                          40)
                fontbig = ImageFont.truetype("Minecraftia.ttf",
                                             45)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as bwdataraw:
                        bwdata = await bwdataraw.json()

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as profiledataraw:
                        profiledata = await profiledataraw.json()
                        rank = profiledata["rank"]

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}') as guilddataraw:
                        guilddata = await guilddataraw.json()

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f'https://crafatar.com/renders/body/{mojang_data["id"]}?&overlay') as skin:
                      skin_read = await skin.read()
                      image_bytesio = io.BytesIO(skin_read)
                
                      
                      
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
                        pass
                      
                      else:
                        rank = profiledata["rank"]
                


                Wins = (bwdata["player"]["stats"]["Bedwars"]["wins_bedwars"])
                bedsbroken = bwdata["player"]["stats"]["Bedwars"]["beds_broken_bedwars"]
                bedslost = bwdata["player"]["stats"]["Bedwars"]["beds_lost_bedwars"]
                Losses = (bwdata["player"]["stats"]["Bedwars"]["losses_bedwars"])
                Levels = (bwdata["player"]["achievements"]["bedwars_level"])
                FinalDeaths = (bwdata["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
                FinalKills = (bwdata["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
                winstreak = (bwdata["player"]["stats"]["Bedwars"]["winstreak"])
                coins = (bwdata["player"]["stats"]["Bedwars"]["coins"])
                FKDR = round(float(FinalKills) / float(FinalDeaths), 1)
                WLR = round(float(Wins) / float(Losses), 1)
                BBLR = round(float(bedsbroken) / float(bedslost), 1)
                IGN = (mojang_data['name'])

                draw.text((200, 150), f"[{rank}] {IGN} [{guild}]", self.somecoloridklmfao, font=fontbig)
                draw.text((800, 270), f"Stars: {Levels:,}", self.white, font=font)
                draw.text((200, 270), f"Winstreak: {winstreak:,}", self.white, font=font)

                draw.text((200, 400), f"Final Kills: {FinalKills:,}", self.white, font=font)
                draw.text((200, 470), f"Final Deaths: {FinalDeaths:,}", self.white, font=font)
                draw.text((200, 540), f"FKDR: {FKDR:,}", self.white, font=font)
                
                draw.text((800, 400), f"Wins: {Wins:,}", self.white, font=font)
                draw.text((800, 470), f"Losses: {Losses:,}", self.white, font=font)
                draw.text((800, 540), f"WLR: {WLR:,}", self.white, font=font)

                draw.text((200, 800), f"Coins: {coins:,}", self.white, font=font)
                draw.text((800, 800), f"BBLR: {BBLR:,}", self.white, font=font)

                skin_img = Image.open(image_bytesio)
                skin_img.thumbnail((500, 500))
                img.paste(skin_img, (1400, 400), mask = skin_img)

                skin_img = Image.open(image_bytesio)
                skin_img.thumbnail((500, 500))
                img.paste(skin_img, (1400, 400), mask = skin_img)
                

                with io.BytesIO() as image_binary:
                    img.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    await ctx.reply(file=discord.File(fp=image_binary, filename='image.png'), mention_author = False)
    
    @commands.command(
      aliases = ["skywars", "skywar", "skywor", "skiwar", "skiwor"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def sw(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                img = Image.open("sw.png")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Minecraftia.ttf",
                                          40)
                fontbig = ImageFont.truetype("Minecraftia.ttf",
                                             45)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as swdataraw:
                        swdata = await swdataraw.json()

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as profiledataraw:
                        profiledata = await profiledataraw.json()
                        rank = profiledata["rank"]

                    if rank == "MVP_PLUS_PLUS":
                      rank = "MVP++"
                    elif rank == "MVP_PLUS":
                      rank = "MVP+"
                    elif rank == "VIP_PLUS":
                      rank = "VIP+"
                    elif rank == None:
                      rank = "Non"
                    else:
                      rank = profiledata["rank"]
                

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}') as guilddataraw:
                        guilddata = await guilddataraw.json()

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f'https://crafatar.com/renders/body/{mojang_data["id"]}?&overlay') as skin:
                      skin_read = await skin.read()
                      image_bytesio = io.BytesIO(skin_read)
                
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as swlvldataraw:
                        swlvldata = await swlvldataraw.json()

                        if guilddata["guild"] == None:
                            guild = "None"
                        else:
                            guild = guilddata["guild"]["name"]
                
                SwWins = (swdata["player"]["stats"]["SkyWars"]["wins"])
                Heads = (swdata["player"]["stats"]["SkyWars"]["heads"])
                SwKills = (swdata["player"]["stats"]["SkyWars"]["kills"])
                SwDeaths = (swdata["player"]["stats"]["SkyWars"]["deaths"])
                lastmode = (swdata["player"]["stats"]["SkyWars"]["lastMode"])
                SwLosses = (swdata["player"]["stats"]["SkyWars"]["losses"])
                SwCoins = (swdata["player"]["stats"]["SkyWars"]["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                IGN = str(mojang_data['name'])
                SwLvl = round(swlvldata["stats"]["SkyWars"]["level"], 1)

                draw.text((200, 150), f"[{rank}] {IGN} [{guild}]", self.somecoloridklmfao, font=fontbig)
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

    @commands.command(
      aliases = ["duels", "d"]
    )
    async def duel(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.mojang.com/users/profiles/minecraft/{user}') as moj4ngdataraw:
                        mojang_data = await moj4ngdataraw.json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                img = Image.open("duels.png")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Minecraftia.ttf",
                                          40)
                fontbig = ImageFont.truetype("Minecraftia.ttf",
                                             45)

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}") as duelsdataraw:
                        duelsdat = await duelsdataraw.json()

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f"https://api.slothpixel.me/api/players/{user}") as profiledataraw:
                        profiledata = await profiledataraw.json()
                        rank = profiledata["rank"]

                    if rank == "MVP_PLUS_PLUS":
                      rank = "MVP++"
                    elif rank == "MVP_PLUS":
                      rank = "MVP+"
                    elif rank == "VIP_PLUS":
                      rank = "VIP+"
                    elif rank == None:
                      rank = "Non"
                    else:
                      rank = profiledata["rank"]
                

                async with aiohttp.ClientSession() as cs:
                      async with cs.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}') as guilddataraw:
                        guilddata = await guilddataraw.json()

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f'https://crafatar.com/renders/body/{mojang_data["id"]}?&overlay') as skin:
                      skin_read = await skin.read()
                      image_bytesio = io.BytesIO(skin_read)

                    if guilddata["guild"] == None:
                        guild = "None"
                    else:
                        guild = guilddata["guild"]["name"]

                
                duels = duelsdat["player"]["stats"]["Duels"]
                
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
                

                draw.text((200, 150), f"[{rank}] {IGN} [{guild}]", self.somecoloridklmfao, font=fontbig)
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

    @commands.command()
    async def server(self, ctx, server):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.obsidion-dev.com/api/v1/server/java?server={server}') as serverinforaw:
                serverjson = await serverinforaw.json()

                serverinfoembed = discord.Embed(title = "Server Status", description = f"{server}")
                
                serverinfoembed.add_field(name = "Online:", value = f'{serverjson["players"]["online"]}/{serverjson["players"]["max"]}', inline = False)
                
                serverinfoembed.add_field(name = "Version:", value = f'{serverjson["version"]}', inline = False)
                
                serverinfoembed.add_field(name = "Numerical IP:", value = f'{serverjson["ip"]}', inline = False)
                
                serverinfoembed.set_footer(text = "Courtesy of api.obsidion-dev.com")
                await ctx.reply(embed=serverinfoembed, mention_author =  False)
      
    @commands.command(
      aliases = ["socials", "s", "connections"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def social(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after=3)
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


                    
                    
                    socialembed = discord.Embed(title=f'Socials of {mojang_data["name"]}')
                    
                    socialembed.add_field(name="Discord:", value=f'{disc0rd}', inline=False)
                    
                    socialembed.add_field(name="Twitch:", value=f'{twitch}', inline=False)
                    
                    socialembed.add_field(name="Forums:", value=f'{forums}', inline=False)
                    
                    socialembed.add_field(name="Instagram:", value=f'{instagram}', inline=False)

                    socialembed.add_field(name = "YouTube:", value = f'{youtube}', inline=False)

                    socialembed.add_field(name = "Twitter:", value = f'{twitter}', inline=False)
                    
                    await ctx.reply(embed=socialembed, mention_author=False)
    
    @commands.command(
      aliases = ["wd", "wdr"]
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def watchdog(self, ctx):
      async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://api.slothpixel.me/api/bans') as watchdograw:
                  watchdog = await watchdograw.json()

                  watchdogembed = discord.Embed(title = "Watchdog Bans", color = 0x2f3136)
                  
                  watchdogembed.add_field(name = "Last Minute:", value = f'{watchdog["watchdog"]["last_minute"]:,}', inline = False)
                  
                  watchdogembed.add_field(name = "Daily:", value = f'{watchdog["watchdog"]["daily"]:,}', inline = False)
                  
                  watchdogembed.add_field(name = "Total:", value = f'{watchdog["watchdog"]["total"]:,}', inline = False)

                  await ctx.reply(embed = watchdogembed, mention_author = False)
      
    
    @commands.command(
      aliases = ["p"]
    )
    @commands.cooldown(1, 5,commands.BucketType.user)
    async def profile(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after=3)
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
                    else:
                      rank = profiledata["rank"]
                    
                    
                    profileembed = discord.Embed(
                        title=f'Profile of [{rank}] {profiledata["username"]}')
                    
                    profileembed.add_field(
                        name="Karma:", value=f'{profiledata["karma"]:,}', inline=False)
                    
                    profileembed.add_field(
                        name="Network Level:", value=f'{profiledata["level"]}', inline=False)
                    
                    profileembed.add_field(
                        name="Quests completed:", value=f'{profiledata["quests_completed"]:,}', inline=False)
                    
                    profileembed.add_field(
                        name="Most Recent Game:", value=f'{profiledata["last_game"]}', inline=False)

                    profileembed.add_field(name = "Guild:", value = f'{guild}', inline=False)

                    profileembed.add_field(name = "Status:", value = f'{status}', inline=False)
                    
                    profileembed.set_footer(
                        text=f"This command uses the Slothpixel API, which is slow at updating.")
                    
                    await ctx.reply(embed=profileembed, mention_author=False)

def setup(client):
    client.add_cog(minecraft(client))