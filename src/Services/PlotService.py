from src.Models.PlotModel import StockPlot


def gen_line_plot(prices, portfolio):
    line_plot = StockPlot(title="ROC+Sharpe Report", prices=prices, values=portfolio, mode='markers+lines',
                          filename="Portfolio.html")
    line_plot.gen_plot()
