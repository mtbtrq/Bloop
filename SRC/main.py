import os
import json

from datetime import datetime
from itertools import cycle

import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!', case_insensitive = True, help_command=None, intents=intents)
client.launch_time = datetime.utcnow()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')

@client.event
async def on_ready():
    user = client.get_user(467962329435471878)
    await user.send("I'm online. <:online:850325400605425684>")
    print(f"I'm ready!")

@tasks.loop(minutes=5)
async def changer():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name=next(client.status)))

status1 = f"Best bot ww! | .help"
status2 = f"Hypixel Stats! | .help"
status3 = f"Open Source! (.src)| .help"
status4 = f"Server Stats! | .help"
status5 = f"DLCs! | .help"
client.status = cycle([status1, status2, status3, status4, status5])
changer.start()

@client.command()
async def stats(ctx):

    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    
    statsembed = discord.Embed(title="Bloop's Stats", color = 0x2f3136)
    
    statsembed.add_field(name = f"Language:", value = f"Python 3.9  <:python:848989130808754196>", inline = False)
    
    statsembed.add_field(name = f"Users:", value = f"{len(client.users):,}", inline = False)
    
    statsembed.add_field(name = f"Guilds:", value = f"{len(client.guilds)}", inline = False)

    statsembed.add_field(name = f"Uptime:", value = f"{hours}h, {minutes}m, {seconds}s.\n\n[Support Website](bitl.ly/bloopBot)", inline = False)
    
    statsembed.set_footer(text="Bloop v2.3 | Supelion#4275")
    
    await ctx.reply(embed=statsembed, mention_author=False)
    print("The Stats Command was executed!")

@client.command()
async def help(ctx):
    
    helpembed = discord.Embed(title='Help', color = 0x2f3136)
        
    helpembed.add_field(name = "My Prefix:", value = "``.``")
        
    helpembed.add_field(name='<:minecraft:848988105943810095> Minecraft', value='``bw`` • ``sw`` • ``duels`` • ``profile`` • ``wdr`` • ``server``\n\n``socials`` • ``skin`` • ``p`` • ``uuid`` • ``compare``\n\n``achievement``', inline=False)

    helpembed.add_field(name='<:misc:844235406877917234> Utility', value='``src`` • ``ping`` • ``invite`` • ``stats`` • ``suggest``', inline=False)

    helpembed.set_thumbnail(url='https://media.discordapp.net/attachments/8350712o70117834773/853578246984433684/lol.png?width=480&height=480')

    helpembed.set_footer(text="Bloop v2.3 | Supelion#4275")

    await ctx.reply(embed=helpembed, mention_author = False)
    print("The Help Command was executed!")


client.run(f"{token}")