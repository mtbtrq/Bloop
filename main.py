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
status3 = f"Open Source! | .help"
status4 = f"Website now live! supebot.ddns.net 🎉| .help"
client.status = cycle([status1, status2, status3, status4])
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

@client.group(invoke_without_command=True)
async def help(ctx):
    helpembed = discord.Embed(
        title='Help', description='Made with <3 by Supelion.', color=discord.Color.blue())

    helpembed.add_field(
        name='<:hypixel:844234115984130078> Hypixel', value='``.bw | .sw | .profile | .server``', inline=False)
    helpembed.add_field(
        name='<:misc:844235406877917234> Utility', value='``.about | .src | .support | .ping | .invite | .stats | .uptime``', inline=False)
    helpembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835071270117834773/844229169863983154/logo.PNG')
    helpembed.set_footer(text="SupeBot v1.1 | Supelion#0001")

    await ctx.send(embed=helpembed)


client.run(f"{token}")