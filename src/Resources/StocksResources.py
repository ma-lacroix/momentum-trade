import src.Services.GCPService as GCPService
import src.Services.SP500Service as SP500Service
import src.Services.YahooService as YahooService


def get_sp500_tickers():
    sp500 = SP500Service.get_sp500()
    GCPService.upload_df_to_bigquery(df=sp500.tickers, destination="tickers.sp500", write_type="replace")


def get_sp500_prices():
    query_tickers = "SELECT DISTINCT(Symbol) as Symbol FROM `tickers.sp500`"

    # TODO: remove .head() -> for testing purposes

    symbols = list(GCPService.get_df_from_bigquery(query_string=query_tickers)['Symbol'].head(10))
    prices = YahooService.send_yahoo_request(symbols)
    GCPService.upload_df_to_bigquery(df=prices, destination="tickers.prices", write_type="replace")


def get_roc():

    # TODO: logic

    query_roc_data = "SELECT * FROM tickers.prices"
    roc_data = GCPService.get_df_from_bigquery(query_string=query_roc_data)
    print(roc_data)

