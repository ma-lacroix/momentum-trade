import datetime as dt
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import src.Resources.StocksResources as Stocks
import src.Resources.PlotsResources as Plots


class MainUI(tk.Tk):
    def __init__(self, name):
        super().__init__()

        self.data_hash = None
        self.main_color = '#706767'
        self.main_font = 'Helvetica'
        self['background'] = self.main_color
        self.geometry('450x330')
        self.resizable(0, 0)
        self.title(name)
        self.img = ImageTk.PhotoImage(Image.open('images/logo.png'))

        # UI options
        paddings = {'padx': 6, 'pady': 6}
        entry_font = {'font': (self.main_font, 14)}
        self.wm_attributes("-transparent", 'False')

        # configure style
        self.style = ttk.Style(self)
        self.style.theme_use('alt')
        self.style.configure('TLabel', font=(self.main_font, 14), background=self.main_color, foreground='white')
        self.style.configure('TButton', font=(self.main_font, 14))

        # heading style
        self.style.configure('Heading.TLabel', font=(self.main_font, 12))

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # UI variables
        self.roc_timeframe = tk.IntVar()
        self.roc_timeframe.set(30)
        self.total_number_stocks = tk.IntVar()
        self.total_number_stocks.set(10)
        self.max_security_price = tk.IntVar()
        self.max_security_price.set(100)
        self.total_budget = tk.IntVar()
        self.total_budget.set(2000)
        self.end_date = tk.StringVar()
        self.end_date.set(dt.datetime.today().strftime('%Y-%m-%d'))
        self.index = tk.StringVar()
        self.index_options = ("SP500", "")  # only SP500 for the moment

        # Labels
        budget_label = ttk.Label(self, text="Total Budget:", style='TLabel')
        roc_label = ttk.Label(self, text="ROC timeframe:")
        stocks_label = ttk.Label(self, text="Securities:")
        price_label = ttk.Label(self, text="Max price:")
        end_label = ttk.Label(self, text="End date (YYYY-MM-DD):")
        index_label = ttk.Label(self, text="Stock Index:")
        logo = ttk.Label(self, image=self.img)
        logo.image = self.img

        # Entry & buttons
        budget_entry = ttk.Entry(self, textvariable=self.total_budget, **entry_font)
        roc_entry = ttk.Entry(self, textvariable=self.roc_timeframe, **entry_font)
        stocks_entry = ttk.Entry(self, textvariable=self.total_number_stocks, **entry_font)
        price_entry = ttk.Entry(self, textvariable=self.max_security_price, **entry_font)
        end_date_entry = ttk.Entry(self, textvariable=self.end_date, **entry_font)
        index_entry = ttk.OptionMenu(self, self.index, self.index_options[0], *self.index_options)
        launch_button = ttk.Button(self, text="Launch analysis", command=self.launch_app)

        # Grid
        budget_label.grid(column=0, row=1, sticky=tk.W, **paddings)
        budget_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
        roc_label.grid(column=0, row=2, sticky=tk.W, **paddings)
        roc_entry.grid(column=1, row=2, sticky=tk.E, **paddings)
        stocks_label.grid(column=0, row=3, sticky=tk.W, **paddings)
        stocks_entry.grid(column=1, row=3, sticky=tk.E, **paddings)
        price_label.grid(column=0, row=4, sticky=tk.W, **paddings)
        price_entry.grid(column=1, row=4, sticky=tk.E, **paddings)
        end_label.grid(column=0, row=5, sticky=tk.W, **paddings)
        end_date_entry.grid(column=1, row=5, sticky=tk.E, **paddings)
        index_label.grid(column=0, row=6, sticky=tk.W, **paddings)
        index_entry.grid(column=1, row=6, sticky=tk.E, **paddings)
        launch_button.grid(column=1, row=7, sticky=tk.E, **paddings)
        logo.grid(column=0, row=7, sticky=tk.W, **paddings)

    def gen_hash(self):
        try:
            self.data_hash = {
                'roc_timeframe': self.roc_timeframe.get(),
                'total_stocks': self.total_number_stocks.get(),
                'max_security_price': self.max_security_price.get(),
                'total_budget': self.total_budget.get(),
                'end_date': self.end_date.get(),
                'index': self.index
            }
        except ValueError as err:
            print(f"Enter integers only - {str(err)}")

    def launch_app(self):
        self.gen_hash()
        end = self.data_hash['end_date']
        # Stocks.get_sp500_tickers()
        # Stocks.get_sp500_prices(Stocks.get_last_update(end), end)
        # Stocks.get_roc(self.data_hash['roc_timeframe'], end)
        # Stocks.get_sharpe(end, self.data_hash['total_stocks'], self.data_hash['max_security_price'])
        # Stocks.gen_portfolio(self.data_hash['total_budget'])
        # Stocks.gen_portfolio_performance()
        Plots.plot_portfolio()
