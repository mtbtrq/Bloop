import discord
import traceback
import sys
from discord.ext import commands
import json
from datetime import datetime

with open('./config.json') as jsonload:
  config = json.load(jsonload)

noCoolDownUsers = config.get("noCoolDownUsers")

now = datetime.now()

logFileName = f"./logs - {now.strftime('%H ; %M ; %S')}.txt"

print(f"Logging commands to {logFileName}")

class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        logs = open(logFileName, "a")
        logs.write(f"\n'{ctx.command}' was executed in '{ctx.guild.name}' (ID: {ctx.guild.id}) by {ctx.author} (ID: {ctx.author.id}) at {datetime.utcnow()} UTC")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                errorembed = discord.Embed(title = 'An Error Occured!')
                errorembed.add_field(name = 'Cause:', value = f"You cannot use this command in DMs!")
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send("I dont have permission to do that", delete_after=8)

        elif isinstance(error, commands.errors.NotOwner):
            errorembed = discord.Embed(title = 'An Error Occured!')
            errorembed.add_field(name = 'Cause:', value = f"You are not the owner of this bot!")
            errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
            await ctx.send(embed = errorembed)

        elif isinstance(error, discord.ext.commands.CommandOnCooldown):
            if ctx.author.id not in noCoolDownUsers:
                errorembed = discord.Embed(title = 'An Error Occured!')
                errorembed.add_field(name = 'Cause:', value = f"You are on cooldown, please try again in `{error.retry_after:.2f}`!")
                errorembed.set_thumbnail(url = "https://media.discordapp.net/attachments/835071270117834773/856907114517626900/error.png")
                await ctx.send(embed = errorembed)
            else:
                await ctx.reinvoke()

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))