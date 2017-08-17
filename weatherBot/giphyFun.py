# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 12:48:55 2017

@author: lfranca
"""

import urllib
import safygiphy

def giphyFun():
    g = safygiphy.Giphy()
    r = g.random(tag="happy")
    link = r['data']['image_url']
    urllib.request.urlretrieve(link,"haha.gif")
    
    return