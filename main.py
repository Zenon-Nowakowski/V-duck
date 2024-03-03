# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import random 
import json 
import string
import datetime
from filteralg import filtering_algorithm

description = '''This is V-duck, a silly discord bot. 
The command prefix is `:V ` (including the white space after :V).
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=':V ', description=description, intents=intents)

# load in json file 
# import internals from json
with open('internal.json') as jsonFile:
    data = json.load(jsonFile)
    token = data['token']
    filtered_strings = data['filtered_strings']
# also import copypasta.json
pastas = open('copypasta.json', 'r')

# Events 

@bot.event
async def on_message(message):
    # this await ensures that the bot will wait and thus be able to continue processing commands
    await bot.process_commands(message)
    # if the message is from the bot, ignore it
    if message.author == bot.user:
        return
    # preset the timeout time (30 seconds)
    duration = datetime.timedelta(seconds=30)
    # Convert the message to lowercase and remove punctuation, then check if it contains any of the filtered strings
    # scan the message word by word to see if the message contains any of the filtered strings
    if filtering_algorithm(message.content.lower(), message.author):
        await message.delete()
        await message.channel.send(f'{message.author.mention}, what is wrong with you? That word is *not* allowed! Go to timeout!')
        await message.author.timeout(duration, reason="Do not do that again >:(")
    # a simple reply to any mentions of the bot (for future use with bardbot)
    if bot.user.mentioned_in(message):
        await message.channel.send("Do not @ me")

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
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} began wasting away at {discord.utils.format_dt(member.joined_at)}')
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def echo(ctx, *, content):
    '''basic echo command, by use of admins only'''
    await ctx.send(content)
    await ctx.message.delete()

@bot.command()
async def join(ctx):
    '''Joins the voice channel of the user who called the command'''
    voice_channel_requested = ctx.author.voice.channel
    if voice_channel_requested:
        await voice_channel_requested.connect()
    else:
        await ctx.send("Where are you? (and I'm so sorry!)")
    await ctx.message.delete()

@bot.command()
async def leave(ctx):
    '''Leave a voice channel'''
    voice_channel_source = ctx.guild.voice_client
    if voice_channel_source:
        await voice_channel_source.disconnect()
    else:
        await ctx.send("I am not connected to a voice channel :/")
    await ctx.message.delete()

@bot.command()
async def filter_list(ctx):
    '''Shows the list of filtered strings'''
    await ctx.send(f'Filtered strings: {filtered_strings}')
    await ctx.message.delete()

@bot.command()
async def copypasta(ctx):
    '''sends a message of a random copy pasta from the json file'''
    # impor the copypasta json file 
    with open("copypasta.json") as jsonFile:
        mega = json.load(jsonFile)
        data = mega["copyastas"]
        # select a random copy pasta
        pasta = random.choice(data)
    message = f"# {(pasta)['name']}\n{(pasta)['text']}"
    await ctx.send(message)
    await ctx.message.delete()

bot.run(token)