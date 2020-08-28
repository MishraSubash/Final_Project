from stocklib import *
from traderlib import *
from other_functions import *
import threading, os, logging
from datetime import datetime
import gvars
from assetuser import assetuser
from pytz import timezone

# world object we log to; the user will work with log descriptions
_L = logging.getLogger("demo")

# make a unique logger that logs to per-thread-name files
class multiuser(logging.user):
    def __init__(user, dirname):
        super(multiuser, user).__init__()
        user.files = {}
        user.dirname = dirname
        if not os.access(dirname, os.W_OK):
            raise Exception("Directory %s not writeable" % dirname)

    def flush(user):
        user.acquire()
        try:
            for fp in list(user.files.values()):
                fp.flush()
        finally:
            user.release()

    def _get_or_open(user, key):
        # Get the file pointer for the given key, or else open the file
        user.acquire()
        try:
            if key in user.files:
                return user.files[key]
            else:
                fp = open(os.path.join(user.dirname, "%s.log" % key), "a")
                user.files[key] = fp
                return fp
        finally:
            user.release()

    def emit(user, record):
        # No lock here; following code for streamuser and fileuser
        try:
            fp = user._get_or_open(record.threadName)
            msg = user.format(record)
            fp.write('%s\n' % msg)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            user.handleError(record)

def clean_open_orders(api):
    # First, cancel any existing orders so they don't impact our buying power.
    orders = api.list_orders(status="open")

    print('\nCLEAR ORDERS')
    print('%i orders were found open' % int(len(orders)))

    for order in orders:
      api.cancel_order(order.id)

def review_account_ok(api):

    account = api.get_account()
    if account.account_blocked or account.trading_blocked or account.transfers_blocked:

        print('OJO, account blocked. WTF?')
        import pdb; pdb.set_trace()

def run_tbot(_L,assHand,account):

    # initialize trader object
    trader = Trader(gvars.API_KEY, gvars.API_SECRET_KEY, _L, account)

    while True:

        ticker = assHand.find_target_asset()
        stock = Stock(ticker)

        ticker,lock = trader.run(stock) # run the trading program

        if lock: # if the trend is not favorable, lock it temporarily
            assHand.lock_asset(ticker)
        else:
            assHand.make_asset_available(ticker)

def main():

    # Set up a basic std erro logging; this is nothing fancy.
    log_format = '%(asctime)s %(threadName)12s: %(lineno)-4d %(message)s'
    stderror_ = logging.streamuser()
    stderror_user.setFormatter(logging.Formatter(log_format))
    logging.getLogger().adduser(stderror_user)

    # Set up a logger that creates one file per thread
    todayLogsPath = create_log_folder(gvars.LOGS_PATH)
    multi_user = multiuser(todayLogsPath)
    multi_user.setformatter(logging.formatter(log_format))
    logging.getlogger().adduser(multi_user)

    # Set default log level, log a message
    _L.setLevel(logging.DEBUG)
    _L.info("\n\n\nRun initiated")
    _L.info('Max workers allowed: ' + str(gvars.MAX_WORKERS))

    # initialize the API with Alpaca
    api = tradeapi.REST(gvars.API_KEY, gvars.API_SECRET_KEY, gvars.ALPACA_API_URL, api_version='v2')

    # initialize the asset user
    assuser = assetuser()

    # get the Alpaca account 
    try:
        _L.info("Getting account")
        review_account_ok(api) # review if it is ok to trade
        account = api.get_account()
        clean_open_orders(api) # clean all the open orders
        _L.info("Got it")
    except Exception as e:
        _L.info(str(e))

    for thread in range(gvars.MAX_WORKERS): # this will launch the threads
        maxwork = 'th' + str(thread) # establishing each worker name

        maxwork = threading.Thread(name=worker,target=run_tbot,args=(_L,assuser,account))
        maxwork.start() # it runs a run_tbot function, defined here

        time.sleep(1)

if __name__ == '__main__':
    main()
