import discord
from discord.ext import commands
from to import Token
import asyncio
import time
import interactions


bot = interactions.Client(token=                      )

"""
@bot.event
async def on_ready():
    print('Log in. ')
    print('Complete.')
    await bot.change_presence(status=discord.Status.online, activity=None)
    """

@bot.command(
    name="Progress",
    description="Shows Progress",
    scope=981957526562156655,
    options = [
        interactions.Option(
            name="Code",
            description="Put your code here!",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def my_first_command(ctx: interactions.CommandContext, text: str):
    await ctx.send(ctx.text.author.mention + "Progress is" + "0")

   
"""
@bot.command()
async def status(ctx,message):
    list_ = ['stats','stat','status','progress']
    
    if any(word in message for word in list_):
        await ctx.send(ctx.message.author.mention + "Your Image is generating")  
    else:
        await ctx.send(ctx.message.author.mention + "It is ready")   
""" 

bot.start()


