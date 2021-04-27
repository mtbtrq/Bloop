import discord
import json
from asyncio import sleep
import pprint
import os
import cogs
from discord.ext import commands

client = commands.Bot(command_prefix='.', help_command=None)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('.help for help'))
    print('Ready.')


TOKEN = 'INSERT TOKEN HERE'


@client.command()
async def ping(ctx):

    await ctx.send(f'{round(client.latency*1000)} ms')


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title='Help', description='Made with <3 by Supelion.', color=ctx.author.color)

    em.add_field(
        name='Duels', value='.duelskills <IGN>; .duelswins <IGN>; .duelskdr <IGN> ; .duelswlr <IGN>', inline=True)
    em.add_field(
        name='BedWars', value='.bwfkdr <IGN> ; .bwlvl <IGN>; .bwwins <IGN>; .bwwlr <IGN>', inline=True)
    em.add_field(
        name='Misc', value='.nwlevel <IGN> ; .karma <IGN>; .coinflip; .about; .src', inline=True)
    em.add_field(name='Moderation', value='.kick ; .ban; .ping;', inline=True)
    em.set_thumbnail(
      url='https://media.discordapp.net/attachments/835818650916487180/835837071771041822/5.png?width=480&height=480')

    await ctx.send(embed=em)


client.run(TOKEN)