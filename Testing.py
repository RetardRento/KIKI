import openai
import os
import discord
from discord.ext import commands

API_KEY = 'YOUR_API_KEY'
os.environ['OPENAI_KEY'] = API_KEY
openai.api_key = os.environ['OPENAI_KEY']

bot = commands.Bot(command_prefix='!')  
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ask(ctx, *, question):
    response = openai.Completion.create(engine='text-davinci-003', prompt=question, max_tokens=200)
    await ctx.send(response['choices'][0]['text'])

bot.run('YOUR_DISCORD_AUTHENTICATION_KEY')
