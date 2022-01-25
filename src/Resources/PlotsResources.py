import src.Services.GCPService as GCPService
import src.Services.PlotService as PlotService


def plot_prices():
    query = "SELECT * FROM tickers.prices WHERE Symbol = 'ABMD'"
    prices = GCPService.get_df_from_bigquery(query_string=query)
    print(prices.head())
    PlotService.gen_line_plot(prices)

