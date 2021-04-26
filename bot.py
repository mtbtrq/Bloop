import discord
import json
import math
from asyncio import sleep
import random
import requests
import pprint
import os
import cogs
from discord.ext import commands

client = commands.Bot(command_prefix= '.', help_command=None)

async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

TOKEN = 'INSERT TOKEN HERE'


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('.help for help'))
  print('Ready.')

def add(n: float, n2: float):
	return n + n2

def sub(n: float, n2: float):
	return n - n2

def div(n: float, n2: float):
	return n / n2

def sqrt(n: float):
	return math.sqrt(n)

def mult(n: float, n2: float):
	return n * n2

@client.command()
async def mathadd(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathdiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathmult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass

@client.command()
async def ping(ctx):

    await ctx.send(f'{round(client.latency*1000)} ms')

@client.group(invoke_without_command=True)
async def help(ctx):
    em= discord.Embed(title='Help', description='Made with <3 by Supelion.',color = ctx.author.color)

    em.add_field(name='Duels', value= '.duelskills <IGN>; .duelswins <IGN>; .duelskdr <IGN> ; .duelswlr <IGN>', inline=True)
    em.add_field(name='BedWars', value= '.bwfkdr <IGN> ; .bwlvl <IGN>; .bwwins <IGN>; .bwwlr <IGN>', inline=True)
    em.add_field(name='Maths', value= '.mathadd ; .mathsub; .mathdiv; .mathmult; .mathsqrt', inline=True)
    em.add_field(name='Misc', value= '.nwlevel <IGN> ; .karma <IGN>; .coinflip; .about', inline=True)
    em.add_field(name='Moderation', value= '.kick ; .ban; .ping;', inline=True)
    em.set_thumbnail(url='https://media.discordapp.net/attachments/835818650916487180/835837071771041822/5.png?width=480&height=480')


    await ctx.send(embed=em)

@client.command()
async def coinflip(ctx):
  choices = ("Tails", "Heads")
  rancoin = random.choice(choices)
  await ctx.send(rancoin)

@client.command()
async def about(ctx):

  await ctx.send("Bot made by Supelion#4292 as a side project and as a introduction to python :D")

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Pls specify a member lololololol")
        return
    await member.kick()
    await ctx.send(f"LMFAO {member.mention} got kicked, L.")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people noob")
 
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Pls specify a member lololololol")
        return
    await member.ban()
    await ctx.send(f"LMFAO {member.mention}  got banned, L.")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people noob")
    
client.run(TOKEN)