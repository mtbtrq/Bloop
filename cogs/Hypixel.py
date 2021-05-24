import discord
import requests
import json
from discord.ext import commands

with open('./config.json') as d:
    config = json.load(d)
hypixelapikey = config.get('hypixelapikey')

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
                networkdata = requests.get(
            f"https://api.slothpixel.me/api/players/{user}").json()

        await ctx.send(networkdata["level"])

    @commands.command(
        aliases=['k']
    )
    @commands.cooldown(1, 10,commands.BucketType.user)
    async def karma(self, ctx, user = None):
        if user is None:
            await ctx.send("Please provide a valid user!", delete_after = 3)
        else:
            try:
                mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
            except:
                await ctx.send(f"The user your provided is not valid! `{user}`", delete_after = 3)
            else:
                karmadata = requests.get(
                    f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={mojang_data['id']}").json()

                karma = str(karmadata["player"]["karma"])
                karmaIGN = str(karmadata["displayname"])

                karmaembed = discord.Embed(title = f"{karmaIGN}'s Karma.", color=0x2f3136)
                karmaembed.add_field(name = f"Karma:", value = f"{karma}")
                await ctx.send(embed=karmaembed)

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
                
                Wins = str(data["player"]["stats"]["Bedwars"]["wins_bedwars"])
                Levels = str(data["player"]["achievements"]["bedwars_level"])
                FinalDeaths = str(data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
                FinalKills = str(data["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
                Kills = str(data["player"]["stats"]["Bedwars"]["kills_bedwars"])
                Deaths = str(data["player"]["stats"]["Bedwars"]["deaths_bedwars"])
                Coins = str(data["player"]["stats"]["Bedwars"]["coins"])
                winstreak = str(data["player"]["stats"]["Bedwars"]["winstreak"])
                FKDR = round(float(FinalKills) / float(FinalDeaths), 1) 
                IGN = str(mojang_data['name'])

                bwembed = discord.Embed(
                    title='Bedwars Stats', description=f'Bedwars Stats of {IGN}', color=0x2f3136)

                bwembed.add_field(
                    name='Stars', value=f'``{Levels}``', inline=True)
                bwembed.add_field(
                    name='Wins', value=f'``{Wins}``', inline=True)
                bwembed.add_field(
                    name='Final Deaths', value=f'``{FinalDeaths}``', inline=True)
                bwembed.add_field(
                    name='FKDR', value=f'``{FKDR}``', inline=True)
                bwembed.add_field(
                    name='Coins', value=f'``{Coins}``', inline=True)
                bwembed.add_field(
                    name='Final Kills', value=f'``{FinalKills}``', inline=True)
                bwembed.add_field(
                    name='Kills', value=f'``{Kills}``', inline=True)
                bwembed.add_field(
                    name='Deaths', value=f'``{Deaths}``', inline=True)
                bwembed.add_field(
                    name='Winstreak', value=f'``{winstreak}``', inline=True)
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
                
                SwWins = str(data["player"]["stats"]["SkyWars"]["wins"])
                Heads = str(data["player"]["stats"]["SkyWars"]["heads"])
                SwKills = str(data["player"]["stats"]["SkyWars"]["kills"])
                SwDeaths = str(data["player"]["stats"]["SkyWars"]["deaths"])
                SwLosses = str(data["player"]["stats"]["SkyWars"]["losses"])
                SwCoins = str(data["player"]["stats"]["SkyWars"]["coins"])
                SwKDR = round(float(SwKills) / float(SwDeaths), 1)
                SwWLR = round(float(SwWins) / float(SwLosses), 1)
                IGN = str(mojang_data['name'])

                swembed = discord.Embed(
                    title='Skywars Stats', description=f'Skywars Stats of {IGN}', color=0x2f3136)

                swembed.add_field(
                    name='Wins', value=f'``{SwWins}``', inline=True)
                swembed.add_field(
                    name='Losses', value=f'``{SwLosses}``', inline=True)
                swembed.add_field(
                    name='WLR', value=f'``{SwWLR}``', inline=True)
                swembed.add_field(
                    name='Heads', value=f'``{Heads}``', inline=True)
                swembed.add_field(
                    name='Kills', value=f'``{SwKills}``', inline=True)
                swembed.add_field(
                    name='Deaths', value=f'``{SwDeaths}``', inline=True)
                swembed.add_field(
                    name='KDR', value=f'``{SwKDR}``', inline=True)
                swembed.add_field(
                    name='Coins', value=f'``{SwCoins}``', inline=True)
                swembed.set_thumbnail(
                    url='https://media.discordapp.net/attachments/836614888080015381/837749892382326834/logo.png')

                await ctx.send(embed=swembed)


def setup(client):
    client.add_cog(Hypixel(client))