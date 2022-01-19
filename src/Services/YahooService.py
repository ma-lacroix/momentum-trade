import pandas as pd
from src.Models.YahooResponse import YahooResponse


def send_yahoo_request(symbols, start_date, end_date):
    prices = []
    for symbol in symbols:
        print(f"Getting data for {symbol}")
        prices.append(YahooResponse(symbol, start_date, end_date).df)
    return pd.concat(prices)
