import pandas as pd
import datetime as dt


def division(val1, val2):
    # some stock data might be null
    if val2 <= 0:
        return 0
    else:
        return round((val1 / val2 - 1) * 100, 3)


class StockData:

    def __init__(self, name, current_close, previous_close,
                 current_high_low, previous_high_low,
                 current_close_open, previous_close_open) -> None:
        self.name = name
        # TODO: improve math logic - quite simple for now
        self.ROC_close = division(current_close, previous_close)
        self.ROC_high_low = division(current_high_low, previous_high_low)
        self.ROC_close_open = division(current_close_open, previous_close_open)
        self.df = pd.DataFrame.from_dict({'Date': [dt.datetime.today().strftime('%Y-%m-%d')],
                                          'Symbol': [self.name],
                                          'ROC_close': [self.ROC_close],
                                          'ROC_high_low': [self.ROC_high_low],
                                          'ROC_close_open': [self.ROC_close_open]})

    def print_all(self):
        # TODO: for debugging purposes
        print(f"{self.name}, {self.ROC_close}, {self.ROC_high_low}, {self.ROC_close_open}")
