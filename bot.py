import discord
import json
from asyncio import sleep
import pprint
from webserver import keep_alive
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
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help for help'))
    print('Am Ready, lololololooololololololoolololololollolol.')


TOKEN = 'INSERT TOKEN HERE'


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (
        message.content, message.author, message.channel.name, message.created_at)


@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents,
                          color=discord.Color.purple(), timestamp=time)
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)


@client.command()
async def ping(ctx):

    await ctx.send(f'{round(client.latency*1000)} ms')


@client.group(invoke_without_command=True)
async def help(ctx):
    helpembed = discord.Embed(
        title='Help', description='Made with <3 by Supelion.', color=ctx.author.color)

    helpembed.add_field(
        name='Duels', value='.duelskills <IGN>; .duelswins <IGN>; .duelskdr <IGN> ; .duelswlr <IGN>', inline=True)
    helpembed.add_field(
        name='BedWars', value='.bwfkdr <IGN> ; .bwlvl <IGN>; .bwwins <IGN>; .bwwlr <IGN>', inline=True)
    helpembed.add_field(
        name='Misc', value='.nwlevel <IGN> ; .karma <IGN>; .coinflip; .about; .src; .snipe; .dadjoke', inline=True)
    helpembed.add_field(name='Moderation', value='.kick ; .ban; .ping;', inline=True)
    helpembed.set_thumbnail(
      url='https://media.discordapp.net/attachments/835818650916487180/835837071771041822/5.png?width=480&height=480')

    await ctx.send(embed=helpembed)


keep_alive()
client.run(TOKEN)
