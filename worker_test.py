#!/usr/bin/env python3

import os
import sys
import time
from rq import Worker, Queue
from redis import Redis
#from tweepymod import StdOutListener

# Create the Connection to a redis dictionary
if __name__ == '__main__':
    c = Redis('127.0.0.1', 6379, password='SXY+GnkMVYoJ7hSb3V565')

    # Create the Worker class on the required queues
    w = Worker(queues=('low', 'high'), connection=c)
    w.work()
    #w.work(logging_level='ERROR')

# vim: tw=65:sw=4:ts=4:sts=4:et:sta
