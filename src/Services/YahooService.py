import pandas as pd
from src.Models.YahooResponse import YahooResponse


def send_yahoo_request(symbols):
    prices = []
    for symbol in symbols:
        # TODO: insert proper START and END values
        prices.append(YahooResponse(symbol, '2021-01-13', '2021-01-14').df)
    return pd.concat(prices)
