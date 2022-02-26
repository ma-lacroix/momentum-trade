import datetime as dt
import tkinter as tk
from tkinter import ttk
import src.Resources.StocksResources as Stocks
import src.Resources.PlotsResources as Plots


# TODO: clean this class up!
class MainUI(tk.Tk):
    def __init__(self, name):
        super().__init__()

        self.data_hash = None
        self.main_color = '#CEC4C2'
        self['background'] = self.main_color
        self.geometry('450x330')
        self.resizable(0, 0)
        self.title(name)

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 14)}
        self.wm_attributes("-transparent", 'False')

        # configure style
        self.style = ttk.Style(self)
        self.style.theme_use('alt')
        self.style.configure('TLabel', font=('Helvetica', 18), background=self.main_color)
        self.style.configure('TButton', font=('Helvetica', 18))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 20))

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.roc_timeframe = tk.IntVar()
        self.total_number_stocks = tk.IntVar()
        self.max_security_price = tk.IntVar()
        self.total_budget = tk.IntVar()

        # Labels
        heading = ttk.Label(self, text='Generate Report', style='Heading.TLabel')
        budget_label = ttk.Label(self, text="Total Budget:")
        roc_label = ttk.Label(self, text="ROC timeframe:")
        stocks_label = ttk.Label(self, text="Securities:")
        price_label = ttk.Label(self, text="Max price:")

        # Entry & buttons
        budget_entry = ttk.Entry(self, textvariable=self.total_budget, **entry_font)
        roc_entry = ttk.Entry(self, textvariable=self.roc_timeframe, **entry_font)
        stocks_entry = ttk.Entry(self, textvariable=self.total_number_stocks, **entry_font)
        price_entry = ttk.Entry(self, textvariable=self.max_security_price, **entry_font)
        entry_button = ttk.Button(self, text="Submit", command=self.gen_hash)
        launch_button = ttk.Button(self, text="Launch app", command=self.launch_app)

        # Grid
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)
        budget_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        budget_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
        roc_label.grid(column=0, row=2, sticky=tk.W, **paddings)
        roc_entry.grid(column=1, row=2, sticky=tk.E, **paddings)
        stocks_label.grid(column=0, row=3, sticky=tk.W, **paddings)
        stocks_entry.grid(column=1, row=3, sticky=tk.E, **paddings)
        price_label.grid(column=0, row=4, sticky=tk.W, **paddings)
        price_entry.grid(column=1, row=4, sticky=tk.E, **paddings)
        entry_button.grid(column=1, row=5, sticky=tk.E, **paddings)
        launch_button.grid(column=1, row=6, sticky=tk.E, **paddings)

    def gen_hash(self):
        self.data_hash = {
            'roc_timeframe': self.roc_timeframe.get(),
            'total_stocks': self.total_number_stocks.get(),
            'max_security_price': self.max_security_price.get(),
            'total_budget': self.total_budget.get()
        }

    def launch_app(self):
        # TODO: add some data verification here
        print(f"Starting project {dt.datetime.today().strftime('%Y-%m-%d')}")
        end = '2022-02-18'
        Stocks.get_sp500_tickers()
        Stocks.get_sp500_prices(Stocks.get_last_update(end), end)
        Stocks.get_roc(self.data_hash['roc_timeframe'], end)
        Stocks.get_sharpe(end, self.data_hash['total_stocks'], self.data_hash['max_security_price'])
        Stocks.gen_portfolio(self.data_hash['total_budget'])
        Stocks.gen_portfolio_performance()
        Plots.plot_portfolio()

