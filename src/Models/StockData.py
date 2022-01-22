import pandas as pd
import datetime as dt


class StockData:

    def __init__(self, name, start_date, end_date, roc_close, roc_high_low, roc_close_open,
                 roc_close_open_log10, roc_avg_daily_change, roc_avg_daily_change_log10) -> None:
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.roc_close = roc_close
        self.roc_high_low = roc_high_low
        self.roc_close_open = roc_close_open
        self.roc_close_open_log10 = roc_close_open_log10
        self.roc_avg_daily_change = roc_avg_daily_change
        self.roc_avg_daily_change_log10 = roc_avg_daily_change_log10
        self.df = pd.DataFrame.from_dict({'Compute_date': [dt.datetime.today().strftime('%Y-%m-%d')],
                                          'Symbol': [self.name],
                                          'Start_date': [self.start_date],
                                          'End_date': [self.end_date],
                                          'roc_close': [self.roc_close],
                                          'roc_high_low': [self.roc_high_low],
                                          'roc_close_open': [self.roc_close_open],
                                          'roc_close_open_log10': [self.roc_close_open_log10],
                                          'roc_avg_daily_change': [self.roc_avg_daily_change],
                                          'roc_avg_daily_change_log10': [self.roc_avg_daily_change_log10]
                                          })

    def print_all(self):
        # TODO: for debugging purposes
        print(f"{self.name}, {self.roc_close}, {self.roc_high_low}, {self.roc_close_open}")
