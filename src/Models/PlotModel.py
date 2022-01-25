import plotly.offline as pyo
import plotly.graph_objs as go


class StockPlot:

    def __init__(self, title, x, y, mode, filename):
        self.title = title
        self.x = x
        self.y = y
        self.mode = mode
        self.filename = filename

    def gen_plot(self):
        trace = go.Scatter(
            x=self.x,
            y=self.y,
            mode=self.mode
        )
        lay = go.Layout(
            title=self.title
        )
        fig = go.Figure(data=trace, layout=lay)
        pyo.plot(fig, filename=self.filename)
