# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:14:16 2015

@author: lenz
"""

import numpy as np
import scipy.interpolate as ip
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import lecroy as lc
import timing
import dfplots as df

file_name = "/Volumes/2015 Data/Sky Waves/070815/Good Skywaves/C1AC00051.trc"
lecroy = lc.lecroy_data(file_name)

seg_time = lecroy.get_seg_time()

segments = lecroy.get_segments()
mult=1e6

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(seg_time[::100]*mult, segments[0][::100])

ax.set_title('Segment 1')

ax.set_xlabel('Time ($\mu$s)')
ax.set_xlim([seg_time[0]*mult, seg_time[-1]*mult])

plt.show()