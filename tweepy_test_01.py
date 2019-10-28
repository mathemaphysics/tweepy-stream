#!/usr/bin/env python3

# Generics
import os
import sys
sys.path.append('./temp')
import time
import pandas as pd
from readsec import read_tokens

#Import the necessary methods from tweepy library
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import exception
import tweepy.error

# This is ridiculous
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

#from tweepymod import classify_tweet
HOME = "/home/rpdaly"
accf = HOME + "/.twitter-access-api"
conf = HOME + "/.twitter-consumer-api"

(ACCESS_TOKEN, ACCESS_SECRET) = read_tokens(accf)
(CONSUMER_KEY, CONSUMER_SECRET) = read_tokens(conf)
print(ACCESS_TOKEN, ACCESS_SECRET)
print(CONSUMER_KEY, CONSUMER_SECRET)

#This is a basic listener that just prints received tweets to stdout.
if __name__ == '__main__':

    while True:
        try:
            l = MyStreamListener()
            auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            stream = Stream(auth, l)
            stream.filter(track=['Trump'])

        except Exception as ex:
            print("Error: Restarting stream")
            print(ex)
            print(ex.__doc__)
            time.sleep(5);

# vim: tw=60:ts=4:sw=4:sts=4:sta
