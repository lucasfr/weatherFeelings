# -*- coding: utf-8 -*-

import tweepy

def tweet( mTweet ):
      CONSUMER_KEY = XXX
      CONSUMER_SECRET = XXX
      ACCESS_KEY = XXX
      ACCESS_SECRET = XXX
      
      auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
      auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
      api = tweepy.API(auth)
      img = 'haha.gif'
      api.update_with_media(img,status = mTweet)
      
      return