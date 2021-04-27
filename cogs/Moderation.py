import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

@commands.command()
@commands.has_permissions(administrator=True)
async def kick(self, ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Pls specify a member lololololol")
        return
    await member.kick()
    await ctx.send(f"LMFAO {member.mention} got kicked, L.")
@kick.error
async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You are not allowed to kick people noob", delete_after = 3)
 
@commands.command()
@commands.has_permissions(administrator=True)
async def ban(self, ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Pls specify a member lololololol")
        return
    await member.ban()
    await ctx.send(f"LMFAO {member.mention}  got banned, L.")
@ban.error
async def ban_error(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people noob", delete_after = 3)

def setup(client):
  client.add_cog(Moderation(client))