from src.Utils.functions import get_date, compile_cpp, bq_pivot_table
from src.Models.QueryStrings import QueryStrings
import src.Services.GCPService as GCPService
import src.Services.SP500Service as SP500Service
import src.Services.YahooService as YahooService
import src.Services.StocksServices as StockService
import numpy as np
import datetime as dt


def get_sp500_tickers():
    sp500 = SP500Service.get_sp500()
    GCPService.upload_df_to_bigquery(df=sp500.tickers, destination="tickers.sp500", write_type="replace")


def get_last_update(end_date):
    qs = QueryStrings()
    try:
        max_date = GCPService.get_df_from_bigquery(query_string=qs.max_date).iloc[0, 0]
    except ValueError as err:
        max_date = '2022-01-01'
    return (dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.datetime.strptime(max_date, '%Y-%m-%d')).days


def get_sp500_prices(backfill, end_date):
    print(f"{backfill} days missing")
    qs = QueryStrings()
    if backfill > 0:
        # TODO: START DATE IN QUERY WRONG
        symbols = list(GCPService.get_df_from_bigquery(query_string=qs.tickers)['Symbol'])
        prices = YahooService.send_yahoo_request(symbols, get_date(backfill, end_date), end_date)
        GCPService.upload_df_to_bigquery(df=prices, destination="tickers.prices", write_type="append")


def get_roc(window, end_date):
    # TODO: something to do a sanity check for the produced data
    start_date = get_date(window, end_date)
    qs = QueryStrings(start_date=start_date)
    roc_data = GCPService.get_df_from_bigquery(query_string=qs.roc_data)
    all_results = StockService.calculate_roc(roc_data, start_date, end_date)
    GCPService.upload_df_to_bigquery(df=np.round(all_results, 3), destination="tickers.roc_values",
                                     write_type="replace")


def get_sharpe(end_date, top, max_price):
    compile_cpp()  # compile c++ code
    qs = QueryStrings(top=top, max_price=max_price)
    unique_symbols = list(GCPService.get_df_from_bigquery(query_string=qs.unique_symbols)['Symbols'])
    # TODO: exclude mergers stocks
    sharpe_data = GCPService.get_df_from_bigquery(query_string=bq_pivot_table(unique_symbols))
    StockService.calculate_sharpe(sharpe_data)
    sharpe_df = StockService.gen_sharpe_df(unique_symbols, end_date)
    GCPService.upload_df_to_bigquery(df=sharpe_df, destination="tickers.sharpe_values",
                                     write_type="replace")


def gen_portfolio(max_budget):
    qs = QueryStrings()
    portfolio_data = GCPService.get_df_from_bigquery(query_string=qs.portfolio)
    portfolio_df = StockService.gen_portfolio_df(portfolio_data, max_budget)
    GCPService.upload_df_to_bigquery(df=portfolio_df, destination="tickers.portfolio",
                                     write_type="replace")


def gen_portfolio_performance():
    qs = QueryStrings()
    portfolio_performance = GCPService.get_df_from_bigquery(query_string=qs.portfolio_performance)
    # TODO: checks for the portfolio_performance
    GCPService.upload_df_to_bigquery(df=portfolio_performance, destination="tickers.portfolio_performance",
                                     write_type="replace")
