# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:59:55 2015

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

MaxAmpl=np.max(segments[0])
MaxInd=np.argmax(segments[0])
MinAmpl=np.min(segments[0])
dt=50e-9
s1=(MaxInd)-100e-6/dt;
s2=s1+1e-3/dt;
print(MaxAmpl,MaxInd)

mult=1e6
cal=58.56
time=seg_time*mult-MaxInd*dt-250e-3;


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(time[s1:s2:100]*mult, segments[0][s1:s2:100]*cal)
plt.show()
