import discord
from discord.ext import commands
import random

# File manipulation
import json 

# Generics 
import string
import datetime
import os
import random

class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @bot.command()
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)
        await ctx.message.delete()

    @bot.command()
    async def roll(ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('That is not a dice format! (NdN)')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)
        await ctx.message.delete()

    @bot.command()
    async def choose(ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))
        await ctx.message.delete()

    @bot.command()
    async def echo(ctx, *, content):
        '''basic echo command, by use of admins only'''
        await ctx.send(content)
        await ctx.message.delete()