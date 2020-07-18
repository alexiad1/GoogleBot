import discord
from googlesearch import search
from discord.ext import commands

client = commands.Bot(command_prefix='^')

@client.command(name='Search', description='Google searches and sends the top results to text channel, default # of results are one but can be changed in request')
async def LetMeGoogleThat(ctx, query, results=1):
    for i in search(query, num=results, stop=results, verify_ssl=False):
        await ctx.send(i)


token = 'NzMzNjQzNDM3NzM1NDExNzgz.XxGKlg.tPYPYgXCR6QC6DFIxPREWELFmz0'
client.run(token)