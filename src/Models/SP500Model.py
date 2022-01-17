import os
import pandas as pd


class SP500:

    def __init__(self):
        self.command = 'curl -o tickers/sp500.csv -LJO https://raw.githubusercontent.com/datasets/\
                                    s-and-p-500-companies/master/data/constituents.csv'
        self.tickers = self.get_tickers()

    def get_tickers(self):
        os.system('mkdir tickers')
        os.system(self.command)
        df = pd.read_csv('tickers/sp500.csv')
        os.system('rm -r tickers constituents.csv')
        return df
