#A bot created to text members of the server to get on discord
#Created by Elias Frieling

import os
import random
import requests

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='scoob')
async def on_message(ctx):

    scoob_quotes = [
    'Drink your milk X',
    'Doob Town',
    'I gotta go workout',
    'Rob Roy is my hero'
    ]

    response = random.choice(scoob_quotes)
    await ctx.channel.send(response)

#Text message to jared
@bot.command(name='jared')
async def on_message(ctx):

    resp = requests.post('https://textbelt.com/text', {
    'phone': JARED_PHONE,
    'message': 'ATTENTION GAMER: YOU HAVE BEEN SUMMONED TO YOUR GAMING STATION',
    'key': 'textbelt',
    })
    response = resp.json()
    if response['success'] == False:
        await ctx.channel.send('Please venmo Elias to buy more messages')
    else:
        await ctx.channel.send('GAMER JARED HAS BEEN SUMMONED')



bot.run(TOKEN)
