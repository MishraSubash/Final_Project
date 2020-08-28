from pathlib import Path
from datetime import datetime

total_stocks = 10 # max threads at a time

profitratio = 2.5 # gainprofit = -stopLoss*profitRatio
stoplossmargin = 0.25 # margin for the stop loss

totalequity = 10000 # sets the target amount per execution
limitOrderMargin = 0.1# sets the offset for the limit orders

# ALPACA API Key below
API_KEY = "PKASYJ8SHB9WRGQL6KKV"
API_SECRET_KEY = "P9RJXsrD4qtOl0IBj32RfZmgOMm/uApZZTFeYewg"
ALPACA_API_URL = "https://paper-api.alpaca.markets"

if API_KEY is "" or API_SECRET_KEY is "":
    print('\n\n##### \n\nPlease get an API key at the Alpaca website! \n\n##### \n\n')
    raise ValueError

################################################################ ATTEMPTS ->
# max iteration attempts
maxAttempts = {
            'EO':10, # enter order
            'AP':10, # analyze oosition
            'CO':10, # cancel order
            'GP':10, # get position
            'FA':6, # fetch asset 
            'UHD1':10, # upload historical dagta 1
            'UHD2':20 # upload historical data 2
            }

# limit for the indicators
limStoch = {
            'maxbuy':150, # max amount to buy
            'minsell':50  # min amount to sell
            }

################################################################ TIMEFRAMES ->
# fetch historical data intervals
fetchinterval = {
            'little':'10Min',
            'big':'60Min'
            }

timeouts = {
        'operation':80*120*120, # main operation
        'posEntered':16*120*120, # position entered
        'GT':0 # if 0, remove erroneous trend immediately
        }

# wait time for each iteration
sleeptimes = {
                'operation':120,
                'GD': 20*120, # general direction
                'ID': 4*120, # instant direction
                'RS': 120, # RSI
                'GA': 6, # grab assets
                'SM': 120, # stochastic every min
                'CO': 20, # check order every 20 sec
                'SO': 10, # submit order every 10 sec
                'LH': 10, # load_historical_data
                'PG': 20, # price grab (current price)
                'CP': 20, # check position, check if it entered
                'GS': 120, # find slope of position
                'UA': 20*120, # unlock assets
                'CL': 4
                }

################################################################ PATHS ->
home = str(Path.home())

FILES_FOLDER = home + '/tbot_files/'
RAW_ASSETS = './_raw_assets.csv'
LOGS_PATH = FILES_FOLDER + 'logs/'

################################################################ ASSET PARAMS ->
# filtering parameters at the asset handler
filterParams = {
    'MIN_SHARE_PRICE':30, #dollars
    'MIN_AVG_VOL':0.5, #millions of dollars
    }
