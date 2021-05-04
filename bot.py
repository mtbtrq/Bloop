import discord
import json
from asyncio import sleep
import pprint
import aiohttp
import random
import requests
import os
import cogs
from discord.ext import commands

client = commands.Bot(command_prefix='.', help_command=None)
client.sniped_messages = {}

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"on {len(client.guilds)} servers | .help"))
    print("I'm ready lololololololololololol.")


TOKEN = 'INSERT TOKEN HERE'


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (
        message.content, message.author, message.channel.name, message.created_at)
    await client.process_commands(message)

@client.command()
async def meme(ctx):
    r = requests.get("https://memes.blademaker.tv/api?lang=en")
    res = r.json()
    title = res["title"]
    sub = res["subreddit"]
    memeembed = discord.Embed(title = f"{title}", color=discord.Color.blue())
    memeembed.set_footer(text=f"Subreddit: {sub}")
    memeembed.set_image(url = res["image"])
    await ctx.send(embed=memeembed)

@client.command(aliases= ['8ball', '8b'])
async def eightball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "is that even a question? yeah idiot.",
                "Yes - definitely.",
                "You may rely on it.",
                "lmao ofc lol",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "for the last time, YES.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "ofc not lol.",
                "My sources say no.",
                "doesnt seem like it tbh lol",
                "Very doubtful."]
    await ctx.send(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}")

@client.event
async def on_message(message):
    if message.guild.me in message.mentions:
        await message.channel.send("Pls dont unecessarily pong me :c, it's .help to get help.")
    await client.process_commands(message)

@client.command()
async def snipe(ctx, message):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents,
                          color=discord.Color.blue(), timestamp=time)
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)
    await client.process_commands(message)


@client.command()
async def ping(ctx):

    await ctx.send(f'{round(client.latency*1000)} ms')


@client.group(invoke_without_command=True)
async def help(ctx):
    helpembed = discord.Embed(
        title='Help', description='Made with <3 by Supelion.', color=discord.Color.blue())

    helpembed.add_field(
        name=':video_game: Hypixel', value='``.bw``', inline=True)
    helpembed.add_field(
        name=':gear: Misc', value='``.coinflip; .about; .src; .snipe; .discord; .dadjoke; .meme; .ping``', inline=True)
    helpembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/836614888080015381/837749892382326834/logo.png')

    await ctx.send(embed=helpembed)


client.run(TOKEN)