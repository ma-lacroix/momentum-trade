import numpy as np
import pandas as pd
from src.Models.StockData import StockData


def calculate_roc(df, start_date, end_date):
    all_results = []
    symbols = list(df['Symbol'].unique())

    for symbol in symbols:
        current_close = df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['Close'].item()
        previous_close = df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['Close'].item()
        current_high_low = df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['High'].item() - \
                           df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['Low'].item()
        previous_high_low = df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['High'].item() - \
                            df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['Low'].item()
        current_close_open = current_close - df[(df['Symbol'] == symbol) & (df['Date'] == end_date)]['Open'].item()
        previous_close_open = previous_close - df[(df['Symbol'] == symbol) & (df['Date'] == start_date)]['Open'].item()
        avg_daily_change = np.mean(df[df['Symbol'] == symbol]['Close'] / df[df['Symbol'] == symbol] \
            .shift(1)['Close'].fillna(1)).item()
        all_results.append(StockData(symbol, start_date, end_date, current_close, previous_close, current_high_low,
                                     previous_high_low, current_close_open, previous_close_open, avg_daily_change).df)
    return pd.concat(all_results).reset_index(drop=True)
