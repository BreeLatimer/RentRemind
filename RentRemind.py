"""
Description: This script will @everyone reminders to pay rent and other bills
"""

import discord
from discord.ext import commands
import os
import asyncio
from datetime import date, datetime, timedelta
from calendar import monthrange

token = "MTAzODM2MjE4MDQ5MzUyMDg5Nw.Gv0OIP.TikxCTzTrtSjZmrggtVDKByQ0qSz70ckMH7JxU"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(">"),
    description='A simple music bot',
    intents=intents,
)

# Command to check every 12 hours if it is 12pm on the 23rd of the month
# If it is, send a message to the channel
@bot.command(name='initialize', help='To remind everyone to pay rent', aliases=['i']):
async def initialize(ctx):
    # Create a loop that is executed every 12 hours
    while True:
        # Get the current date
        today = date.today()
        # Get the current time
        now = datetime.now()
        # Get the current hour
        current_hour = now.strftime("%H")
        # Get the current month
        current_month = today.strftime("%m")
        # Get the current year
        current_year = today.strftime("%Y")

        # If it is the 11th of the month and past 12pm, send a message to the channel
        if today.day == 11 and current_hour >= 12:
            await ctx.send('@everyone The power bill is due in one week!')

        # If it is the 18th of the month and past 12pm, send a message to the channel
        if today.day == 18 and current_hour >= 12:
            await ctx.send('@everyone The Internet bill is due in one week, and the power bill is due today!!')

        # If it is the 23rd of the month and past 12pm, send a message to the channel
        if today.day == 23 and current_hour >= 12:
            await ctx.send('@everyone Rent is due at the end of the month!')

        # If it is the 25th of the month and past 12pm, send a message to the channel
        if today.day == 25 and current_hour >= 12:
            await ctx.send('@everyone The internet bill is due today!!')

        # If it is the last day of the month and past 12pm, send a message to the channel
        if today.day == monthrange(current_year, current_month)[1] and current_hour >= 12:
            await ctx.send('@everyone Rent is due today!!')

        # Wait 12 hours to check again
        await asyncio.sleep(43200)

# Run the bot
bot.run(token)