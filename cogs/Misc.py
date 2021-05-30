import discord
import random
import requests
import aiohttp
import tracemalloc
import asyncio
from asyncio import sleep as s
import json
from aiohttp import ClientSession
from discord.ext import commands 


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        choices = ("Tails", "Heads")
        rancoin = random.choice(choices)
        await ctx.send(rancoin)

    @commands.command()
    async def about(self, ctx):
      aboutembed = discord.Embed(title="About", description=f"Bot made by Supelion#0001 as a side project and as a introduction to python. I am currently in ``{len(self.client.guilds)}`` servers and getting used by ``{len(self.client.users)}`` users!", color=discord.Color.blue())
      aboutembed.set_footer(text="SupeBot v1.1 | Supelion#0001")
      await ctx.send(embed=aboutembed)

    @commands.command()
    async def stats(self, ctx):
      statsembed = discord.Embed(title="Bot Stats", description = "SupeBot's stats", color=discord.Color.blue())
      statsembed.add_field(name = f"Users:", value = f"```python\n{len(self.client.users)}```", inline = False)
      statsembed.add_field(name = f"Guilds:", value = f"```python\n{len(self.client.guilds)}```", inline = False)
      statsembed.set_footer(text="SupeBot v1.1 | Supelion#0001")
      await ctx.send(embed=statsembed)

    @commands.command(
      aliases = ["reminder", "remindme"]
    )
    async def remind(self, ctx, time:int, *, msg):
      await ctx.message.delete()
      await ctx.send(f"{ctx.author.mention} You will be sent a reminder in ``{time} minutes`` to: ``{msg}``\n||Please note, if the bot goes offline, you will not be sent a reminder!||")
      
      
      while True:
        await s(60*time)
        await ctx.send(f'{msg}, {ctx.author.mention}')
        await ctx.message.delete()
        return

    @commands.command()
    async def support(self, ctx):
      serverembed = discord.Embed(title="Support Server.", description="SupeBot Support Server: https://discord.gg/CUwrDgCB4W", color=discord.Color.blue())
      await ctx.send(embed=serverembed)
    
    @commands.command()
    async def affirm(self, ctx):
      affirmationlmfao = requests.get("https://dulce-affirmations-api.herokuapp.com/affirmation")
      affirmationjson = affirmationlmfao.json()
      affirmation = affirmationjson["phrase"]

      affirmationembed = discord.Embed(title = "Need a affirmation?")
      affirmationembed.add_field(name = "Here's one: ", value = f"{affirmation}")
      affirmationembed.set_footer(text = f"Made with ♥ by Supelion#0001")
      await ctx.send(embed = affirmationembed)

    @commands.command(
      aliases = ["doggo"]
    )
    async def dogpic(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
          res = await r.json()
          r3s = res['message']

      dogembed = discord.Embed(title = 'Dog Image!', color = ctx.author.color)
      dogembed.set_image(url=f"{r3s}")
      await ctx.send(embed=dogembed)

    @commands.command()
    async def bored(self, ctx):
          async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.boredapi.com/api/activity') as r:
              activitything = await r.json()
              activity1 = activitything["activity"]

          boredembed = discord.Embed(title = 'Are you bored?')
          boredembed.add_field(name = 'Try:', value = f"{activity1}")
          await ctx.send(embed=boredembed)

    @commands.command(
        aliases=['pfp']
    )
    async def avatar(self, ctx, member: discord.Member = None):

        if member is None:
            await ctx.send("You seem lost, did you mean to do ``.pfp <member>``?")
            return

        else:
            pfpembed = discord.Embed(title="User's Avatar:", color = ctx.author.color)
            pfpembed.set_image(url=member.avatar_url)
            await ctx.send(embed=pfpembed)
      
    @commands.command()
    async def ping(self, ctx):
      await ctx.send(f'{round(self.client.latency*1000)} ms')

    @commands.command()
    async def src(self, ctx):
      srcembed = discord.Embed(title="Source Code", url="https://github.com/Supelion/SupeBot/releases", description="SupeBot's SRC can be found on GitHub by clicking the title of this embed.", color=discord.Color.blue())
      await ctx.send(embed=srcembed)
        
    @commands.Cog.listener()
    async def on_command(self, ctx):
      channel = self.client.get_channel(844647290291224607)
      await channel.send(f"Command ({ctx.command}) was executed by {ctx.author.name}#{ctx.author.discriminator} in guild '{ctx.guild.name}'")

    @commands.command(aliases= ['8ball', '8b'])
    async def eightball(self, ctx, *, question):
        responses = ["No.",
                    "Not at ALL.",
                    "Nope.",
                    "Yeah yeah no.",
                    "Yes.",
                    "For the last time, YES.",
                    "Idk man :grimacing:",
                    "Bro...",
                    "Lol, yeah.",
                    "YESSIR!",
                    "You must be stupid to think otherwise!",
                    "Yes, ofcourse!",
                    "Yup."]
        await ctx.send(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}")

    @commands.command()
    async def invite(self, ctx):
      invitembed = discord.Embed(color = discord.Color.blue())
      invitembed.add_field(name=f"Invite Link :link:", value = "https://discord.com/api/oauth2/authorize?client_id=835237831412547607&permissions=268762199&scope=bot")
      await ctx.send(embed=invitembed)

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://memes.blademaker.tv/api?lang=en') as r:
            memejson = await r.json()
            title = memejson["title"]
            auth = memejson["author"]
            sub = memejson["subreddit"]
        
        memeembed = discord.Embed(title = f"{title}", color=discord.Color.blue())
        memeembed.set_footer(text=f"Subreddit: {sub} | Author: {auth}")
        memeembed.set_image(url = memejson["image"])
        await ctx.send(embed=memeembed)

    @commands.command(
        aliases=['dadjokes', 'joke']
    )
    async def dadjoke(self, ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': "fcd928e39dmsh8b6706ff61a7661p1d1e02jsn94f1b9f21ad7"
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")

    @commands.command(
      aliases = ["id", "identity"]
    )
    async def fakeid(self, ctx):
      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.namefake.com') as fakeidraw:
            fakeidjson = await fakeidraw.text()
            fakeidjson = json.loads(fakeidjson)
            name = fakeidjson["name"]
            address = fakeidjson["address"]
            birth_date = fakeidjson["birth_data"]
            ip_adress = fakeidjson["ipv4"]
            mac_adress = fakeidjson["macaddress"]
            email_1 = fakeidjson["email_u"]
            email_2 = fakeidjson["email_d"]
            email_3 = f'{email_1}@{email_2}'
            company = fakeidjson["company"]
            idembed  = discord.Embed(title = "Fake ID Generator", color=0x2f3136)
            idembed.add_field(name = "Name:", value = f'``{name}``', inline = False)
            idembed.add_field(name = "Address:", value = f'``{address}``', inline = False)
            idembed.add_field(name = "Date of Birth", value = f'``{birth_date}``', inline = False)
            idembed.add_field(name = "IP:", value = f'``{ip_adress}``', inline = False)
            idembed.add_field(name = "MAC:", value = f'``{mac_adress}``', inline = False)
            idembed.add_field(name = "Email:", value = f'``{email_3}``', inline = False)
            idembed.add_field(name = "Email Access:", value = f'``https:{fakeidjson["email_url"]}``', inline = False)
            idembed.add_field(name = "Company:", value = f'``{company}``', inline = False)
            await ctx.send(embed=idembed)

  
def setup(client):
    client.add_cog(Misc(client))