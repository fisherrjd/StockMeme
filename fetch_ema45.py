import yfinance as yf
import pandas as pd
import argparse

def fetch_ema(ticker, days=7):
    # Set the time period for the last 'days' days
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')
    start_date = (pd.to_datetime('today') - pd.DateOffset(days=days)).strftime('%Y-%m-%d')

    # Fetch historical data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate EMA45
    data['EMA45'] = data['Close'].ewm(span=45, adjust=False).mean()

    # Display the results
    print(data[['Close', 'EMA45']])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch EMA45 values for a stock over a specified number of days.")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol")
    parser.add_argument("--days", type=int, default=7, help="Number of days for historical data (default: 7)")

    args = parser.parse_args()

    fetch_ema(args.ticker, args.days)