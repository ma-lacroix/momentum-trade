import src.Resources.StocksResources as Stocks
import datetime as dt
from src.Utils.functions import timeit


@timeit
def main():
    print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
    # Stocks.get_sp500_tickers()
    # Stocks.get_sp500_prices()
    Stocks.get_roc()


if __name__ == "__main__":
    main()
