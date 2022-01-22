from src.Utils.functions import timeit
import src.Resources.StocksResources as Stocks
import datetime as dt


@timeit
def main():
    print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
    end = '2022-01-21'
    backfill_window = 60
    roc_window = 30
    Stocks.get_sp500_tickers()
    Stocks.get_sp500_prices(backfill_window, end)
    Stocks.get_roc(roc_window, end)


if __name__ == "__main__":
    main()
