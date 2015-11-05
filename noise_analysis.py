# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:24:41 2015

@author: lenz
"""
import numpy as np
from pylab import show, ginput, plot
import matplotlib.pyplot as plt

def noise_analysis(x,y,fs,t0): #t0 is the pretrigger!
    fig=plt.figure()
    ax=fig.add_subplot(111)
    
    
    ax.plot(x,y)
    temp=[]
    
    def onclick(event):
        print('I pressed g')
        if event.key == "g":
            xx = ginput(3)    
            temp.append(xx)
    cid = fig.canvas.mpl_connect('key_press_event', onclick)

    show()
#    print("Please click")

    xx = temp[0]
#    print(temp)
#    print("clicked",xx)
    sampling_time=1/fs
    t0_noise=np.int(xx[0][0]/sampling_time)-t0/sampling_time
    tf_noise=np.int(xx[1][0]/sampling_time)-t0/sampling_time
    t_end=np.int(xx[2][0]/sampling_time)-t0/sampling_time
#    print(t0_noise,tf_noise)
    
    y_toend=y[t0_noise:t_end]
    t_max=np.argmax(y_toend) + t0_noise #because we shift everything to the left using t0=pretrigger, this calculates the peak from 0 to the 3rd ginput point
    y_topeak=y[t0_noise:t_max]
    noise_data_window=y[t0_noise:tf_noise]
    sigma=np.std(noise_data_window)
    mean=np.mean(noise_data_window)

    min_ind=np.argmax(np.abs(1.0/((mean+3*sigma)-y_topeak)))
    min_ampl=y_topeak[min_ind]
    max_ampl=np.max(y_topeak)
    y_ampl=max_ampl-min_ampl
#    print(sigma,min_ampl,max_ampl,y_ampl)
   
    ten_percent_ind=np.argmax(np.abs(1.0/((0.1*y_ampl+min_ampl)-y_topeak)))
    twenty_percent_ind=np.argmax(np.abs(1.0/((0.2*y_ampl+min_ampl)-y_topeak)))
    fifty_percent_ind=np.argmax(np.abs(1.0/((0.5*y_ampl+min_ampl)-y_topeak)))
    eighty_percent_ind=np.argmax(np.abs(1.0/((0.8*y_ampl+min_ampl)-y_topeak)))
    ninety_percent_ind=np.argmax(np.abs(1.0/((0.9*y_ampl+min_ampl)-y_topeak)))
    
#    print("min",min_ind)  
#    print("10",ten_percent_ind)  
#    print("90",ninety_percent_ind)
    
#    print("standard deviation= %r noise mean= %r"%(sigma,mean))
    plot(x[t0_noise:t_end],y_toend, 'b', \
    x[t0_noise:tf_noise],y[t0_noise:tf_noise], 'g', \
    [x[t0_noise],x[t_end]],[mean,mean], 'r', \
    [x[t0_noise],x[t_end]],[mean+sigma,mean+sigma], '--r', \
    [x[t0_noise],x[t_end]],[mean-sigma,mean-sigma], '--r', \
    [x[min_ind]+t0_noise*sampling_time,x[ten_percent_ind]+t0_noise*sampling_time,x[ninety_percent_ind]+t0_noise*sampling_time],[y_topeak[min_ind],y_topeak[ten_percent_ind],y_topeak[ninety_percent_ind]], 'or')
    show()
    
    ten_percent_time=(ten_percent_ind+t0_noise)*sampling_time
    twenty_percent_time=(twenty_percent_ind+t0_noise)*sampling_time
    fifty_percent_time=(fifty_percent_ind+t0_noise)*sampling_time
    eighty_percent_time=(eighty_percent_ind+t0_noise)*sampling_time
    ninety_percent_time=(ninety_percent_ind+t0_noise)*sampling_time
    risetime_10_90=(ninety_percent_time-ten_percent_time)
    
#    print("10%% time",ten_percent_time)
#    print("90%% time",twenty_percent_time)
    return ten_percent_time,twenty_percent_time,fifty_percent_time,eighty_percent_time,ninety_percent_time,risetime_10_90,x[t0_noise:t_end],(y_toend-mean)