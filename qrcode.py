import discord
from discord.ext import commands
import pyqrcode
from pyqrcode import QRCode
import asyncio
import os

bot = commands.Bot(command_prefix=("qr!"))

@bot.event
async def on_ready():
    print('----------------------------')
    print(f'{bot.user.name} Olarak Giriş Yapıldı')
    print(f'Discord Versiyonu {discord.__version__}')
    print('----------------------------')


@bot.command(pass_context=True)
async def karekod(ctx, link):
    s = link

    url = pyqrcode.create(s)
    url.png('qrkod.png', scale = 6)

    await ctx.send(file=discord.File('qrkod.png'))

    await asyncio.sleep(5)

    os.remove("qrkod.png")


@karekod.error
async def karekod_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lütfen kare kodunu oluşturmak istediğiniz linki komut sonrasında belirtiniz.")


bot.run('TOKEN')