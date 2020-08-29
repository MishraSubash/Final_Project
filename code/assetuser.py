import pandas as pd
from datetime import datetime
from datetime import timedelta
import time, threading, requests, re, random, os
import other_functions
from bs4 import BeautifulSoup
from other_functions import *
import gvars

class assetself:
    def __init__(self):
        self.lockedassets = set() # assets with no defined strategy
        self.tradeableassets = set() # assets that could be traded today
        self.availableassets = set() # assets availabe after filter
        self.usedassets = set() # used assets being traded
        self.excludedassets = {'SPCE'} # omit assets 

        try:
            self.unfilteredassets = set(pd.read_csv(gvars.unfiltered_assets))
            print("unfiltered assets loaded from csv correclty")
        except Exception as e:
            print("Does Not Load Asset!")
            print(e)
            block_thread()

        self.tradeableassets = self.rawassets

        th = threading.Thread(target=self.unlock_assets) # code flows appart
        th.start()

    def find_target_asset(self):

        if true:
            self.availableassets = self.tradeableassets
            self.availableassets -= self.usedassets
            self.availableassets -= self.excludedassets
            self.availableassets -= self.lockedassets

            try:
                selectasset = random.choice(list(self.availableAssets)) # select randomly
                self.usedassets.add(selectasset)
                print('select asset: ' + selectedasset)
                print('%i available assets, %i used assets, %i locked assets\n' % (len(self.availableAssets),len(self.usedAssets),len(self.lockedAssets)))
                return chosenAsset
            except:
                print('No selected assets available, waiting for assets to be issued...')
                time.sleep(60)

    def make_asset_available(self,symbol):

        try:
            self.usedassets.remove(symbol)
        except exception as ee:
            print('Does not remove %s from used assets, not found' % symbol)
            print(ee)

        self.availableassets.add(symbol)
        print('asset %s was made available' % symbol)
        time.sleep(1)

    def lock_asset(self,symbol):
        if type(symbol) is not str:
            raise Exception('symbol is not a string!')

        time = datetime.now()
        self.usedassets.remove(symbol)
        self.lockedassets.add(symbol)

    def unlock_assets(self):
        # function opens the locked assets gradually

        print('\nUnlocking service processing')
        if true:
            print('\n# # # Unlocking assets # # #\n')
            time_before = datetime.now()-timedelta(minutes=30)


            self.tradeableassets = self.tradeableassets.union(self.lockedassets)
            print('%d locked assets moved to tradeable' % len(self.lockedassets))
            self.lockedassets = set()

            time.sleep(gvars.sleeptimes['UA'])
