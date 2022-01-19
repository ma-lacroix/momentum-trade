import src.Resources.StocksResources as Stocks
import datetime as dt
import time


# TODO: put this decorator in a utils file
def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        print(f"{func.__name__} took %2.4f {te - ts} seconds")
        return result

    return timed


@timeit
def main():
    print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
    Stocks.get_sp500_tickers()
    Stocks.get_sp500_prices()
    Stocks.get_roc()


if __name__ == "__main__":
    main()
