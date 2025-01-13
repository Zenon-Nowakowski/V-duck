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

#other
from src.FilterAlgorithm import FilterAlgorithm

class CopyPastaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# load in json file 
# import internals from json
with open('config/config.json') as jsonFile:
    data = json.load(jsonFile)
    pastas = open('config/copypasta.json', 'r')

@commands.command()
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