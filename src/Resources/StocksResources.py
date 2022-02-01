from src.Utils.functions import get_date, compile_cpp
import src.Services.GCPService as GCPService
import src.Services.SP500Service as SP500Service
import src.Services.YahooService as YahooService
import src.Services.StocksServices as StockService
import numpy as np
import os
import datetime as dt


def get_sp500_tickers():
    sp500 = SP500Service.get_sp500()
    GCPService.upload_df_to_bigquery(df=sp500.tickers, destination="tickers.sp500", write_type="replace")


def get_last_update(end_date):
    try:
        query_max_date = "SELECT MAX(Date) AS max_date FROM `tickers.prices`"
        max_date = GCPService.get_df_from_bigquery(query_string=query_max_date).iloc[0, 0]
    except ValueError as err:
        max_date = '2021-01-01'
    return (dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.datetime.strptime(max_date, '%Y-%m-%d')).days


def get_sp500_prices(backfill, end_date):
    print(f"{backfill} days missing")
    if backfill > 0:
        # TODO: remove the LIMIT condition
        query_tickers = "SELECT DISTINCT(Symbol) as Symbol FROM `tickers.sp500` ORDER BY 1 LIMIT 10"
        symbols = list(GCPService.get_df_from_bigquery(query_string=query_tickers)['Symbol'])
        prices = YahooService.send_yahoo_request(symbols, get_date(backfill, end_date), end_date)
        GCPService.upload_df_to_bigquery(df=prices, destination="tickers.prices", write_type="append")


def get_roc(window, end_date):
    # TODO: something to do a sanity check for the produced data
    query_roc_data = "SELECT * FROM tickers.prices"
    roc_data = GCPService.get_df_from_bigquery(query_string=query_roc_data)
    all_results = StockService.calculate_roc(roc_data, get_date(window, end_date), end_date)
    GCPService.upload_df_to_bigquery(df=np.round(all_results, 3), destination="tickers.roc_values",
                                     write_type="replace")


def get_sharpe():
    lib = 'src/Utils/cpp_sharpe'
    if not os.path.exists(f'{lib}.so'):  # compile c++ code
        compile_cpp(libName=lib)
    query_roc_data = "SELECT * FROM tickers.prices"
    sharpe_data = GCPService.get_df_from_bigquery(query_string=query_roc_data)
    #
