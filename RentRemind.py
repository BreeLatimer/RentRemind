"""
Description: This script will @everyone reminders to pay rent and other bills
"""

import discord
from discord.ext import tasks, commands
import os
from datetime import date, datetime
from calendar import monthrange

token = os.environ.get('RENTREMIND_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(
    command_prefix="!",
    description='A bot to remind people to pay rent and other bills',
    intents=intents,
)

@client.event
async def on_ready():
    await client.wait_until_ready()
    check_remind.start()
    print('Bot is ready.')

# Check every hour for reminders
@tasks.loop(hours=1)
async def check_remind():
    # get today's date
    # day = date.today().day

    # get today's month
    # month = date.today().month

    # get today's year
    # year = date.today().year

    # get the current hour
    #hour = datetime.now().hour

    day = 11
    month = 11
    year = 2022
    hour = 12
    channel = client.get_channel((int)(os.environ.get('CHANNEL_ID')))

    # If it is the 11th of the month and past 12pm, send a message to the channel
    if day == 11 and hour == 12:
        await channel.send('@everyone The power bill is due in one week!')

    # If it is the 18th of the month and past 12pm, send a message to the channel
    if day == 18 and hour == 12:
        await channel.send('@everyone The internet bill($14.83) is due in one week, and the power bill is due today!')

    # If it is the 23rd of the month and past 12pm, send a message to the channel
    if day == monthrange(year, month)[1] - 7 and hour == 12:
        await channel.send('@everyone Rent is due at the end of the month!')

    # If it is the 25th of the month and past 12pm, send a message to the channel
    if day == 25 and hour >= 12:
        await channel.send('@everyone The internet bill is due today!')

    # If it is the last day of the month and past 12pm, send a message to the channel
    if day == monthrange(year, month)[1] and hour == 12:
        await channel.send('@everyone Rent is due today!')

# Run the bot
client.run(token)