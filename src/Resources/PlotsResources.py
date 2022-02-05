import src.Services.GCPService as GCPService
import src.Services.PlotService as PlotService


def plot_portfolio():
    query_prices = "SELECT * FROM tickers.prices t1 JOIN `tickers.portfolio` t2 USING(Symbol) ORDER BY t1.Date"
    query_portfolio = "SELECT * FROM tickers.portfolio ORDER BY Securities"
    prices = GCPService.get_df_from_bigquery(query_string=query_prices)
    portfolio = GCPService.get_df_from_bigquery(query_string=query_portfolio)
    PlotService.gen_line_plot(prices, portfolio)

