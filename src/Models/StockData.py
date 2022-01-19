import math
import pandas as pd
import datetime as dt


def division(val1, val2):
    # some stock data might be null
    if val2 <= 0:
        return 0
    else:
        return round((val1 / val2 - 1) * 100, 3)


class StockData:

    def __init__(self, name, start_date, end_date, current_close, previous_close,
                 current_high_low, previous_high_low,
                 current_close_open, previous_close_open,
                 avg_daily_change) -> None:
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.ROC_close = division(current_close, previous_close)
        self.ROC_high_low = division(current_high_low, previous_high_low)
        self.ROC_close_open = division(current_close_open, previous_close_open)
        self.ROC_close_open_log10 = math.log10(abs(division(current_close_open, previous_close_open)))
        self.ROC_avg_daily_change = avg_daily_change
        self.ROC_avg_daily_change_log10 = math.log10(avg_daily_change)
        self.df = pd.DataFrame.from_dict({'Results_date': [dt.datetime.today().strftime('%Y-%m-%d')],
                                          'Symbol': [self.name],
                                          'Start_date': [self.start_date],
                                          'End_date': [self.end_date],
                                          'ROC_close': [self.ROC_close],
                                          'ROC_high_low': [self.ROC_high_low],
                                          'ROC_close_open': [self.ROC_close_open],
                                          'ROC_close_open_log10': [self.ROC_close_open_log10],
                                          'ROC_avg_daily_change': [self.ROC_avg_daily_change],
                                          'ROC_avg_daily_change_log10': [self.ROC_avg_daily_change_log10]
                                          })

    def print_all(self):
        # TODO: for debugging purposes
        print(f"{self.name}, {self.ROC_close}, {self.ROC_high_low}, {self.ROC_close_open}")
