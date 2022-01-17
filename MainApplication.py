import src.Resources.StocksResources as Stocks
import datetime


def main():
    print(f"Starting project {datetime.datetime.today()}")
    Stocks.get_sp500_tickers()
    Stocks.get_sp500_prices()


if __name__ == "__main__":
    main()
