import discord
from discord.ext import commands
import random, os, requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def checkAI(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            namafile = file.filename
            urlfile = file.url
            await file.save(f'./{namafile}')
            await ctx.send(f'gambar telah disimpan dengan nama {namafile}')

            #klasifikasi dan inferensi
            kelas, skor = get_class('keras_model.h5', 'labels.txt', namafile)

            if kelas == 'semut\n' and skor >= 0.75:
                await ctx.send('Ini adalah semut')
                await ctx.send('semut biasa ketemu pada makanan atau minuman yang manis')
            elif kelas == 'rayap\n' and skor >= 0.75:
                await ctx.send('Ini adalah rayap')
                await ctx.send('rayap dapat merusak barang yang terbuat dari kayu')
            elif kelas == 'kumbang\n' and skor >= 0.75:
                await ctx.send('Ini adalah rayap')
                await ctx.send('cangkang kumbang sekilas terlihat seperti cangkang kura-kura')
            else:
                await ctx.send('Ini bukan serangga')
    else:
        await ctx.send('mana nih gambarnya')


bot.run("TOKEN")
