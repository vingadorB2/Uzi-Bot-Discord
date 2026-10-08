
import discord
from discord.ext import commands
from discord.ext import tasks
import random
import os
import requests
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)
#----------------------------------event-------------------------------------
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f'Bem-vindo ao servidor, {member.mention}! idiota')
#*************************************************************************************


#------------------------ready-------------------------------
@bot.event
async def on_ready():
    frase_aleatoria.start()
#*************************************************************************************
@bot.event
async def on_ready():
    print("Bot online")
    print("Comandos carregados:", [c.name for c in bot.commands])
    frase_aleatoria.start()

#------------------------------------command-----------------
@bot.command()
async def teste(ctx):
    await ctx.send("ligado")


@bot.command(aliases=['aniversario'])
async def aniverdario(ctx):
    print("ativado: aniverdario")
    target = None
    # Tenta por ID primeiro (se configurado), depois por nome/display_name

@bot.command()  
async def humor(ctx):
    print("ativado: humor")
    emotion = random.choice([
        "vai embora >:(",
        "não quero conversar agora",
        "bite me!"
    ])
    await ctx.send(emotion)

@bot.command()
async def gosta(ctx, usuario):
    resposta = random.choice([
        "eu não gosto de ninguém >:(",
        "não",
        "por que quer saber???",
        "sei la",
        "hm, talvez, não me importo >:/"
    ])

    await ctx.send(f"eu gosto do {usuario}? {resposta}" )


def img_aleatoria():
    img = random.choice(os.listdir('imagens')) 
    return img

@bot.command()
async def meme(ctx):
    # Sem uso da função
    with open(f'imagens/{img_aleatoria()}', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#*************************************************************************************


@tasks.loop(minutes=10)
async def frase_aleatoria():
    canal = bot.get_channel(1478179704568807539)   
    canal_real = bot.get_channel(1412946608387133542)   
    frases = [
        "não gosto de ninguém!",
        "humanos são malditos",
        "Bite me!",
        "eu odeio a cyn..."
    ]
    await canal_real.send(random.choice(frases))





bot.run("MTQ4MDY2Njc1NDE3Mzg5NDgxMQ.G2I5Sr.zdErtytMLN8uSaPJsaDWO5A9506g_AKWKa4s-w")








