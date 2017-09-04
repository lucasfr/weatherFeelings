# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:51:43 2017

@author: lfranca
"""
# THIS SCRIPT GENERATES THE secret.py FILE THAT CONTAINS THE API KEYS
# (PLEASE, INSERT THE KEYS WITH QUOTATION MARKS)

consumer_key = str(input("CONSUMER_KEY: "))
consumer_secret = str(input("CONSUMER_SECRET: "))
access_key = str(input("ACCESS_KEY: "))
access_secret = str(input("ACCESS_SECRET: "))


f = open('secret.py', 'w')

f.write('CONSUMER_KEY = "' + CONSUMER_KEY + '"\n')
f.write('CONSUMER_SECRET = "' + CONSUMER_SECRET + '"\n')
f.write('ACCESS_KEY = "' + ACCESS_KEY + '"\n')
f.write('ACCESS_SECRET = "' + ACCESS_SECRET + '"\n')

f.close()