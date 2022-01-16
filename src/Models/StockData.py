# Stock class holding ROC values

class Stock:
    
    def __init__(self,name,current_price,previous_price) -> None:
        self.name = name
        self.ROC = round((current_price/previous_price-1)*100,3)