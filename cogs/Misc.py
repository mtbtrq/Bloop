import discord
import random
import requests
import aiohttp
import asyncio
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
      aboutembed = discord.Embed(title="About", description=f"Bot made by Supelion#0001 as a side project and as a introduction to python. I am currently in ``{len(self.client.guilds)}`` servers", color=discord.Color.blue())
      aboutembed.set_footer(text="SupeBot v1.0 | Supelion#0001")
      await ctx.send(embed=aboutembed)

    @commands.command()
    async def support(self, ctx):
      serverembed = discord.Embed(title="Support Server.", description="SupeBot Support Server: https://discord.gg/CUwrDgCB4W", color=discord.Color.blue())
      await ctx.send(embed=serverembed)

    @commands.command()
    async def affirm(self, ctx):
      async with aiohttp.ClientSession() as cs:
         with cs.get('https://www.affirmations.devn') as affirmthing:
          res = await affirmthing.json()  
          affirmation = (res['affirmation'])

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

    @commands.command()
    async def apod(self, ctx):
      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://api.nasa.gov/planetary/apod?api_key=rmYhg5SgkCLJl2jKpHWhkaBUPz3AAqyBcZHKyKDx') as r:
            ap0d = await r.json()
            apod = ap0d["hdurl"]
      
      apodembed = discord.Embed(title = f"Nasa's APOD:")
      apodembed.set_image(url = f"{apod}")
      apodembed.set_footer(text = f"APOD = Astronomy Picture of the Day")
      await ctx.send(embed=apodembed)

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
    @commands.cooldown(1, 10,commands.BucketType.user)
    async def nitro(self, ctx):
      await ctx.send(f"{ctx.author.mention}, you have entered the ``Discord Nitro Classic for 1 month`` giveaway! <:horriblydrawnnitroclassic:844645205431812097> <:nitro:844646006028632074>")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        cooldownmessage = f"{ctx.author.mention} **You can only use this command every ``10`` seconds!**"
        await ctx.send(cooldownmessage, delete_after = 3)

    @commands.command()
    async def src(self, ctx):
      srcembed = discord.Embed(title="Source Code", url="https://github.com/Supelion/SupeBot/releases", description="SupeBot's SRC (up until 0.7) can be found on GitHub by clicking the title of this embed.", color=discord.Color.blue())
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
            idembed  = discord.Embed(title = "Fake ID Generator")
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