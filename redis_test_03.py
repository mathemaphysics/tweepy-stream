#!/usr/bin/env python3

import os
import sys
import time
import numpy as np
from termcolor import cprint

from testmod import ret_a_val, write_val
from rq import Queue
from rq.decorators import job
from redis import Redis

con1 = Redis('192.168.2.122', 6380, password='SXY+GnkMVYoJ7hSb3V565')
q1 = Queue('low', connection=con1)
q2 = Queue('high', connection=con1)

for i in range(2):
    j1 = q1.enqueue(ret_a_val)
    j2 = q2.enqueue(ret_a_val)
    while not j1.is_finished or not j2.is_finished:
        time.sleep(0.01)
    print()
    cprint("Result %03d:" % i, 'cyan')
    cprint(j1.result, 'yellow')
    cprint(j2.result, 'green')

# vim: tw=65:ts=4:sw=4:sts=4:et:sta