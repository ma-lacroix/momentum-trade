from pkgutil import get_data
import pandas as pd
import numpy as np
from pandas_datareader import data as dr

class YahooRequest:

    def __init__(self,security,start,end) -> str:
        self.service = 'yahoo'
        self.security = security
        self.start = start
        self.end = end
        self.df = self.get_data()
    
    def get_data(self):
        try:
            df = np.round(dr.DataReader(self.security,self.service,self.start,self.end),2)
        except dr.RemoteDataError:
            print("Data not found at Ticker {}".format(self.security))
        return df
