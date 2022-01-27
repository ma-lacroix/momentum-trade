from plotly.subplots import make_subplots
import plotly.offline as pyo
import plotly.graph_objs as go


# TODO: think about graph types and classes
class StockPlot:

    def __init__(self, title, prices, roc, mode, filename):
        self.title = title
        self.prices = prices
        self.roc = roc
        self.mode = mode
        self.filename = filename

    def gen_plot(self):
        symbols = list(self.prices.Symbol.unique())
        # TODO: make 'fig' customizable in the class
        fig = make_subplots(rows=2,
                            cols=2,
                            column_widths=[0.7, 0.3],
                            row_width=[0.3, 0.7],
                            horizontal_spacing=0.05,
                            vertical_spacing=0.1,
                            specs=[[{}, {}], [{"colspan": 2}, None]],
                            subplot_titles=['Daily Close', 'Daily Volumes', 'ROC Close'])
        for symbol in symbols:
            fig.add_trace(go.Scatter(
                    x=self.prices[self.prices.Symbol == symbol].Date,
                    y=self.prices[self.prices.Symbol == symbol].Close,
                    mode=self.mode,
                    name=symbol,
                    legendgroup='one'),
                row=1,
                col=1
            )
            fig.add_trace(go.Scatter(
                    x=self.prices[self.prices.Symbol == symbol].Date,
                    y=self.prices[self.prices.Symbol == symbol].Volume,
                    mode=self.mode,
                    name=symbol,
                    legendgroup='one',
                    showlegend=False),
                row=1,
                col=2
            )
        fig.add_trace(go.Bar(
            x=self.roc.Symbol,
            y=self.roc.roc_close,
            showlegend=False),
            row=2,
            col=1
        )
        fig.update_layout(title_text=self.title)
        pyo.plot(fig, filename=self.filename)
