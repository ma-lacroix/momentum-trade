from src.Utils.functions import timeit
import src.Resources.StocksResources as Stocks
import src.Resources.PlotsResources as Plots
import datetime as dt


@timeit
def main():
    print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
    end = '2022-01-28'
    Stocks.get_sp500_tickers()
    Stocks.get_sp500_prices(Stocks.get_last_update(end), end)
    Stocks.get_roc(30, end)
    Plots.plot_prices()
    Stocks.get_sharpe()


if __name__ == "__main__":
    main()
