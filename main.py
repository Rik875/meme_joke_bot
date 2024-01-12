import discord
import os
import random
import pyjokes
from googletrans import Translator
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

translator = Translator()

bot = commands.Bot(command_prefix='$', intents=intents)

image = os.listdir('image')

@bot.command()
async def mem(ctx):
    picture = random.choice(image)
    with open(f'image/{picture}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file = picture)

@bot.command()
async def joke(ctx):
    joke = pyjokes.get_joke()
    joke_result = translator.translate(joke, dest='ru')
    await ctx.send(joke_result.text)

      

bot.run("MTE4ODg0ODc2MTU5MDUyNjAwMg.Gh2ZCi.XMX5BAsefyD-jFDXKeLNRIzWZIOwT3ZBWloRjs")