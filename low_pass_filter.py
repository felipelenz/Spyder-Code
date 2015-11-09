# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:47:23 2015

@author: lenz
"""
#import Yoko750 as yk
#import lecroy as lc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import signal
#import scipy import signal
matplotlib.rcParams.update({'font.size': 20})

#date=82015
#seg=4
#RS_number=5
#M_comp_number=1
#t0=0.251506
#event=35
#suffix41=3 #yoko Last digit of the .wvf file name
#suffix43=3 #lecroy last digit og the .trc file name
#duplicate_delay=0#6.37252e-6
#
#dt1=1
#dt2=1
##Yoko
#yoko_fileName = "/Volumes/2015 Data/0"+str(date)+"/Scope41/APD000"+str(suffix41)
#
#f = yk.Yoko750File(yoko_fileName)
#header = f.get_header()
#
##Diode 2
#lecroy_fileName_Scope43_APD2 = "/Volumes/2015 Data/0"+str(date)+"/Scope43/C2AC0000"+str(suffix43)+".trc"
#lecroy_Scope43_APD2 = lc.lecroy_data(lecroy_fileName_Scope43_APD2)
#seg_time_Scope43_APD2 = lecroy_Scope43_APD2.get_seg_time()
#segments_Scope43_APD2 = lecroy_Scope43_APD2.get_segments()
#
#tf=t0+10e-3
#APD_32=f.get_trace_data(header,12,t0,tf)
#
#yoko_pretrigger=t0+0.005-duplicate_delay
#
#x=APD_32.data
#t=APD_32.dataTime-yoko_pretrigger
#fs=100e6

def LPF(t,x,fs):
#    X=np.fft.fft(x)
#    n=len(x)
#    frequency_axis=np.arange(0,n-1,1)*fs/n
#    fft_magnitude=20*np.log10(np.abs(X[0:-1]))
#    plt.plot(frequency_axis,fft_magnitude)
#    plt.show()
    
    New_fs=400e3
    
    
    def butter_lowpass(cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
        return b, a
    
    def butter_lowpass_filter(data, cutoff, fs, order=5):
        b, a = butter_lowpass(cutoff, fs, order=order)
        y = signal.lfilter(b, a, data)
        return y
    
    fs=100e6
    order=5
    cutoff=New_fs
    
    b, a = butter_lowpass(cutoff, fs, order)
    
    y = butter_lowpass_filter(x, cutoff, fs, order)
    plt.figure(figsize=(11,8.5))    
    plt.plot(t,x)
    plt.plot(t,y)
    
    plt.show()
    return y