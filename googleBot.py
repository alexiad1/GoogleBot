import discord, auth
from googlesearch import search
from discord.ext import commands

client = commands.Bot(command_prefix='^')

@client.command(name='Search', description='Google searches and sends the top results to text channel, default # of results are one but can be changed in request')
async def LetMeGoogleThat(ctx, results=1):
    await ctx.send('Please enter search Query')

    query = await client.wait_for('message')

    await ctx.send(f'now searching for {results} results for "{query.content}"')

    for i in search(str(query.content), num=results+1, stop=results+1, verify_ssl=False):
        await ctx.send(i)


token = auth.getAuth()
client.run(token)