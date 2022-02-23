import tkinter as tk
from tkinter import ttk


class MainUI(tk.Tk):
    # TODO: clean this up
    def __init__(self, name):
        super().__init__()

        self.geometry('300x300')
        self.resizable(0, 0)
        self.title = name

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 14)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.roc_timeframe = tk.StringVar()
        self.total_number_stocks = tk.StringVar()
        self.max_security_price = tk.StringVar()
        self.total_budget = tk.StringVar()

        heading = ttk.Label(self, text='Generate Report', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        budget_label = ttk.Label(self, text="Total Budget:")
        budget_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        budget_entry = ttk.Entry(self, textvariable=self.total_budget, **entry_font)
        budget_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

        roc_label = ttk.Label(self, text="Total Budget:")
        roc_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        roc_entry = ttk.Entry(self, textvariable=self.roc_timeframe, **entry_font)
        roc_entry.grid(column=1, row=2, sticky=tk.E, **paddings)
        #
        stocks_label = ttk.Label(self, text="Total Budget:")
        stocks_label.grid(column=0, row=3, sticky=tk.W, **paddings)

        stocks_entry = ttk.Entry(self, textvariable=self.total_number_stocks, **entry_font)
        stocks_entry.grid(column=1, row=3, sticky=tk.E, **paddings)
        #
        price_label = ttk.Label(self, text="Total Budget:")
        price_label.grid(column=0, row=4, sticky=tk.W, **paddings)

        price_entry = ttk.Entry(self, textvariable=self.max_security_price, **entry_font)
        price_entry.grid(column=1, row=4, sticky=tk.E, **paddings)
        # login button
        login_button = ttk.Button(self, text="Login", command=self.print_something)
        login_button.grid(column=1, row=5, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 14))
        self.style.configure('TButton', font=('Helvetica', 14))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 16))

    def print_something(self):
        print(f"{self.title} - {self.roc_timeframe} - {self.total_number_stocks} - {self.total_budget} \
                {self.max_security_price}")
