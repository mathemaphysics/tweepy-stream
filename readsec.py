import os
import sys
import numpy as np

def read_tokens(filename):
    fp = open(filename, "r")
    if fp.readable():
        keys = [ln.strip() for ln in fp.readlines()]
        return (keys[0], keys[1])
    else:
        return ('', '')

# vim: tw=60:ts=4:sts=4:sw=4:sta
