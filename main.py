import discord
import os
import json
from datetime import datetime
from itertools import cycle
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', help_command=None,intents=intents)
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


@tasks.loop(minutes=5)
async def changer():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name=next(client.status)))


status1 = f"Best bot ww! | .help"
status2 = f"Hypixel Stats! | .help"
status3 = f"Open Source! (.src)| .help"
status4 = f"Website now live! supebot.ddns.net 🎉| .help"
status5 = f"Server Stats! | .help"
status6 = f"DLCs! | .help"
client.status = cycle([status1, status2, status3, status4, status5, status6])
changer.start()
    
@client.event
async def on_message(message):
    if message.guild.me in message.mentions:
        await message.channel.send("Seems like you're lost. Do ``.help``!")
    await client.process_commands(message)

@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    uptimeembed = discord.Embed(color = 0x2f3136)
    uptimeembed.add_field(name = "Uptime:", value = f"{days}d, {hours}h, {minutes}m, {seconds}s since last restart.")
    await ctx.reply(embed=uptimeembed, mention_author = False)

@client.group(invoke_without_command=True)
async def help(ctx):
    helpembed = discord.Embed(
        title='Help', description='Made with <3 by Supelion.', color=discord.Color.blue())
    
    helpembed.add_field(name = "My Prefix:", value = "``.``")
    
    helpembed.add_field(
        name='<:minecraft:848988105943810095> Minecraft', value='``bw``, ``sw``, ``duels``, ``profile``, ``wdr``, ``server``,  ``socials``, ``skin``', inline=False)
    helpembed.add_field(
        name='<:misc:844235406877917234> Utility', value='``src``, ``support``, ``ping``, ``invite``, ``stats``, ``uptime``, ``downloads``', inline=False)
    helpembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/8350712o70117834773/853578246984433684/lol.png?width=480&height=480')
    helpembed.set_footer(text="Bloop v1.7 | Supelion#4275")

    await ctx.reply(embed=helpembed, mention_author = False)


client.run(f"{token}")