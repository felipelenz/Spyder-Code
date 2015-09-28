#!/usr/bin/env python

# Add personal packages directory to path
import sys
sys.path.append('/home/jaime/Documents/Python Code')

# Import other packages
import numpy as np

def fix_time(time, num_ticks):
    """
    This functions gives back the time to get whole units in the plots.
    The acceptable units to use are seconds, milliseconds, microseconds, or
    nanoseconds.
    """

    delta_t = np.diff(time)[0]
    tick_spacing = delta_t / num_ticks
    multiplier = 1.0

    n = 0

    print(n , multiplier,  tick_spacing)

    while tick_spacing < 1:
        n += 1
        m = 10
        tick_spacing *= m
        multiplier *= m
        print(n , multiplier,  tick_spacing)

    if (multiplier == 1E0):
        string = 'seconds'

    elif (multiplier <= 1E3):
        multiplier = 1E3
        string = 'milliseconds'

    elif (multiplier <= 1E6):
        multiplier = 1E6
        string = '$\mu$seconds'

    elif (multiplier <= 1E9):
        multiplier = 1E9
        string = 'nanoseconds'

    elif (multiplier <= 1E12):
        multiplier = 1E12
        string = 'femtoseconds'

    else:
        string = 'tiny!'

    return multiplier, string