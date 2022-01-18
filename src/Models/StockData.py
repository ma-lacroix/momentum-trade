# Stock class holding ROC values

class StockData:

    def __init__(self, name, current_price, previous_price) -> str:
        self.name = name
        # TODO: ROC might be calculated better and/or with different variables
        self.ROC = round((current_price/previous_price-1)*100, 3)