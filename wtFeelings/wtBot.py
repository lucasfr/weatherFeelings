# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:38:42 2017

@author: lfranca
"""

from tweet import tweet
from weatherStat import weatherStat
from giphyFun import giphyFun

from threading import Thread
from time import sleep

from time import localtime, strftime

def call_at_interval(period, callback, args):
    while True:
        sleep(period)
        callback(*args)

def setInterval(period, callback, *args):
    Thread(target=call_at_interval, args=(period, callback, args)).start()

def wtBot():
    
    LATITUDE = 51.509865
    LONGITUDE = -0.118092
    message = weatherStat( LATITUDE, LONGITUDE)
    message = strftime("%H:%M", localtime()) + " | " + message
    print(message)
    giphyFun()
    tweet(message)
        
setInterval(1200, wtBot)

