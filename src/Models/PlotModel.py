from plotly.subplots import make_subplots
import plotly.offline as pyo
import plotly.graph_objs as go


# TODO: think about graph types and classes
class StockPlot:

    def __init__(self, title, prices, values, performance, mode, filename):
        self.title = title
        self.prices = prices
        self.values = values
        self.performance = performance
        self.mode = mode
        self.filename = filename
        self.symbols = list(self.prices.Symbol.unique())

    def gen_plot(self):
        # TODO: make 'fig' customizable in the class
        fig = make_subplots(rows=2,
                            cols=2,
                            column_widths=[0.5, 0.5],
                            row_width=[0.5, 0.5],
                            horizontal_spacing=0.05,
                            vertical_spacing=0.1,
                            specs=[[{}, {}], [{}, {}]],
                            subplot_titles=['Suggested Securities', 'Daily Closes', 'ROC Close',
                                            'Suggested Portfolio Performance'])
        fig.add_trace(go.Bar(
            x=self.values.Securities,
            y=self.values.Symbol,
            orientation='h',
            showlegend=False),
            row=1,
            col=1
        )
        for symbol in self.symbols:
            fig.add_trace(go.Scatter(
                x=self.prices[self.prices.Symbol == symbol].Date,
                y=self.prices[self.prices.Symbol == symbol].Close,
                mode=self.mode,
                name=symbol,
                showlegend=True),
                row=1,
                col=2
            )
        fig.add_trace(go.Bar(
            x=self.values.roc_close,
            y=self.values.Symbol,
            orientation='h',
            showlegend=False),
            row=2,
            col=1
        )
        fig.add_trace(go.Scatter(
            x=self.performance.Date,
            y=self.performance.Performance,
            showlegend=False),
            row=2,
            col=2
        )
        fig.update_layout(title_text=self.title, title_x=0.5,
                          font_family="verdana",
                          font_color="grey",
                          title_font_family="arial",
                          title_font_color="black",
                          title_font_size=26)
        fig.layout.images = [dict(
            source="https://raw.githubusercontent.com/ma-lacroix/momentum-trade/main/images/logo.png",
            xref="paper", yref="paper",
            x=0.12, y=1.17,
            sizex=0.15, sizey=0.15,
            xanchor="right", yanchor="top"
        )]
        pyo.plot(fig, filename=self.filename)
