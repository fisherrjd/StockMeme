def get_stock_price(symbol):
    try:
        # Get stock data
        stock_data = yf.Ticker(symbol)

        # Get the current stock price
        current_price = stock_data.info["ask"]

        return current_price
    except Exception as e:
        return f"Error retrieving stock price: {e}"
