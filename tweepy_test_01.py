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
import tweepymod as tm
#from tweepymod import classify_tweet

HOME = "/home/rpdaly"
accf = HOME + "/.twitter_oauth"
conf = HOME + "/.twitter_consumer"

(ACCESS_TOKEN, ACCESS_SECRET) = read_tokens(accf)
(CONSUMER_KEY, CONSUMER_SECRET) = read_tokens(conf)

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_connect(self):
        print("Initializing database")
        self.db = ds.connect("sqlite:///kratom_tweetset.db")
        self.tbl = self.db["tweets"]
        self.conn = Redis('127.0.0.1', 6379)
        self.queue = Queue('high', connection=self.conn)
        return True

    def on_status(self, status):
        print("Saved %s" % status.user.name)
        self.queue.enqueue_call(func=tm.classify_tweet, args=(status, self))
        return True

    def on_error(self, status):
        print(status)
        time.sleep(5)
        return True

if __name__ == '__main__':

    while True:
        try:
            l = StdOutListener()
            auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            stream = Stream(auth, l)
            stream.filter(track=['Kavanaugh','Trump'],
                          stall_warnings=False)
        except Exception as ex:
            print("Error: Restarting stream")
            print(ex)
            print(ex.__doc__)
            time.sleep(5);

# vim: tw=60:ts=4:sw=4:sts=4:sta
