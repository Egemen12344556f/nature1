import discord
import random
from discord.ext import commands
import os
print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
       print(f'{bot.user} Ok Ok I am here! :) ')

@bot.command()
async def DoğayıKoru(ctx):
      
    await ctx.send(f'Merhaba ben bir botum Ve amacım insanların doğa hakkında bilinçlenmesi.Sende doğa hakkında bilgi öğrenmek istiyorsan /Help yaz. ')
    @bot.command()
    async def Havaaa(ctx):
        await ctx.send(f'HAVA')
        await ctx.send(f'Havayı korumak için yapılması gereken şeyler;')
        await ctx.send(f'Fabrikalara filtre takmak, kapalı alanlarda sigaraiçmemek, elektrikli araç kullanmak vs;')

@bot.command()
async def Help(ctx):
    await ctx.send(f'hava için /Hava')



# @bot.command()
# async def Hava(ctx):
#     await ctx.send(f'HAVA')
#     await ctx.send(f'Havayı korumak için yapılması gereken şeyler;')
#     await ctx.send(f'Fabrikalara filtre takmak, kapalı alanlarda sigaraiçmemek, elektrikli araç kullanmak vs;')



@bot.command()
async def Su(ctx):

    await ctx.send(f'SU')
    await ctx.send(f'Suyu korumak için fabriklaradan çıkan kirli suları filtrelemeliyiz ')
    await ctx.send(f'SU')


@bot.command()
async def Toprak(ctx):
    await ctx.send(f'toprak')
    await ctx.send(f'Gıda atığımızı azaltmak,Kompost yapmak, Toprak ölçümü yaptırmak vs,')

      

@bot.command()
async def mem(ctx):
    with open('images\mem1.jpeg', 'rb') as f:

        picture = discord.File(f)
        await ctx.send(file=picture)


bot.run("You cant get that hahahhahahhahhahhaha")
