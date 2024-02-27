import yfinance as yf
import pandas as pd
import argparse


def calculate_supertrend(data, multiplier, atr_length):
    high = data["High"]
    low = data["Low"]

    upper_band = (high + low) / 2 + multiplier * atr_length
    lower_band = (high + low) / 2 - multiplier * atr_length
    return [upper_band, lower_band]


def fetch_supertrend(ticker, days=1):
    end_date = pd.to_datetime("today").strftime("%Y-%m-%d")
    start_date = (pd.to_datetime("today") - pd.DateOffset(days=days)).strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start_date, end=end_date)

    print(calculate_supertrend(data, 7, 3))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch Supertrend values for a stock over a specified number of days."
    )
    parser.add_argument("ticker", type=str, help="Stock ticker symbol")
    parser.add_argument(
        "--days", type=int, default=2, help="Number of days for historical data (default: 1)"
    )
    parser.add_argument(
        "--atr_length", type=int, default=7, help="Length of ATR calculation (default: 7)"
    )
    parser.add_argument(
        "--multiplier",
        type=int,
        default=3,
        help="Multiplier for Supertrend calculation (default: 3)",
    )

    args = parser.parse_args()

    fetch_supertrend(args.ticker, args.days)
