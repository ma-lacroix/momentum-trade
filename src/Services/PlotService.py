from src.Models.PlotModel import StockPlot


def gen_line_plot(prices, roc_values):
    line_plot = StockPlot(title="Mock ROC report", prices=prices, roc=roc_values, mode='markers+lines',
                          filename="testPlot.html")
    line_plot.gen_plot()
