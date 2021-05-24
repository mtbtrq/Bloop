import discord
import os
import json
from itertools import cycle
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', help_command=None,intents=intents)
client.sniped_messages = {}

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')

@client.event
async def on_ready():
    print("I'm ready lol.")


@tasks.loop(seconds=15)
async def changer():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name=next(client.status)))


status1 = f"Best bot ww! | !help"
status2 = f"Hypixel Stats! | !help"
status3 = f"Doggo Pictures! | !help"
status4 = f"Crypto Stats! | !help"
status5 = f"Memes! | !help"
status6 = f"Dadjokes! 😒 | !help"
status7 = f"Nitro Giveaway!! 🥳🎊🎉 (DM Supelion#0001) | !help"
status8 = f"Open Source. | !help"
client.status = cycle([status1, status2, status3, status4, status5,status6,status7])
changer.start()
    
@client.event
async def on_message(message):
    if message.guild.me in message.mentions:
        await message.channel.send("Do ``.help``!")
    await client.process_commands(message)

@client.group(invoke_without_command=True)
async def help(ctx):
    helpembed = discord.Embed(
        title='Help', description='Made with <3 by Supelion.', color=discord.Color.blue())

    helpembed.add_field(
        name='<:hypixel:844234115984130078> Hypixel', value='``.bw; .sw; .karma; .nwlevel``', inline=False)
    helpembed.add_field(
        name='<:crypto:844234812331524117> Crypto', value='``.btc ; .eth; .doge; .bat; .ada``', inline=False)
    helpembed.add_field(
        name='<:misc:844235406877917234> Misc', value='``.about; .src; .support; .ping; .invite; .affirm``', inline=False)
    helpembed.add_field(
        name='<a:813111549941252126:844446604043878410> Fun', value='``.meme; .dadjoke; .coinflip; .8b; .avatar; .bored; .doggo``', inline=False)
    helpembed.add_field(
        name=':full_moon: Astronomy', value='``.apod``', inline=False)
    helpembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835071270117834773/844229169863983154/logo.PNG')
    helpembed.set_footer(text="SupeBot v0.9 | Supelion#0001")

    await ctx.send(embed=helpembed)


client.run(f"ODM2NjU1MTEyMDIxMjEzMjI0.YIhJyw.OqyrfFdxyKGEz-vs3r8tMUUXlsY")