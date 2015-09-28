#!/usr/bin/env python

# Add personal packages directory to path
import sys
#sys.path.append('/Volumes/2015 Data/Sky Waves/070615/Good Skywaves')

# Import other packages
import numpy as np
#import scipy.interpolate as ip
import matplotlib.pyplot as plt
#from matplotlib.ticker import LinearLocator
import lecroy as lc
#import timing
#import dfplots as df
#import JaimePackages.oscilloscopes.lecroy as lc
#import JaimePackages.timing.timing as timing

file_name = "/Volumes/Promise 12TB RAID5/2015 Data/071915/Scope43/C1AC00000.trc"
#~ x,y = lc.read_timetrace(file_name)
lecroy = lc.lecroy_data(file_name)

seg_time = lecroy.get_seg_time()

segments = lecroy.get_segments()

#n_ticks = 1.0
#
#mult, string = timing.fix_time(seg_time, n_ticks)
#~     mult = 1
#~     string = ''
mult=1e6

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(seg_time[::100]*mult, segments[0][::100])

ax.set_title('Segment 1')

ax.set_xlabel('Time ($\mu$s)')
ax.set_xlim([seg_time[0]*mult, seg_time[-1]*mult])
#ax.xaxis.set_major_locator(LinearLocator(numticks=n_ticks))
#  ax.xaxis.set_ticks()
#~ ax.locator_params(axis='x', nbins=200)
#~ ax.locator_params(axis='y', nbins=10)
#~ ax.locator_params(tight=True)


#~ i = 1
#~ plt.figure()
#~
#~ for segment in segments:
#~     plt.subplot(len(segments),1,i)
#~     plt.plot(seg_time*1E3,segment)
#~     plt.title("%s Segment %d" % (lecroy.get_timestamp().strftime('%Y-%m-%d %H:%M:%S.%f'),i))
#~     i += 1

#plt.show()
#cal=58.56
#p = df.RelativeTimePlot(seg_time[::20],segments[0][::20]*cal)
#p.plot()
#plt.show()
#
#MaxAmpl=np.max(segments[0])
#MaxInd=np.argmax(segments[0])
#MinAmpl=np.min(segments[0])
#dt=50e-9
#s1=(MaxInd)-100e-6/dt;
#s2=s1+1e-3/dt;
#print(MaxAmpl,MaxInd)
#
#time=seg_time*mult-MaxInd*dt+250e-3;
#plt.plot(time[s1:s2],segments[0][s1:s2])
#plt.show()

#y=segments[0][::20]*cal
#weight=np.repeat(1.0,5)/5.0
#smooth=np.convolve(y,weight,"same")
#    
#
#interp_data=ip.interp1d(seg_time[::20],y)
#
#p = df.RelativeTimePlot(seg_time[::20],smooth,1e9)
#p.plot()
#plt.show()
#
#fig, ax=p.relative_plot(1e6)
#
#ax.set_title('Date: 07-08-2015, UTC Time: 16:15:20.6 \n Negative CG Flash (8 kA peak) over sand 324 km West of ICLRT')
#ax.set_xlabel(r'Time ($\mu$s)')
#ax.set_ylabel('Electric Field Amplitude (V/m)')
#plt.grid()

plt.show()

