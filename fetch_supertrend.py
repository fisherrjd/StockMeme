import yfinance as yf
import pandas as pd
import argparse

def calculate_supertrend(data, atr_length=7, multiplier=3):
    # Calculate ATR
    data['TR'] = abs(data['High'] - data['Low'])
    data['ATR'] = data['TR'].rolling(window=atr_length).mean()

    # Calculate Supertrend
    data['UpperBand'] = data['High'] + multiplier * data['ATR']
    data['LowerBand'] = data['Low'] - multiplier * data['ATR']
    data['Supertrend'] = 1.0

    for i in range(1, len(data)):
        if data['Close'].iloc[i - 1] <= data['UpperBand'].iloc[i - 1]:
            data.loc[data.index[i], 'Supertrend'] = max(data['UpperBand'].iloc[i], data['Supertrend'].iloc[i - 1] if not pd.isna(data['Supertrend'].iloc[i - 1]) else 0)
        else:
            data.loc[data.index[i], 'Supertrend'] = min(data['LowerBand'].iloc[i], data['Supertrend'].iloc[i - 1] if not pd.isna(data['Supertrend'].iloc[i - 1]) else 0)

    return data[['Close', 'Supertrend']]

def fetch_supertrend(ticker, days=7, atr_length=7, multiplier=3):
    # Set the time period for the last 'days' days
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')
    start_date = (pd.to_datetime('today') - pd.DateOffset(days=days)).strftime('%Y-%m-%d')

    # Fetch historical data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate Supertrend
    result = calculate_supertrend(data, atr_length=atr_length, multiplier=multiplier)

    # Display the results
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Supertrend values for a stock over a specified number of days.")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol")
    parser.add_argument("--days", type=int, default=7, help="Number of days for historical data (default: 7)")
    parser.add_argument("--atr_length", type=int, default=7, help="Length of ATR calculation (default: 7)")
    parser.add_argument("--multiplier", type=int, default=3, help="Multiplier for Supertrend calculation (default: 3)")

    args = parser.parse_args()

    fetch_supertrend(args.ticker, args.days, args.atr_length, args.multiplier)
