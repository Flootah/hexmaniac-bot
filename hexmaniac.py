import discord
from discord.ext import commands
import random

description = '''a humble bot that can perform a few simple tasks for now. 
NOT for bully!'''

client = discord.Client()
hex = commands.Bot(command_prefix='!', description= description)

@hex.event
async def on_ready():
    print(hex.user.name + '@' + hex.user.id + ',')
    print('Reporting for Duty!')
    print('------')


@hex.command()
async def echo(*, phrase : str):
    """Repeats whatever the user said."""
    await hex.say(phrase)

@hex.command()
async def roll(dice : str):
    """Rolls dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await hex.say("Uh, i'm not sure what kind of dice you want me to roll..." + 
                        "Please use the NdN format!")
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await hex.say(result)

@hex.command(pass_context=True)
async def thanks(msg):
    member = msg.message.author
    await hex.say("You're welcome, " + '{0.name}'.format(member) + "~")

hex.run('Mzc3NjIwMTE4MjYxMjAyOTY0.DOQAAg.wx2IJIPwIAuD45Iw61Te2lw1azE')
