from src.Utils.functions import get_date, compile_cpp, bq_pivot_table
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
    try:
        query_max_date = "SELECT MAX(Date) AS max_date FROM `tickers.prices`"
        max_date = GCPService.get_df_from_bigquery(query_string=query_max_date).iloc[0, 0]
    except ValueError as err:
        max_date = '2022-01-01'
    return (dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.datetime.strptime(max_date, '%Y-%m-%d')).days


def get_sp500_prices(backfill, end_date):
    print(f"{backfill} days missing")
    if backfill > 0:
        # TODO: remove the LIMIT condition
        query_tickers = "SELECT DISTINCT(Symbol) as Symbol FROM `tickers.sp500` ORDER BY 1"
        symbols = list(GCPService.get_df_from_bigquery(query_string=query_tickers)['Symbol'])
        prices = YahooService.send_yahoo_request(symbols, get_date(backfill, end_date), end_date)
        GCPService.upload_df_to_bigquery(df=prices, destination="tickers.prices", write_type="append")


def get_roc(window, end_date):
    # TODO: something to do a sanity check for the produced data
    start_date = get_date(window, end_date)
    query_roc_data = f"SELECT * FROM tickers.prices WHERE Date >= '{start_date}'"
    roc_data = GCPService.get_df_from_bigquery(query_string=query_roc_data)
    all_results = StockService.calculate_roc(roc_data, start_date, end_date)
    GCPService.upload_df_to_bigquery(df=np.round(all_results, 3), destination="tickers.roc_values",
                                     write_type="replace")


def get_sharpe(end_date, top):
    compile_cpp()  # compile c++ code
    query_unique_symbols = f"""
    SELECT Symbol AS Symbols FROM
        (SELECT Symbol FROM `tickers.roc_values`
        WHERE Compute_date = CAST(current_date() AS STRING)
        ORDER BY roc_close DESC) 
    LIMIT {top}"""
    unique_symbols = list(GCPService.get_df_from_bigquery(query_string=query_unique_symbols)['Symbols'])
    sharpe_data = GCPService.get_df_from_bigquery(query_string=bq_pivot_table(unique_symbols))
    StockService.calculate_sharpe(sharpe_data)
    sharpe_df = StockService.gen_sharpe_df(unique_symbols, end_date)
    GCPService.upload_df_to_bigquery(df=sharpe_df, destination="tickers.sharpe_values",
                                     write_type="replace")


def gen_portfolio(max_budget):
    query_portfolio = """
    WITH last_close AS (
      SELECT t1.Symbol AS Symbol, t1.Date AS Date, Close
      FROM `tickers.prices` t1
      JOIN (SELECT Symbol, MAX(Date) AS Date FROM `tickers.prices` GROUP BY 1) t2
      ON t1.Symbol = t2.Symbol AND t1.Date = t2.Date
    ), roc_values AS (
      SELECT t1.Symbol AS Symbol, roc_close, roc_avg_daily_change_log10
      FROM `tickers.roc_values` t1
      JOIN (SELECT Symbol, MAX(End_date) AS Date FROM `tickers.roc_values` GROUP BY 1) t2
      ON t1.Symbol = t2.Symbol AND t1.End_date = t2.Date
    ), sharpe_values AS (
      SELECT Symbol, Sharpe FROM `tickers.sharpe_values` 
    )
    SELECT * FROM sharpe_values JOIN (SELECT * FROM roc_values) USING(Symbol) 
        JOIN (SELECT * FROM last_close) USING(Symbol) ORDER BY Sharpe DESC
    """
    portfolio_data = GCPService.get_df_from_bigquery(query_string=query_portfolio)
    portfolio_df = StockService.gen_portfolio_df(portfolio_data, max_budget)
    GCPService.upload_df_to_bigquery(df=portfolio_df, destination="tickers.portfolio",
                                     write_type="replace")