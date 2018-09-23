""" 
    Utils
"""

from time import time

def execute(f, text, measure_time = True):
    if (measure_time): t0 = time()
    ret = f()
    if (measure_time): print("%s: %d" % (text, round(time() - t0, 3)))
    return ret
