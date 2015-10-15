# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:24:41 2015

@author: lenz
"""
import numpy as np
from pylab import show, ginput, plot
import matplotlib.pyplot as plt

def noise_analysis(x,y,fs,t0): #t0 is the pretrigger!
    
    plot(x,y)
    print("Please click")
    xx = ginput(3)
    print("clicked",xx)
    sampling_time=1/fs
    t0_noise=np.int(xx[0][0]/sampling_time)-t0/sampling_time
    tf_noise=np.int(xx[1][0]/sampling_time)-t0/sampling_time
    t_end=np.int(xx[2][0]/sampling_time)-t0/sampling_time
    print(t0_noise,tf_noise)
    show() 
    
    t_max=np.argmax(y[0:t_end]) #because we shift everything to the left using t0=pretrigger, this calculates the peak from 0 to the 3rd ginput point
    y_topeak=y[0:t_max]
    noise_data_window=y[t0_noise:tf_noise]
    sigma=np.std(noise_data_window)
    mean=np.mean(noise_data_window)

    min_ind=np.argmax(np.abs(1.0/((mean+3*sigma)-y_topeak)))   
    min_ampl=y_topeak[min_ind]
    max_ampl=np.max(y_topeak)
    y_ampl=max_ampl-min_ampl
    print(sigma,min_ampl,max_ampl,y_ampl)
   
    ten_percent_ind=np.argmax(np.abs(1.0/((0.1*y_ampl+min_ampl)-y_topeak)))  
    twenty_percent_ind=np.argmax(np.abs(1.0/((0.2*y_ampl+min_ampl)-y_topeak))) 
    fifty_percent_ind=np.argmax(np.abs(1.0/((0.5*y_ampl+min_ampl)-y_topeak))) 
    eighty_percent_ind=np.argmax(np.abs(1.0/((0.8*y_ampl+min_ampl)-y_topeak))) 
    ninety_percent_ind=np.argmax(np.abs(1.0/((0.9*y_ampl+min_ampl)-y_topeak))) 
    risetime_10_90=(ninety_percent_ind-ten_percent_ind)/fs
    
    print("10",ten_percent_ind)    
    
    print("standard deviation= %r noise mean= %r"%(sigma,mean))
    plot(x,y, 'b', \
    x[t0_noise:tf_noise],y[t0_noise:tf_noise], 'g', \
    [x[0],x[-1]],[mean,mean], 'r', \
    [x[0],x[-1]],[mean+sigma,mean+sigma], '--r', \
    [x[0],x[-1]],[mean-sigma,mean-sigma], '--r', \
    [x[min_ind],x[ten_percent_ind],x[ninety_percent_ind]],[y[min_ind],y[ten_percent_ind],y[ninety_percent_ind]], 'or')
    show()
    
    return ten_percent_ind,twenty_percent_ind,fifty_percent_ind,eighty_percent_ind,ninety_percent_ind,risetime_10_90