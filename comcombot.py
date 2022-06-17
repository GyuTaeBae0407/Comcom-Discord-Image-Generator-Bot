import discord
import os

from discord.ext import commands

Token = os.environ.get('DISCORD_TOKEN', 'development')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('로그인중. ')
    print(f"봇={bot.user.name} 연결중")
    print('연결 완료')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command(aliases=['hi'])
async def 안녕(ctx):
    print('안녕~~')
    await ctx.send('안녕하세요.')


@bot.command(aliases=['hello'])
async def Hi(ctx):
    await ctx.send('Hello.')


@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(text)

# api call 형식으로해서 (아니면 서버있는걸, 예: lib)
# command: /Image <-- 커맨드 시작이고
# /Image (ctx) Computer with a mouse (Text) <-- (ctx, *, text)
# Image maker <-- (text) input, output --> discord send

bot.run(Token)
