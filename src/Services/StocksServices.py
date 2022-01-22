import numpy as np
import pandas as pd
import math
from src.Models.StockData import StockData
from src.Utils.functions import timeit


def division(val1, val2):
    # some stock data might be null
    if val2 <= 0:
        return 0
    else:
        return round((val1 / val2 - 1) * 100, 3)


def log10(val1):
    if abs(val1) == 0:
        return 0
    else:
        return math.log10(abs(val1))

@timeit
def calculate_roc(df, start_date, end_date):
    all_results = []
    symbols = list(df['Symbol'].unique())

    for symbol in symbols:
        print(symbol)
        # extract the data from the DF
        current_close = df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['Close'].item()
        previous_close = df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['Close'].item()
        current_high_low = df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['High'].item() - \
                            df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['Low'].item()
        previous_high_low = df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['High'].item() - \
                            df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['Low'].item()
        current_close_open = current_close - df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['Open'].item()
        previous_close_open = previous_close - df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['Open'].item()
        roc_avg_daily_change = np.mean(df[df['Symbol'] == symbol]['Close'] / df[df['Symbol'] == symbol] \
                                   .shift(1)['Close'].fillna(1)).item()

        # prepare stock data
        roc_close = division(current_close, previous_close)
        roc_high_low = division(current_high_low, previous_high_low)
        roc_close_open = division(current_close_open, previous_close_open)
        roc_close_open_log10 = log10(roc_close_open)
        roc_avg_daily_change_log10 = math.log10(roc_avg_daily_change)

        # instance of stock data class
        all_results.append(StockData(symbol, start_date, end_date, roc_close, roc_high_low, roc_close_open,
                                     roc_close_open_log10, roc_avg_daily_change, roc_avg_daily_change_log10).df)
    return pd.concat(all_results).reset_index(drop=True)
