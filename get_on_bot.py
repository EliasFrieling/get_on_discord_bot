#A bot created to text members of the server to get on discord
#Created by Elias Frieling

import os
import random
import requests
import time
import discord
from dotenv import load_dotenv
from discord.ext import commands

client = discord.Client()
load_dotenv()
#discord bot token
TOKEN = os.getenv('DISCORD_TOKEN')
#phone number constants
JARED_PHONE = os.getenv('JARED_PHONE')
ELIAS_PHONE = os.getenv('ELIAS_PHONE')
TYLER_PHONE = os.getenv('TYLER_PHONE')
JAKE_PHONE = os.getenv('JAKE_PHONE')
THOMAS_PHONE = os.getenv('THOMAS_PHONE')
MIKE_PHONE = os.getenv('MIKE_PHONE')
LUKE_PHONE = os.getenv('LUKE_PHONE')
COKES_PHONE = os.getenv('COKES_PHONE')
SCOOB_PHONE = os.getenv('SCOOB_PHONE')

PHONE_BOOK = {'jared' : JARED_PHONE,
            'elias' : ELIAS_PHONE,
            'tyler' : TYLER_PHONE,
            'jake' : JAKE_PHONE,
            'thomas' : THOMAS_PHONE,
            'mike' : MIKE_PHONE,
            'luke' : LUKE_PHONE,
            'cokes' : COKES_PHONE,
            'scoob' : SCOOB_PHONE}
API_KEY = os.getenv('API_KEY')

bot = commands.Bot(command_prefix='!')


#on start message
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    #elias_timeout = False


def sendText(name):
    """
    Makes the call to the textbelt api by taking in the name of who the message is going to and sending
    the message to their number through the PHONE_BOOK dictionary.
    Returns false and logs the error if the api call failed
    """
    resp = requests.post('https://textbelt.com/text', {
    'phone': PHONE_BOOK[name],
    'message': 'ATTENTION GAMER: YOU HAVE BEEN SUMMONED TO YOUR GAMING STATION',
    'key': API_KEY,
    })
    print(resp.json())
    response = resp.json()
    if response['success'] == False:
        with open('err.log', 'w') as file:
            file.write(str(response))
        file.close()
        return response
    else:
        return response


#Text message to elias
@bot.command(name='elias')
async def on_message(ctx):
    elias_timeout = True
    if elias_timeout:
        response = sendText('elias')
        if response['success']:
            await ctx.channel.send('GAMER ELIAS HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
            #elias_timeout = True
        else:
            await ctx.channel.send('It broke, someone tell elias to check the logs')
    else:
        await ctx.channel.send('Stop spamming messages and wasting my money')

#Text message to jared
@bot.command(name='jared')
async def on_message(ctx):
    response = sendText('jared')
    if response['success']:
        await ctx.channel.send('GAMER JARED HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')

#Text message to tyler
@bot.command(name='tyler')
async def on_message(ctx):
    response = sendText('tyler')
    if response['success']:
        await ctx.channel.send('GAMER TYLER HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')

#Text message to thomas
@bot.command(name='thomas')
async def on_message(ctx):
    response = sendText('thomas')
    if response['success']:
        await ctx.channel.send('GAMER THOMAS HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')
#Text message to jake
@bot.command(name='jake')
async def on_message(ctx):
    response = sendText('jake')
    if response['success']:
        await ctx.channel.send('GAMER JAKE HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')
#Text message to elias
@bot.command(name='mike')
async def on_message(ctx):
    response = sendText('mike')
    if response['success']:
        await ctx.channel.send('GAMER MIKE HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')

@bot.command(name='luke')
async def on_message(ctx):
    response = sendText('luke')
    if response['success']:
        await ctx.channel.send('GAMER LUKE HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')
@bot.command(name='cokes')
async def on_message(ctx):
    response = sendText('cokes')
    if response['success']:
        await ctx.channel.send('GAMER COKES HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')
@bot.command(name='scoob')
async def on_message(ctx):
    response = sendText('scoob')
    if response['success']:
        await ctx.channel.send('GAMER SCOOB HAS BEEN SUMMONED\nMessages left: ' + str(response['quotaRemaining']))
    else:
        await ctx.channel.send('It broke, someone tell elias to check the logs')
@bot.command(name='all')
async def on_message(ctx):
    response = sendText('luke')
    response = sendText('mike')
    response = sendText('jake')
    response = sendText('thomas')
    response = sendText('tyler')
    response = sendText('jared')
    response = sendText('elias')
    response = sendText('cokes')
    response = sendText('scoob')
    await ctx.channel.send('ALL THE GAMERS HAVE BEEN SUMMONED\nI REPEAT ALL THE GAMERS HAVE BEEN SUMMONED AHHHHHHHHHHHHHH')


bot.run(TOKEN)
