#!/usr/bin/env python3

import os
import sys
import time
from rq import Worker
from redis import Redis

# Create the Connection to a redis dictionary
c = Redis('127.0.0.1', 6379)

# Create the Worker class on the required queues
w = Worker(queues=('low', 'high'), connection=c)
w.work()

# vim: tw=65:sw=4:ts=4:sts=4:et:sta
