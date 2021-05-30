import discord
from discord.ext import commands


class ErrorHandling(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error, *, from_local=False):
        if hasattr(ctx.command, "on_error") and not from_local:
            return
        error = getattr(error, "original", error)

        if isinstance(error, discord.ext.commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown, please try again in `{error.retry_after:.2f}` seconds.")

def setup(bot):
    bot.add_cog(ErrorHandling())