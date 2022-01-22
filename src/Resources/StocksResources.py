import src.Services.GCPService as GCPService
import src.Services.SP500Service as SP500Service
import src.Services.YahooService as YahooService
import src.Services.StocksServices as StockService
import datetime as dt
import numpy as np


def get_date(window):
    date = dt.datetime.today() - dt.timedelta(days=window)
    # weekend
    if date.weekday() > 4:
        date -= dt.timedelta(days=6 - date.weekday())
    return date.strftime('%Y-%m-%d')


def get_sp500_tickers():
    sp500 = SP500Service.get_sp500()
    GCPService.upload_df_to_bigquery(df=sp500.tickers, destination="tickers.sp500", write_type="replace")


def get_sp500_prices():
    query_tickers = "SELECT DISTINCT(Symbol) as Symbol FROM `tickers.sp500`"
    symbols = list(GCPService.get_df_from_bigquery(query_string=query_tickers)['Symbol'])
    prices = YahooService.send_yahoo_request(symbols, get_date(3), get_date(2))
    # TODO: write_type should be "append" when done testing
    GCPService.upload_df_to_bigquery(df=prices, destination="tickers.prices", write_type="append")


def get_roc():
    query_roc_data = "SELECT * FROM tickers.prices"
    roc_data = GCPService.get_df_from_bigquery(query_string=query_roc_data)
    all_results = StockService.calculate_roc(roc_data, get_date(30), get_date(2))
    GCPService.upload_df_to_bigquery(df=np.round(all_results, 3), destination="tickers.roc_values", write_type="replace")
