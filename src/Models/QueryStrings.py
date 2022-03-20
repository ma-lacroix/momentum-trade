class QueryStrings:

    def __init__(self, start_date='2022-01-01', top=10, pivot_list=[''], max_price=5000):
        self.max_date = "SELECT MAX(Date) AS max_date FROM `tickers.prices`"
        self.tickers = "SELECT DISTINCT(Symbol) as Symbol FROM `tickers.sp500` ORDER BY 1"
        self.roc_data = f"""
            -- Using MIN row value as Yahoo sometimes returns more than a single row per stock
            SELECT
                Date, Symbol, MIN(High) AS High, MIN(Low) AS Low, MIN(Open) AS Open, 
                MIN(Close) AS Close, MIN(Volume) AS Volume 
            FROM `mythical-harbor-167208.tickers.prices`  
            WHERE Date >= '{start_date}'
            GROUP BY 1,2
            """
        self.unique_symbols = f"""
            SELECT Symbol AS Symbols FROM
                (SELECT Symbol FROM `tickers.roc_values`
                WHERE Compute_date = CAST(current_date() AS STRING)
                AND close <= {max_price} 
                ORDER BY roc_close DESC) 
            LIMIT {top}"""
        self.portfolio = """
            WITH last_close AS (
              SELECT t1.Symbol AS Symbol, t1.Date AS Date, Close
              FROM `tickers.prices` t1
              JOIN (SELECT Symbol, MAX(Date) AS Date FROM `tickers.prices` GROUP BY 1) t2
              ON t1.Symbol = t2.Symbol AND t1.Date = t2.Date
            ), roc_values AS (
              SELECT t1.Symbol AS Symbol, roc_close, roc_avg_daily_change_log10
              FROM `tickers.roc_values` t1
              JOIN (SELECT Symbol, MAX(End_date) AS Date FROM `tickers.roc_values` GROUP BY 1) t2
              ON t1.Symbol = t2.Symbol AND t1.End_date = t2.Date
            ), sharpe_values AS (
              SELECT Symbol, Sharpe FROM `tickers.sharpe_values` 
            )
            SELECT * FROM sharpe_values JOIN (SELECT * FROM roc_values) USING(Symbol) 
                JOIN (SELECT * FROM last_close) USING(Symbol) ORDER BY Sharpe DESC
            """
        self.portfolio_performance = "SELECT t1.Date AS Date, ROUND(SUM(t1.Close*Securities),2) AS Performance " \
                                     "FROM `tickers.prices` t1 JOIN `tickers.portfolio` t2 " \
                                     "USING(Symbol) GROUP BY 1 ORDER BY 1"
        self.plot_prices = "SELECT * FROM tickers.prices t1 JOIN `tickers.portfolio` t2 " \
                           "USING(Symbol) ORDER BY t1.Date"
        self.plot_portfolio = "SELECT * FROM tickers.portfolio ORDER BY Securities"
        self.plot_portfolio_performance = "SELECT * FROM tickers.portfolio_performance ORDER BY 1"
