#!/usr/bin/env python3

# Generic shit
import os
import sys
import time
import json
import dataset as ds
import sqlite3 as sql # Dealt with now by dataset module
import pandas as pd
from readsec import read_tokens

#Import the necessary methods from tweepy library
from redis import Redis
from rq import Queue
from rq.decorators import job
from textblob import TextBlob
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import exception
import tweepy.error

# Import routines for the workers tor un
from tweepymod import StdOutListener

#from tweepymod import classify_tweet
HOME = "/home/rpdaly"
accf = HOME + "/.twitter_oauth"
conf = HOME + "/.twitter_consumer"

(ACCESS_TOKEN, ACCESS_SECRET) = read_tokens(accf)
(CONSUMER_KEY, CONSUMER_SECRET) = read_tokens(conf)

#This is a basic listener that just prints received tweets to stdout.
if __name__ == '__main__':

    while True:
        try:
            #queue = Queue('high', connection=Redis('127.0.0.1', 6379))
            #dbase = sql.connect('kratom_tweetset.db')
            l = StdOutListener()
            auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            stream = Stream(auth, l)
            stream.filter(track=['Kavanaugh','Trump'])

        except Exception as ex:
            print("Error: Restarting stream")
            print(ex)
            print(ex.__doc__)
            time.sleep(5);

# vim: tw=60:ts=4:sw=4:sts=4:sta
