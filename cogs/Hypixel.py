import discord
import requests
import json
import random
from discord.ext import commands

hypix3lapikey = ["HYPIXEL API KEY 1",
                "HYPIXEL API KEY 2"]
hypixelapikey = random.choice(hypix3lapikey)

class Hypixel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=['nwlvl']
    )
    @commands.cooldown(1, 10,commands.BucketType.user)
    async def nwlevel(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                network_data_v2  = requests.get(
                  f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(f'Network level of ``{user}``: {network_data_v2["level"]}.')

    @commands.command()
    @commands.cooldown(1, 10,commands.BucketType.user)
    async def bw(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                data = requests.get(
                    f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}").json()
                
                Wins = (data["player"]["stats"]["Bedwars"]["wins_bedwars"])
                Levels = (data["player"]["achievements"]["bedwars_level"])
                FinalDeaths = (data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
                FinalKills = (data["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
                Kills = (data["player"]["stats"]["Bedwars"]["kills_bedwars"])
                Deaths = (data["player"]["stats"]["Bedwars"]["deaths_bedwars"])
                Coins = (data["player"]["stats"]["Bedwars"]["coins"])
                winstreak = (data["player"]["stats"]["Bedwars"]["winstreak"])
                FKDR = round(float(FinalKills) / float(FinalDeaths), 1) 
                IGN = (mojang_data['name'])

                bwembed = discord.Embed(
                    title='Bedwars Stats', description=f'Bedwars Stats of {IGN}', color=0x2f3136)

                bwembed.add_field(
                    name='Stars', value=f'``{Levels:,}``', inline=True)
                
                bwembed.add_field(
                    name='Wins', value=f'``{Wins:,}``', inline=True)
                
                bwembed.add_field(
                    name='Final Deaths', value=f'``{FinalDeaths:,}``', inline=True)
                
                bwembed.add_field(
                    name='FKDR', value=f'``{FKDR:,}``', inline=True)
                
                bwembed.add_field(
                    name='Coins', value=f'``{Coins:,}``', inline=True)
                
                bwembed.add_field(
                    name='Final Kills', value=f'``{FinalKills:,}``', inline=True)
                
                bwembed.add_field(
                    name='Kills', value=f'``{Kills:,}``', inline=True)
                
                bwembed.add_field(
                    name='Deaths', value=f'``{Deaths:,}``', inline=True)
                
                bwembed.add_field(
                    name='Winstreak', value=f'``{winstreak:,}``', inline=True)
                
                bwembed.set_thumbnail(
                    url='https://media.discordapp.net/attachments/836614888080015381/837749892382326834/logo.png')

                await ctx.send(embed=bwembed)


    @commands.command()
    @commands.cooldown(1, 10,commands.BucketType.user)
    async def sw(self, ctx, user=None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                data = requests.get(
                    f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}").json()
                
                SwWins = (data["player"]["stats"]["SkyWars"]["wins"])
                Heads = (data["player"]["stats"]["SkyWars"]["heads"])
                SwKills = (data["player"]["stats"]["SkyWars"]["kills"])
                SwDeaths = (data["player"]["stats"]["SkyWars"]["deaths"])
                SwLosses = (data["player"]["stats"]["SkyWars"]["losses"])
                SwCoins = (data["player"]["stats"]["SkyWars"]["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                IGN = str(mojang_data['name'])

                swembed = discord.Embed(
                    title='Skywars Stats', description=f'Skywars Stats of {IGN}', color=0x2f3136)

                swembed.add_field(
                    name='Wins', value=f'``{SwWins:,}``', inline=True)
                
                swembed.add_field(
                    name='Losses', value=f'``{SwLosses:,}``', inline=True)
                
                swembed.add_field(
                    name='WLR', value=f'``{SwWLR:,}``', inline=True)
                
                swembed.add_field(
                    name='Heads', value=f'``{Heads:,}``', inline=True)
                
                swembed.add_field(
                    name='Kills', value=f'``{SwKills:,}``', inline=True)
                
                swembed.add_field(
                    name='Deaths', value=f'``{SwDeaths:,}``', inline=True)
                
                swembed.add_field(
                    name='KDR', value=f'``{SwKDR:,}``', inline=True)
                
                swembed.add_field(
                    name='Coins', value=f'``{SwCoins:,}``', inline=True)
                
                swembed.set_thumbnail(
                    url='https://media.discordapp.net/attachments/836614888080015381/837749892382326834/logo.png')

                await ctx.send(embed=swembed)

    @commands.command(
      aliases = ["p"]
    )
    async def profile(self, ctx, user=None):
      if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
      else:
            try:
                mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
               try:
                profiledata = requests.get(
                    f"https://api.slothpixel.me/api/players/{user}").json()
                guildinfo = requests.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={mojang_data["id"]}').json()
                
                profileembed = discord.Embed(title = f'Profile of {profiledata["username"]}')
                
                profileembed.add_field(name = "Rank:", value = f'{profiledata["rank"]}', inline=False)
                
                profileembed.add_field(name = "Karma:", value = f'{profiledata["karma"]:,}', inline=False)
                
                profileembed.add_field(name = "Network Level:", value = f'{profiledata["level"]}', inline=False)
                
                profileembed.add_field(name = "Quests completed:", value = f'{profiledata["quests_completed"]:,}', inline=False)
                
                profileembed.add_field(name = "Most Recent Game:", value = f'{profiledata["last_game"]}', inline=False)

                profileembed.add_field(name = "Guild:", value = f'{guildinfo["guild"]["name"]}')

                profileembed.set_footer(text = f"This command uses the Slothpixel API, which is slow at updating.")
                
                await ctx.send(embed=profileembed)
               except Exception as e:
                   print(e)

def setup(client):
    client.add_cog(Hypixel(client))