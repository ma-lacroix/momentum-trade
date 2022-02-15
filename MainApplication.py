from src.Utils.functions import timeit
import src.Resources.StocksResources as Stocks
import src.Resources.PlotsResources as Plots
import datetime as dt
import os


@timeit
def main():
    print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
    end = '2022-02-10'
    # Stocks.get_sp500_tickers()
    # Stocks.get_sp500_prices(Stocks.get_last_update(end), end)
    # Stocks.get_roc(30, end)
    # Stocks.get_sharpe(end, 10)
    # Stocks.gen_portfolio(2250)
    # Stocks.gen_portfolio_performance()
    Plots.plot_portfolio()


if __name__ == "__main__":
    main()
