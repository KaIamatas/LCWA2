import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = 'NDQ4MjMyNzQ2OTE4MjE1Njgw.DeTI_w.QiLumUFS8jy_SUdhoPm16k9m9_w'

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
