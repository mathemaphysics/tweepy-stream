#!/usr/bin/env python3
import os
import sys
import time
from termcolor import cprint

from rq import Queue, Connection
from redis import Redis
from testmod import val_org, val_job

# Set up connection to redis server
con1 = Redis('127.0.0.1', 6379)
q1 = Queue('low', connection=con1)
q2 = Queue('high', connection=con1)

# Run the first method
cprint('Round 1: Calling val_org (no decorator)', 'red')

# Submit 1 in queue 'low'
j1 = q1.enqueue(val_org)
while not j1.is_finished:
    time.sleep(0.01)

cprint('Result:', color='green', end=' ', attrs=['bold'])
cprint('val = %5d' % j1.result, color='yellow')

# Run the second method
cprint('Round 2: Calling val_job.delay() (via decorator)', 'red')

# Submit 2 in queue 'low'; will run in 'low'
# queue because this is specified via the @job
# decorator in the testmod module in
# ~/.local/lib/python
j2 = val_job.delay()
while not j2.is_finished:
    time.sleep(0.01)

cprint('Result:', color='blue', end=' ', attrs=['bold'])
cprint('val = %5d' % j2.result, color='magenta')

# Run the third method
cprint('Round 3: Calling val_job() (direct call to val_job)', 'red')

# Submit 3 in queue 'high'
j3 = q2.enqueue(val_org)
while not j3.is_finished:
    time.sleep(0.01)

cprint('Result:', color='cyan', end=' ', attrs=['bold'])
cprint('val = %5d' % j3.result, color='white')
# vim: tw=65:ts=4:sw=4:sts=4:et:sta
