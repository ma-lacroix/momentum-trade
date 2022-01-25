from src.Models.PlotModel import StockPlot


def gen_line_plot(df):
    line_plot = StockPlot(title="Testing Plotly", x=df.Date,
                          y=df.Close, mode='markers+lines',
                          filename="testPlot.html")
    line_plot.gen_plot()
