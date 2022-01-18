import pandas as pd
from src.Models.StockData import StockData


def calculate_roc(df):
    all_results = []
    symbols = list(df['Symbol'].unique())

    # TODO: dates proper implementation
    min_date = df['Date'].min()
    max_date = df['Date'].max()

    for symbol in symbols:
        current_close = df[(df['Symbol'] == symbol) & (df['Date'] == max_date)]['Close'].item()
        previous_close = df[(df['Symbol'] == symbol) & (df['Date'] == min_date)]['Close'].item()
        current_high_low = df[(df['Symbol'] == symbol) & (df['Date'] == max_date)]['High'].item() - \
                           df[(df['Symbol'] == symbol) & (df['Date'] == max_date)]['Low'].item()
        previous_high_low = df[(df['Symbol'] == symbol) & (df['Date'] == min_date)]['High'].item() - \
                            df[(df['Symbol'] == symbol) & (df['Date'] == min_date)]['Low'].item()
        current_close_open = current_close - df[(df['Symbol'] == symbol) & (df['Date'] == max_date)]['Open'].item()
        previous_close_open = previous_close - df[(df['Symbol'] == symbol) & (df['Date'] == min_date)]['Open'].item()
        all_results.append(StockData(symbol, current_close, previous_close, current_high_low, previous_high_low,
                                     current_close_open, previous_close_open).df)
    return pd.concat(all_results).reset_index(drop=True)
