#Discord imports 
import discord
from discord.ext import commands

# Generics 
import string
import datetime
import os
import random

# File manipulation
import json 

#other
from src.FilterAlgorithm import FilterAlgorithm

with open('config/config.json') as jsonFile:
            data = json.load(jsonFile)
            token = data['token']

#init
description = '''This is V-duck, a silly discord bot. 
The command prefix is `:V ` (including the white space after :V).
'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=[':V ',':v ', ':V',':v'], description=description, intents=intents)

# Cogs
extensions = ['Cogs.Misc',
              'Cogs.WordFilter',
              'Cogs.CopyPasta']

# init
if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run(token)