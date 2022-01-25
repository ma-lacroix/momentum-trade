import plotly.offline as pyo
import plotly.graph_objs as go


# TODO: think about graph types and classes
class StockLinePlot:

    def __init__(self, title, data, mode, filename):
        self.title = title
        self.data = data
        self.mode = mode
        self.filename = filename

    def gen_plot(self):
        symbols = list(self.data.Symbol.unique())
        for symbol in symbols:
            print(self.data[self.data.Symbol == symbol].Close)
        traces = [go.Scatter(
            x=self.data[self.data.Symbol == symbol].Date,
            y=self.data[self.data.Symbol == symbol].Close,
            mode=self.mode,
            name=symbol
        ) for symbol in symbols]
        lay = go.Layout(
            title=self.title
        )
        fig = go.Figure(data=traces, layout=lay)
        pyo.plot(fig, filename=self.filename)
