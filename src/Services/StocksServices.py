import csv
import ctypes
import numpy as np
import math
import os
import pandas as pd
from src.Models.StockData import StockData
from src.Utils.functions import timeit
from src.Utils.functions import division, log10


@timeit
def calculate_roc(df, start_date, end_date):
    all_results = []
    symbols = list(df['Symbol'].unique())

    for symbol in symbols:
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


@timeit
def calculate_sharpe(df):
    # TODO: clean this up a bit
    simulations = 10000
    df.set_index('Date', drop=True, inplace=True)
    ret = pd.DataFrame(df/df.shift(1)-1).fillna(0).reset_index()
    cpp_sharpe = ctypes.CDLL('src/Utils/cpp_sharpe.so')
    dummy_returns = list(ret.mean() * len(df))
    dummy_std = list(ret.std() * len(df))
    arr_size = (ctypes.c_int)
    arr_size = len(dummy_std)
    arr1 = (ctypes.c_float * len(dummy_returns))(*dummy_returns)
    arr2 = (ctypes.c_float * len(dummy_std))(*dummy_std)
    cpp_sharpe.showSharpe(simulations, arr1, arr2, arr_size)


def gen_sharpe_df(unique_symbols):
    # TODO: add dates to DF
    # TODO: convert ratio to float64
    fdict = {'Symbol': [], 'Sharpe': []}
    ratios = open("src/Utils/cpp_ratios.csv")
    for row in zip(unique_symbols, csv.reader(ratios)):
        fdict['Symbol'].append(row[0])
        fdict['Sharpe'].append(row[1][0][0:5])
    final_df = pd.DataFrame.from_dict(fdict)
    ratios.close()
    os.system("rm src/Utils/cpp_ratios.csv")
    return final_df
