import os

try:
    import json
    from datetime import datetime
    from itertools import cycle
    import asyncpg
    import discord
    from discord.ext import commands, tasks
    import PIL # I know, we're not usig this module right now, but its for the try except statement

except ImportError:
    print("One or many requirements are missing! Installing them now.")
    os.system("pip3 install -r requirements.txt")
    print("Done!")

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
postgresDatabaseDSN = config.get('postgresDSN')
botLogChannel = config.get('bot-log-channel')

os.system("cls")

async def create_db_pool():
    client.db = await asyncpg.create_pool(dsn = postgresDatabaseDSN)
    print("Connected to the DB!")

    await client.db.execute("CREATE TABLE IF NOT EXISTS prefixes(guild_id bigint PRIMARY KEY, prefix text);")
    print("Created Table")

PRE = '.'
async def get_pre(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(PRE)(bot,message)
    prefix = await client.db.fetchval('SELECT prefix FROM prefixes WHERE guild_id = $1', message.guild.id)
    if not prefix:
        prefix = PRE
    return commands.when_mentioned_or(prefix)(bot,message)

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = get_pre, case_insensitive = True, help_command=None, intents=intents)
client.launch_time = datetime.utcnow()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    user = client.get_user(467962329435471878)
    await user.send("I'm online. <:online:850325400605425684>")
    print(f"I'm ready! I have logged in as {client.user}")

@client.command()
async def elmne(ctx):
    embed = discord.Embed(title = "Good Job.")
    embed.add_field(name = "Next Step", value = "Subscribe to Supelion on YouTube with an account that has subscriptions public. Once you have done that, DM Supelion of that screenshot and he will DM you your next hint.")
    embed.set_footer(text = "If you unsubscribe in the future, you will be banned from future events.")
    await ctx.send(embed = embed)

@client.command()
async def fghrei(ctx):
    embed = discord.Embed(title = "Good Job.")
    embed.add_field(name = "Next Step", value = "Z29vZCBqb2IgbWFraW5nIGl0IHRoaXMgZmFyLCBub3csIGV4ZWN1dGUgdGhpcyBjb21tYW5kOiBoaWps")
    embed.set_footer(text = "Decode the text!")
    await ctx.send(embed = embed)

@client.command()
async def hijl(ctx):
    embed = discord.Embed(title = "Good Job.")
    embed.add_field(name = "Next Step", value = "Check Supelion's Socials for a command.")
    embed.set_footer(text = "This one might not be so easy, so good luck!")
    await ctx.send(embed = embed)

@client.command()
async def lolIwon(ctx):
    embed = discord.Embed(title = "GG.")
    embed.add_field(name = "You won!", value = "DM Supelion#4275 to claim your prize!")
    await ctx.send(embed = embed)
    print(f"{ctx.author} won the giveaway!")
    
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
status5 = f"DLCs! | .help"
client.status = cycle([status1, status2, status3, status4, status5])
changer.start()

@client.command()
@commands.has_permissions(manage_guild = True)
@commands.cooldown(1, 50,commands.BucketType.guild)
async def prefix(ctx, new=None):
    old = await client.db.fetchval('SELECT prefix FROM prefixes WHERE guild_id = $1', ctx.guild.id)
    if not new:
        old = old or '.'
        await ctx.send(f"My prefix here is: `{old}`")
        return

    if len(new) > 10:
        return await ctx.send("Prefixes must be no longer than 10 characters long!")
    if not old:
        await client.db.execute('INSERT INTO prefixes(guild_id, prefix) VALUES ($1, $2)', ctx.guild.id, new)
    else:
        await client.db.execute('UPDATE prefixes SET prefix = $1 WHERE guild_id = $2', new, ctx.guild.id)
    await ctx.send(f"The new prefix is: `{new}`")

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

    statsembed.add_field(name = f"Uptime:", value = f"{hours}h, {minutes}m, {seconds}s.\n\n[Support Website](https://supelion.github.io/bl00p/)", inline = False)
    
    statsembed.set_footer(text="Bloop v2.4 | Supelion#4275")
    
    await ctx.reply(embed=statsembed, mention_author=False)
    print("The Stats Command was executed!")

@client.command()
async def help(ctx):
    
    helpembed = discord.Embed(title='Help', color = 0x2f3136)
        
    helpembed.add_field(name = "My Prefix:", value = "``.``")
        
    helpembed.add_field(name='<:minecraft:848988105943810095> Minecraft', value='``bw`` • ``sw`` • ``duels`` • ``profile`` • ``wdr`` • ``server``\n\n``socials`` • ``skin`` • ``p`` • ``uuid`` • ``compare``\n\n``achievement``', inline=False)

    helpembed.add_field(name='<:misc:844235406877917234> Utility', value='``src`` • ``ping`` • ``invite`` • ``stats`` • ``suggest`` • ``prefix``', inline=False)

    helpembed.set_thumbnail(url='https://media.discordapp.net/attachments/8350712o70117834773/853578246984433684/lol.png?width=480&height=480')

    helpembed.set_footer(text="Bloop v2.4 | Supelion#4275 | All Commmands work in DMs.")

    await ctx.reply(embed=helpembed, mention_author = False)
    print("The Help Command was executed!")

client.loop.run_until_complete(create_db_pool())
client.run(f"{token}")