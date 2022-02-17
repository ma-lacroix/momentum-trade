from src.Models.PlotModel import StockPlot
import datetime as dt


def gen_line_plot(prices, portfolio, portfolio_performance):
    line_plot = StockPlot(title=f"ROC and Sharpe Report {dt.datetime.today().strftime('%Y-%m-%d')}",
                          prices=prices, values=portfolio,
                          performance=portfolio_performance, mode='markers+lines',
                          filename="Portfolio.html")
    line_plot.gen_plot()
