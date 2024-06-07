import discord
from discord.ext import commands
import random
import os
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def mem(ctx):

    memes = random.choice(os.listdir("images"))

    with open(f'images/{memes}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def con(ctx):
     consejos = ["Reduce el consumo de plástico.", "Apaga las luces cuando no las necesites.", "Usa transporte público o bicicleta.","Recoge la basura en la naturaleza.", "Planta árboles y cuida la vegetación local."]
     await ctx.send(random.choice(consejos))

@bot.command()
async def rim(ctx):
    rimas = ["Con cariño y acción, salvemos nuestra misión.", "En armonía con la tierra, la vida se encierra.","Consciencia en acción, por un mundo en expansión.", "Cada paso, cada gesto, por un mundo en esto.", "Con amor y voluntad, preservemos la biodiversidad."]
    await ctx.send(random.choice(rimas))

@bot.command()
async def video(ctx):
    video_eco = 'https://youtu.be/aWgHk8Mso0s?si=_kcKpofmS4QWOHcZ'
    await ctx.send(f'Aquí tienes un video del porque cuidar el medio ambiente o el ecosistema. (CREDITOS AL CANAL DE YOUTUBE: Clío Niños) {video_eco}')



@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcom mand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')




bot.run('TOKEN')
