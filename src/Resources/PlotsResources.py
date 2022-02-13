import src.Services.GCPService as GCPService
import src.Services.PlotService as PlotService
from src.Models.QueryStrings import QueryStrings


def plot_portfolio():
    qs = QueryStrings()
    prices = GCPService.get_df_from_bigquery(query_string=qs.plot_prices)
    portfolio = GCPService.get_df_from_bigquery(query_string=qs.plot_portfolio)
    PlotService.gen_line_plot(prices, portfolio)

