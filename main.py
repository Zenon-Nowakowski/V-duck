# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
from internal import token

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.
The command prefix is `:V ` (including the white space after :V).
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=':V ', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

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
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    await ctx.message.delete()

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
    await ctx.message.delete()

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def echo(ctx, *, content):
    await ctx.send(content)
    await ctx.message.delete()

bot.run(token)