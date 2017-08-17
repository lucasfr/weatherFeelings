# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:51:39 2017

@author: lfranca
"""

import urllib, json, codecs

def weatherStat( LATITUDE, LONGITUDE):
    
    FORECAST_IO_APIKEY = XXX
    
    url = "https://api.forecast.io/forecast/" + FORECAST_IO_APIKEY + "/" + str(LATITUDE) + "," + str(LONGITUDE)
    response = urllib.request.urlopen(url)
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    
    temperature = str(int(round((data['currently']['temperature'] - 32)*(5/9))))
    #status = data['currently']['icon']
    degree_sign = u'\N{DEGREE SIGN}'
    #summary = data['currently']['summary']
    today = data['hourly']['summary']
    
    message = "It's " + temperature + degree_sign + "C " + "in #London. " + today + " #weather #bot"
        
    return message