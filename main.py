import discord
import os
import asyncio
import json
from datetime import datetime
from itertools import cycle
import os
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', help_command=None,intents=intents)
client.launch_time = datetime.utcnow()

page1 = discord.Embed(title="Minecraft", description=".bw | .sw | .p | .server", 
colour=discord.Colour.orange())
page1.set_footer(text = "Note: You get timed out after 20 seconds.")

page2 = discord.Embed(title="Utility", description=".about | .src | .ping | .support | .invite | .stats", colour=discord.Colour.orange())
page2.set_footer(text = "Note: You get timed out after 20 seconds.")


help_pages = [page1, page2]

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')

@client.event
async def on_ready():
    print("I'm ready lol.")


@tasks.loop(minutes=2)
async def changer():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name=next(client.status)))


status1 = f"Best bot ww! | .help"
status2 = f"Hypixel Stats! | .help"
status3 = f"Doggo Pictures! | .help"
status4 = f"Crypto Stats! | .help"
status5 = f"Memes! | .help"
status6 = f"Dadjokes! 😒 | .help"
status7 = f"Open Source! | .help"
status8 = f"Website now live! supebot.ddns.net 🎉| .help"
client.status = cycle([status1, status2, status3, status4, status5,status6,status7, status8])
changer.start()
    
@client.event
async def on_message(message):
    if message.guild.me in message.mentions:
        await message.channel.send("Do ``.help``!")
    await client.process_commands(message)

@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    uptimeembed = discord.Embed(title = "")
    uptimeembed.add_field(name = "Uptime:", value = f"{days}d, {hours}h, {minutes}m, {seconds}s since last restart.")
    await ctx.send(embed=uptimeembed)

@client.command()
async def help(ctx):
    buttons = [u"\u2B05", u"\u27A1"] 
    current = 0
    msg = await ctx.send(embed=help_pages[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=20.0)

        except asyncio.TimeoutError:
          pass

        else:
            previous_page = current
                
            if reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=help_pages[current])


client.run(f"{token}")