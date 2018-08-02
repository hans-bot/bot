import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random, os
import time

"""
Join Link:
    https://discordapp.com/oauth2/authorize?&client_id=456751260704571394&scope=bot&permissions=0
"""

##Bot Information
Client = discord.Client()
bot_prefix = "$"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Hans is online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

#Text Commands
@client.command(pass_context=True)
async def hi(ctx):
    await client.say("Hello there!")

@client.command(pass_context=True)
async def invite(ctx):
    await client.say("https://discordapp.com/oauth2/authorize?&client_id=456751260704571394&scope=bot&permissions=0")

##Voice Channel Password
@client.command(pass_context=True)
async def password(ctx):
    vc = discord.utils.find(lambda x: x.name == 'Password', ctx.message.server.channels)
    pass_attempt = ctx.message.content
    message = ctx.message
    pass_attempt = pass_attempt.strip('$password ')
    

    pword = "3496"
    author = ctx.message.author
    
    if pass_attempt == pword:
        channel = ctx.message.channel
        await client.move_member(author, vc)
        await client.delete_message(message)

    else:
        await client.say("That is the wrong password.")

#Text Commands
@client.command(pass_context=True)
async def release(ctx):
    await client.say("There is no release date yet, but you can add Last Man Sitting to your wishlist here: https://store.steampowered.com/app/774291/Last_Man_Sitting/")

@client.command(pass_context=True)
async def delete(ctx):
    channel = ctx.message.channel
    message = ctx.message
    await client.delete_message(message)

client.run("token")





"""
https://media.readthedocs.org/pdf/discordpy/rewrite/discordpy.pdf
https://github.com/20BBrown14/Voice_Channel_Discord_Bot/blob/master/python_bot.py
"""
