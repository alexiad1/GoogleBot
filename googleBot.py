import discord, auth
from googlesearch import search
from discord.ext import commands

client = commands.Bot(command_prefix='^')

@client.command(name='Search', description='Google searches and sends the top results to text channel, default # of results are one but can be changed in request', help='Type "Search" and an optional amount of desired results followed by a google search query')
async def LetMeGoogleThat(ctx, results=1):
    if results > 10:
        await ctx.send("Too many results to search for try 10 or less")
        return

    await ctx.send('Please enter search Query')
    query = await client.wait_for('message')
    
    if query.author != client:
        await ctx.send(f'now searching for {results} results for "{query.content}"')
        for i in search(str(query.content), stop=results, verify_ssl=False, safe='on'):
            await ctx.send(i)


token = auth.getAuth()
client.run(token)
