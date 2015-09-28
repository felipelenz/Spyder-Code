#!/usr/bin/env python

# Add personal packages directory to path
import sys
sys.path.append('/home/jaime/Documents/Python Code')

# Import other modules
import numpy as np
import matplotlib.pyplot as plt
import math

import JaimePackages.oscilloscopes.yoko850 as yk
import JaimePackages.plotting.dfplots as df


fileName = ["/home/jaime/Documents/My Papers/Ongoing/Current Reflections"
            "/Raw Data/GOLF/UF14-42_GC/UF1442_GOLF_E"]

traces = {'LOG_E':1}#'II_HI':1, 'II_LO':1, 'II_VL':1}	# Specifies which traces you want to look at
traceUnits = {'LOG_E':'V/m'}#'II_HI':'kA', 'II_LO':'kA', 'II_VL':'A'} # Specifies the units for 
                                                      # each trace for plotting
traceUnitsFactors = {'LOG_E':1}#'II_HI':1E-3, 'II_LO':1E-3, 'II_VL':1}	# Specifies the
                                                            # unit conversion 
                                                            # factor for
                                                            # plotting

calFactors = {'LOG_E':1}#'II_HI':19723.87, 'II_LO':1962.71 , 'II_VL':78.59} # Specifies 
                                                                 # the
                                                                 # calibration 
                                                                 # factor for 
                                                                 # each trace
t_start = 0                                                            
df32_tStart = {'LOG_E':t_start}#'II_HI':t_start, 'II_LO':t_start, 'II_VL':t_start} # Gives the starting time of 
                                                # interest for each trace

t_end = 5 
df32_tStop = {'LOG_E':t_end}#'II_HI':t_end, 'II_LO':t_end, 'II_VL':t_end}	# Gives the ending time of 
                                                # interes for each trace
                                                
wantOffset = 'y'
						
traceKeys = traces.keys()	# Gets the key names for each trace to be used 
							# as an index for the other dictionaries

f = {}
header = {}

try:
    for i, key in enumerate(traceKeys):
        print("Obtaining header: '%s'" % key)
        f[key] = yk.Yoko850File(fileName[i])
        header[key] = f[key].get_header()
except IOError as e:
    print(str(e))
    raise

results = {}
for i,key in enumerate(traceKeys):
	print("Obtaining trace: '%s'" % key)
	results[key] = f[key].get_trace_data(header[key], traces[key], \
	                                     df32_tStart[key], \
									     df32_tStop[key], calFactors[key], \
									     wantOffset)
									
for i,key in enumerate(traceKeys):
	print("%s ID: %s" % (key,results[key].traceLabel))

#~ print results['II_HI'].dataTime.shape[0]
#~ print results['II_HI'].data.shape[0]

ds_factor = len(results['LOG_E'].data)/1E5

from scipy.signal import savgol_filter
E_filtered = savgol_filter(results['LOG_E'].data[::ds_factor], 9, 5)
tt = results['LOG_E'].dataTime[::ds_factor]

print("Plotting results...")
#~ ds_factor = 20

plt.figure()
plt.plot(E_filtered)

#~ plt.subplot(311)
#~ plt.plot(results['II_HI'].dataTime[::ds_factor], \
         #~ results['II_HI'].data[::ds_factor]*traceUnitsFactors['II_HI'])
#~ plt.grid()
#~ plt.title('UF 14-08')
#~ plt.ylabel('II_HI (%s)' % traceUnits['II_HI'])
#~ 
#~ 
#~ plt.subplot(312)
#~ plt.plot(results['II_LO'].dataTime[::ds_factor], \
         #~ results['II_LO'].data[::ds_factor]*traceUnitsFactors['II_LO'])
#~ plt.grid()
#~ plt.ylabel('II_LO (%s)' % traceUnits['II_LO'])
#~ 
#~ plt.subplot(313)
#~ plt.plot(results['II_VL'].dataTime[::ds_factor], \
         #~ results['II_VL'].data[::ds_factor]*traceUnitsFactors['II_VL'])
#~ plt.grid()
#~ plt.ylabel('II_VL (%s)' % traceUnits['II_VL'])

plt.xlabel('Time (seconds)')
	
plt.show()

