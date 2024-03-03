# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import subprocess
import math 
import random 
import json 

# load in json file 
# import internals from json
with open('internal.json') as jsonFile:
     data = json.load(jsonFile)
     token = data['token']
     filtered_strings = data['filtered_strings']
# also import copypasta.json
pastas = open('copypasta.json', 'r')

description = '''This is V-duck, a silly discord bot. 
The command prefix is `:V ` (including the white space after :V).
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=':V ', description=description, intents=intents)

# Events

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
        await ctx.send("I am not connected to a voice channel ?:/")
    await ctx.message.delete()

@bot.command()
async def filter_list(ctx):
    '''Shows the list of filtered strings'''
    await ctx.send(f'Filtered strings: {filtered_strings}')
    await ctx.message.delete()

@bot.command()
async def copypasta(ctx):
    '''sends a message of a random copy pasta from the json file'''
    with open("copypasta.json") as jsonFile:
        mega = json.load(jsonFile)
        data = mega["copyastas"]
        pasta = random.choice(data)
    message = f"# {(pasta)['name']}\n{(pasta)['text']}"
    await ctx.send(message)
    await ctx.message.delete()

#work in progress
@bot.command()
async def play(ctx, video_url):
    '''Play a video from any url'''
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        voice_client = await voice_channel.connect()
        try:
            # Open the video using the default media player on the host machine
            subprocess.Popen(['xdg-open', video_url])
            await ctx.send(f'Playing {video_url} in the voice channel.')
        except Exception as e:
            await ctx.send(f'An error occurred while playing the video: {str(e)}')
    else:
        await ctx.send("You need to be in a voice channel to use this command.")
    await ctx.message.delete()

bot.run(token)