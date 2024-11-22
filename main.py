# This example requires the 'members' and 'message_content' privileged intents to function.

#Discord imports 
import discord
from discord.ext import commands
import random
# File manipulation
import json 
# Generics 
import string
import datetime
import os
#other
from src.FilterAlgorithm import FilterAlgorithm
#init the bot
description = '''This is V-duck, a silly discord bot. 
The command prefix is `:V ` (including the white space after :V).
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=[':V ',':v ', ':V',':v'], description=description, intents=intents)

# load in json file 
# import internals from json
with open('config/config.json') as jsonFile:
    data = json.load(jsonFile)
    token = data['token']
    FilteredStrings = data['FilteredStrings']
# also import copypasta.json
pastas = open('config/copypasta.json', 'r')

#bot events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # this await ensures that the bot will wait and thus be able to continue processing commands
    await bot.process_commands(message)
    # if the message is from the bot, ignore it
    if message.author == bot.user:
        return
    # preset the timeout time (5 seconds)
    duration = datetime.timedelta(seconds=5)
    # Convert the message to lowercase and remove punctuation, then check if it contains any of the filtered strings
    # scan the message word by word to see if the message contains any of the filtered strings
    msg = message.content.lower()
    msg = msg.translate(str.maketrans('', '', string.punctuation))
    if FilterAlgorithm(msg, message.author):
        await message.delete()
        await message.channel.send(f'{message.author.mention}, what is wrong with you? That word is *not* allowed! Go to timeout!')
        await message.author.timeout(duration, reason="Do not do that again >:(")
    # a simple reply to any mentions of the bot (for future use with bardbot)
    if bot.user.mentioned_in(message):
        await message.channel.send("Do not @ me")


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


@bot.command()
async def filterList(ctx):
    '''Shows the list of filtered strings'''
    await ctx.send(f'Filtered strings: {FilteredStrings}')
    await ctx.message.delete()

@bot.command()
async def copypasta(ctx):
    '''sends a message of a random copy pasta from the json file'''
    # import the copypasta json file 
    with open("config/copypasta.json") as jsonFile:
        mega = json.load(jsonFile)
        data = mega["copyastas"]
        # select a random copy pasta
        pasta = random.choice(data)
    message = f"# {(pasta)['name']}\n{(pasta)['text']}"
    await ctx.send(message)
    await ctx.message.delete()

bot.run(token)