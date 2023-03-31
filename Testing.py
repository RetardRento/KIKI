import openai
import os
import discord
from discord.ext import commands

API_KEY = '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'
os.environ['OPENAI_KEY'] = API_KEY
openai.api_key = os.environ['OPENAI_KEY']

bot = commands.Bot(command_prefix='!')  # Prefix for the bot commands

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ask(ctx, *, question):
    response = openai.Completion.create(engine='text-davinci-003', prompt=question, max_tokens=200)
    await ctx.send(response['choices'][0]['text'])

bot.run('MTA4NTE5NjA2NjY2MTU5NzIzNQ.GVBfRg.fuU-d13hw-PhxGI7BIYhMDB9YOjzqwFpbjzUKM')

#MTA4NTE5NjA2NjY2MTU5NzIzNQ.GVBfRg.fuU-d13hw-PhxGI7BIYhMDB9YOjzqwFpbjzUKM