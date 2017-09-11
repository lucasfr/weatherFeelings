#!/usr/bin/env python

# Likely to add all functions on this file

from __future__ import print_function
from secret import *
import twitter

def SearchTweets(latitude, longitude):
    # Create an Api instance.
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    results = api.GetSearch(
        raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")

    # Print tweet text for each result (better to return as json object for js parsing)
    tweets = [r.text for r in results]

    return tweets

print(SearchTweets(123, 456))