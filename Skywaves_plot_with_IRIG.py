# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:48:47 2015

@author: lenz
"""

import lecroy as lc
import numpy as np
import matplotlib.pyplot as plt
import IRIGA
from pylab import ginput, plot

fs=10e6 #sampling rate
event=41 #event name
RS_number=1 #return stroke number
RS_time=57.298446790 #seconds of the XLI time stamp (for trigger lightning) 
                    #this time can be found in the triggered lightning reports

#import IRIG file
lecroy_fileName_DBY_IRIG = "/Volumes/Promise 12TB RAID5/2015 Data/082715/DBY Data/C2DBY00011.trc"
lecroy_DBY_IRIG= lc.lecroy_data(lecroy_fileName_DBY_IRIG)
seg_time_DBY_IRIG = lecroy_DBY_IRIG.get_seg_time()
segments_DBY_IRIG = lecroy_DBY_IRIG.get_segments()

#read IRIG file and print time stamp
timestamp,t =IRIGA.IRIGA_signal(segments_DBY_IRIG[0], fs, year=2015)
print(timestamp)

#import skywaves data
lecroy_fileName_DBY = "/Volumes/Promise 12TB RAID5/2015 Data/082715/DBY Data/C1DBY00011.trc"
lecroy_DBY= lc.lecroy_data(lecroy_fileName_DBY)
seg_time_DBY = lecroy_DBY.get_seg_time()
segments_DBY = lecroy_DBY.get_segments()

t0=RS_time-(timestamp.second+timestamp.microsecond/1e6)+200e3/2.99e8
t0=round(t0*1e9)/1e9
tf=t0+0.5
n0=int((t0-0.5)*fs)
nf=int(tf*fs)
#plt.plot([0,0],[-1,1],t[n0:nf]-t0,segments_DBY[0][n0:nf])
#plt.xlabel('UTC Time in seconds after '+str(timestamp.hour)+':'+str(timestamp.minute)+':'+str(round((timestamp.second+timestamp.microsecond/1e6+t0)*1e9)/1e9))
#plt.xlim(0,0.00035)
#plt.title("UF 15-"+str(event)+ " return stroke #"+str(RS_number) )
#plt.grid()
#plt.show()

skywave=segments_DBY[0][n0:nf];
time=t[n0:nf]-t0;

#chop lists
time=time[int(0.5*fs):int((0.00035+0.5)*fs)]
skywave=skywave[int(0.5*fs):int((0.00035+0.5)*fs)]
plt.plot(time,skywave)
plt.xlim(0,0.00035)
plt.show()

#plot([0,0],[-1,1],t[n0:nf]-t0,segments_DBY[0][n0:nf])
#xx = ginput(2)
#print("clicked",xx)
#skywave=segments_DBY[0][int((xx[0][0]+t0)*fs):int((xx[1][0]+t0)*fs)]
#time=t[int((xx[0][0]+t0)*fs):int((xx[1][0]+t0)*fs)]
#
#freq_axis=np.arrange([0,len(skywave)-1])
#SKYWAVE_FFT=np.fft.fft(skywave)
#plt.plot( freq_axis,20*np.log10(SKYWAVE_FFT) ) #[0:len(skywave)-1]*(fs/len(skywave))
#plt.show()

    