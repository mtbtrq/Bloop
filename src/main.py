import os

try:
    import json
    from datetime import datetime
    from itertools import cycle
    import discord
    from discord.ext import commands, tasks
    import platform
    import PIL # I know, we're not using this module right now, but its for the try except statement

except ImportError:
    print("One or many requirements are missing! Installing them now.")
    os.system("pip3 install -r requirements.txt")
    print("Done!")

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
botLogChannel = config.get('bot-log-channel')
prefix = config.get('prefix')

os.system("cls")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = prefix, case_insensitive = True, help_command=None, intents=intents)

launch_time = datetime.utcnow()

botVersion = "Bloop v2.7"

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    user = client.get_user(467962329435471878)
    await user.send("I'm online. <:online:850325400605425684>")
    print(f"I have logged in as {client.user}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()}")
    
@client.command()
async def reload(ctx, *, module):
    try:
        client.reload_extension(module)
        await ctx.send("Done!")
    except commands.ExtensionError as e:
        await ctx.send(f'{e.__class__.__name__}: {e}')

@client.event
async def on_guild_remove(guild):
    channel = client.get_channel(botLogChannel)
    await channel.send(f"I got removed from `{guild.name}`, which is owned by `{guild.owner}`. I am now in {len(client.guilds)} servers.")

@client.event
async def on_guild_join(guild):
    channel = client.get_channel(botLogChannel)
    await channel.send(f"I got added to the guild `{guild.name}`, which is owned by `{guild.owner}`. I am now in {len(client.guilds)} servers.")

@tasks.loop(minutes=5)
async def changer():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name=next(client.status)))

status1 = f"Best bot ww! | .help"
status2 = f"Hypixel Stats! | .help"
status3 = f"Open Source! (.src)| .help"
status4 = f"Server Stats! | .help"
status5 = f"Map Information! | .help"
status6 = f"Requeue Checker! | .help"
status7 = f"Stats Comparer! | .help"
status8 = f"Watchdog Stats! | .help"
client.status = cycle([status1, status2, status3, status4, status5, status6])
changer.start()

@client.command()
async def stats(ctx):

    delta_uptime = datetime.utcnow() - launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    
    statsembed = discord.Embed(title="Bloop's Stats", color = 0x2f3136)
    
    statsembed.add_field(name = f"Language:", value = f"Python 3.9  <:python:848989130808754196>", inline = False)
    
    statsembed.add_field(name = f"Users:", value = f"{len(client.users):,}", inline = False)
    
    statsembed.add_field(name = f"Guilds:", value = f"{len(client.guilds)}", inline = False)

    statsembed.add_field(name = f"Uptime:", value = f"{days}d {hours}h, {minutes}m, {seconds}s.\n\n[Support Website](https://supelion.github.io/bl00p/)", inline = False)
    
    statsembed.set_footer(text=f"{botVersion} | Supelion#4275")
    
    await ctx.reply(embed=statsembed, mention_author=False)

@client.command()
async def help(ctx):
    
    helpembed = discord.Embed(title='Help', color = 0x2f3136)
        
    helpembed.add_field(name = "My Prefix:", value = "``.``")
        
    helpembed.add_field(name='<:minecraft:848988105943810095> Minecraft', value='``bw`` • ``sw`` • ``duels`` • ``profile`` • ``wdr`` • ``server``\n\n``socials`` • ``skin`` • ``p`` • ``uuid`` • ``compare``\n\n``achievement`` • ``map`` • ``requeue`` • ``key``', inline=False)

    helpembed.add_field(name='<:utility:877105943844904980> Utility', value='``src`` • ``ping`` • ``invite`` • ``stats`` • ``suggest``', inline=False)

    helpembed.set_thumbnail(url='https://media.discordapp.net/attachments/8350712o70117834773/853578246984433684/lol.png?width=480&height=480')

    helpembed.set_footer(text=f"{botVersion} | Supelion#4275 | All Commmands work in DMs.")

    await ctx.reply(embed=helpembed, mention_author = False)

client.run(f"{token}")