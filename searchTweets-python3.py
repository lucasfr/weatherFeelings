#!/usr/bin/env python

from __future__ import print_function
from secret import *
import twitter

# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

results = api.GetSearch(raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")

print(results)

#print([u.Text for u in users])