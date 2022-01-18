from pkgutil import get_data
import pandas as pd
import numpy as np
from pandas_datareader import data as dr


class YahooResponse:

    def __init__(self, security, start, end) -> None:
        self.service = 'yahoo'
        self.security = security
        self.start = start
        self.end = end
        self.df = self.get_data()

    def get_data(self):
        df = pd.DataFrame()
        try:
            df = np.round(dr.DataReader(self.security, self.service, self.start, self.end)
                          [['High', 'Low', 'Open', 'Close', 'Volume']], 2)\
                .reset_index()
            df['Symbol'] = self.security
            df['Date'] = pd.to_datetime(df['Date']).dt.date
        except ValueError as err:
            print(f"Couldn't get {self.security}: {err}")
        finally:
            return df
