import discord
import yfinance as yf
from discord.ext import commands

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


# Command: !stock <ticker>
@bot.command(name="stock", help="Get the current stock price for a given ticker")
async def get_stock_price(ctx, ticker):
    try:
        # Get stock data
        stock_data = yf.Ticker(ticker)

        # Get the current stock price
        current_price = stock_data.info["ask"]

        # Send the response to the Discord channel
        await ctx.send(f"The current stock price of {ticker} is: {current_price}")
    except Exception as e:
        await ctx.send(f"Error retrieving stock price: {e}")


# Command: !stock <ticker>
@bot.command(name="info", help="Get the latest news on a stock from its ticker")
async def get_stock_price(ctx, ticker):
    await ctx.send(f"Currently a WIP... \n{ticker} has no data yet")


# Run the bot with the token
bot.run("MTIxNTAyMTkyMTUzNjcwNDUzMg.G1M7Gy.KxSwWB8oZjOHhNVDisuwYo9588AQz8lkW4LHrc")
