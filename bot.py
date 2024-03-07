import discord
import yfinance as yf
from discord.ext import commands
import Deck

# Define intents
intents = discord.Intents.all()  # Set all intents to True

# Create an instance of the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)


# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("------")


# Command: !hello
@bot.command(name="hello", help="Responds with a greeting")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")


# Command: !poop
@bot.command(name="poop", help="Poop In Dr's mouth")
async def hello(ctx):
    await ctx.send(f"I want to poop in Dr's mouth!")


# Command: !card
@bot.command(name="card", help="Draw a card")
async def hello(ctx):

    deck = Deck.Deck()
    hand = deck.deal(1)
    print("Dealt cards:")
    for card in hand:
        print(card)
        await ctx.send(f"{card}")


# Run the bot with the token
