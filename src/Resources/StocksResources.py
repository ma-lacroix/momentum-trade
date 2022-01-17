import src.Services.GCPService as GCPService
import src.Services.StocksServices as StockService
import src.Services.YahooService as YahooService
import src.Services.SP500Service as SP500Service
import pandas as pd


def get_sp500_tickers():
    sp500 = SP500Service.get_sp500()
    GCPService.upload_df_to_bigquery(df=sp500.tickers, destination="tickers.sp500")


def get_sp500_prices():
    query_tickers = "SELECT DISTINCT(Symbol) FROM `tickers.sp500`"
    df = GCPService.get_df_from_bigquery(query_string=query_tickers)
    print(df.head())


def get_roc():
    pass


def get_sharpe():
    pass


def upload_to_gcp():
    pass


def pull_from_gcp():
    pass
