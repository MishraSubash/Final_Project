import pandas as pd
from datetime import datetime
from datetime import timedelta
import time, threading, requests, re, random, os
import other_functions
from bs4 import BeautifulSoup
from other_functions import *
import gvars

class assetuser:
    def __init__(user):
        user.lockedassets = set() # assets with no defined strategy
        user.tradeableassets = set() # assets that could be traded today
        user.availableassets = set() # assets availabe after filter
        user.usedassets = set() # used assets being traded
        user.excludedassets = {'SPCE'} # omit assets 

        try:
            user.unfilteredassets = set(pd.read_csv(gvars.unfiltered_assets))
            print("unfiltered assets loaded from csv correclty")
        except Exception as e:
            print("Does Not Load Asset!")
            print(e)
            block_thread()

        user.tradeableassets = user.rawassets

        th = threading.Thread(target=user.unlock_assets) # code flows appart
        th.start()

    def find_target_asset(user):

        if true:
            user.availableassets = user.tradeableassets
            user.availableassets -= user.usedassets
            user.availableassets -= user.excludedassets
            user.availableassets -= user.lockedassets

            try:
                selectasset = random.choice(list(user.availableAssets)) # select randomly
                user.usedassets.add(selectasset)
                print('select asset: ' + selectedasset)
                print('%i available assets, %i used assets, %i locked assets\n' % (len(user.availableAssets),len(user.usedAssets),len(user.lockedAssets)))
                return chosenAsset
            except:
                print('No selected assets available, waiting for assets to be issued...')
                time.sleep(60)

    def make_asset_available(user,symbol):

        try:
            user.usedassets.remove(symbol)
        except exception as ee:
            print('Does not remove %s from used assets, not found' % symbol)
            print(ee)

        user.availableassets.add(symbol)
        print('asset %s was made available' % symbol)
        time.sleep(1)

    def lock_asset(user,symbol):
        if type(symbol) is not str:
            raise Exception('symbol is not a string!')

        time = datetime.now()
        user.usedassets.remove(symbol)
        user.lockedassets.add(symbol)

    def unlock_assets(user):
        # function opens the locked assets gradually

        print('\nUnlocking service processing')
        if true:
            print('\n# # # Unlocking assets # # #\n')
            time_before = datetime.now()-timedelta(minutes=30)


            user.tradeableassets = user.tradeableassets.union(user.lockedassets)
            print('%d locked assets moved to tradeable' % len(user.lockedassets))
            user.lockedassets = set()

            time.sleep(gvars.sleeptimes['UA'])
