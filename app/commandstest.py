import interactions
import discord
from discord.ext import commands


bot = interactions.Client(token="")

#use 2 machine

@bot.command( #has to be in english
    name="request_image", #name of comamand
    description="Request to create an image",
    scope=981957526562156655,
    options = [
        interactions.Option(
            name="text",
            description="Input your description!",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def request_image(ctx: interactions.CommandContext, text: str):
    await ctx.send("Your Image is generating")



@bot.command( #has to be in english
    name="image_status", #name of comamand
    description="Request the status of your image",
    scope=981957526562156655,
    options = [
        interactions.Option(
            name="text",
            description="Input your code!",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    ],
)
async def image_status(ctx: interactions.CommandContext, text: int):
    if text > 10:
        await ctx.send("Your Image is generating")  
    else:
        await ctx.send("It is ready")  
 


bot.start()
