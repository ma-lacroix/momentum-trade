import src.Services.GCPService as GCPService
import src.Services.PlotService as PlotService


def plot_prices():
    query_prices = "SELECT * FROM tickers.prices ORDER BY Date"
    query_roc = "SELECT * FROM tickers.roc_values"
    prices = GCPService.get_df_from_bigquery(query_string=query_prices)
    roc_values = GCPService.get_df_from_bigquery(query_string=query_roc)
    PlotService.gen_line_plot(prices, roc_values)

