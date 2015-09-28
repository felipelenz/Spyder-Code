# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:08:22 2015

@author: lenz
"""

import numpy as np
from pylab import show, ginput, plot

def noise_analysis(x,y,fs,t0):
    
    plot(x,y)
    print("Please click")
    xx = ginput(3)
    print("clicked",xx)
    sampling_time=1/fs
    t0_noise2=np.int(xx[0][0]/sampling_time)-t0/sampling_time
    tf_noise2=np.int(xx[1][0]/sampling_time)-t0/sampling_time
    print(t0_noise2,tf_noise2)
    show()

    noise_data_window=y[t0_noise2:tf_noise2]
    sigma=np.std(noise_data_window)
    mean=np.mean(noise_data_window)
    print("standard deviation= %d noise mean= %d"%(sigma,mean))
    plot(x,y, 'b', \
    x[t0_noise2:tf_noise2],y[t0_noise2:tf_noise2], 'g', \
    [x[0],y[-1]],[mean,mean], 'r', \
    [x[0],y[-1]],[mean+sigma,mean+sigma], '--r', \
    [x[0],y[-1]],[mean-sigma,mean-sigma], '--r')
    show()