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

class WordFilterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cog.listener()
    async def on_message(message):
        # this await ensures that the bot will wait and thus be able to continue processing commands
        await self.bot.process_commands(message)
        # if the message is from the bot, ignore it
        if message.author == self.bot.user:
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
        if self.bot.user.mentioned_in(message):
            await message.channel.send("Do not @ me")

    @commands.command()
    async def filterList(ctx):
        '''Shows the list of filtered strings'''
        with open('config/config.json') as jsonFile:
            data = json.load(jsonFile)
            FilteredStrings = data['FilteredStrings']
        await ctx.send(f'Filtered strings: {FilteredStrings}')
        await ctx.message.delete()