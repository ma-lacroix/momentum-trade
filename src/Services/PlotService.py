from src.Models.PlotModel import StockLinePlot


def gen_line_plot(df):
    line_plot = StockLinePlot(title="Testing Plotly", data=df, mode='markers+lines',
                              filename="testPlot.html")
    line_plot.gen_plot()
