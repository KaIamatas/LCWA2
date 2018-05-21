import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = ("?", "!")
TOKEN = 'NDQ3NTAwMDAzOTIyMTQ5Mzc3.DeIeaQ.USPt4Bsnj0EagijHaIrwqZUsyo0'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
