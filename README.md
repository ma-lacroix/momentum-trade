# Momentum trading with ROC and Sharpe ratios
###### NOTE: WIP

This application will pull stock tickers from popular indexes & closing prices, return their associated _rate of change_ values, simulates portfolio allocation and picks the one with the best _Sharpe ratio_.

The application does not send any trade requests, it only makes recommendations. 

**DISCLAIMER**: For educational purposes only. I am not responsible for the actions you take with the data this application produces.   

## How to use on MacOS

1. Make sure you have Python 3.8 (or later) & pip 22 (or later) installed.
2. 4. Make sure you are using Clang 13 or above `gcc -v` (though you should be good with earlier versions)
3. Clone the repo. 
4. From the repo folder: `pip install -r requirements.txt`.
5. You'll need a GCP SA key, which you can add as an environment variable in your bash profile: `gcp_key=[YOUR KEY]` If you are using an IDE like Pycharm, you can add this key value in your run configuration file. 
6. Run the main application file: `python MainApplication.py`.
7. Invest at your own risk. I do not recommend you take investment advice from someone on the internet.