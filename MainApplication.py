from src.Utils.functions import timeit
import src.Resources.StocksResources as Stocks
import datetime as dt


@timeit
def main():
    print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
    end = '2022-01-21'
    # Stocks.get_sp500_tickers()
    Stocks.get_sp500_prices(Stocks.get_last_update(end), end)
    Stocks.get_roc(30, end)


if __name__ == "__main__":
    main()
