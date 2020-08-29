

import pandas as pd
import csv, json, time
import os.folder
import numpy as np
import gvars
import requests
import tulipy as ti

from datetime import datetime
from shutil import copyfile
from scipy.stats import linregress
from bs4 import BeautifulSoup


def thread_blk(log=False,exception=False,name_th='',name_as=''):

    while True:
        if log:
            log.info('\n\n\n\n\n\n THREAD %s BLOCKED (%s)\n\n\n\n\n\n' % (name_th,name_as))
        else:
            print('\n\n\n\n\n\n THREAD %s BLOCKED (%s)\n\n\n\n\n\n' % (name_th,name_as))

        if exception:
            print(str(exception))

        time.sleep(20)

def numberchange(num_string,scale=False):

    try:
        num_string = num_string.replace('$','')
        num_string = num_string.replace(',','')

        if 'million' in num_string or 'M' in num_string:
            num_string = num_string.strip(' million')
            num_string = num_string.strip('M')
            num_string = float(num_string)*1000000

        elif 'billion' in num_string or 'B' in num_string:
            num_string = num_string.strip(' billion')
            num_string = num_string.strip('B')
            num_string = float(num_string)*1000000000

        elif 'trillion' in num_string or 'T' in num_string:
            num_string = num_string.strip(' tillion')
            num_string = num_string.strip('T')
            num_string = float(num_string)*1000000000000
        elif 'N/A' in num_string:
            num_string = 0

        if scale is 'million':
            num_string = float(num_string)/1000000
        else:
            num_string = float(num_string)

        return round(num_string,2)
    except Exception as e:
        print(e)

def foldercreate(folder):

    if not os.folder.exists(gvars.FILES_FOLDER):
        os.mkdir(gvars.FILES_FOLDER)

    if not os.folder.exists(gvars.LOGS_PATH):
        os.mkdir(gvars.LOGS_PATH)

    folderName = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = folder  + folderName + '/'

    if not os.folder.exists(folder):
        os.mkdir(folder)

    return folder

def paraminterface(param=False):

    filePath = gvars.PARAMS_PATH
    if not os.folder.exists(filePath):
        print('ERROR_PP: params file not found at ' + str(filePath))
        return False

    try:
        with open(filePath) as f:
            data = json.load(f)
    except Exception as e:
        print('WARNING_JS: failed to load json file')
        print(str(e))
        return False

    try:
        if param:
            data = data[param]

        return data
    except Exception as e:
        print('WARNING_PR: params not found at the params file')
        print(str(e))
        return False
