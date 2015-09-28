#!/usr/bin/python
"""
#How to run in iPython:
#
#execfile('/Volumes/OSX2/Users/jaime/Data/ICLRT/Code/Scopes/Yokogawa/yoko750_example.py')

"""
import Yoko750 as yk
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import nanmean



def downsample(array, R):
    pad_size = math.ceil(float(len(array))/R)*R - len(array)
    A_pad = np.append(array, np.zeros(pad_size)*np.NaN)
    return nanmean(A_pad.reshape(-1,R), axis=1)

fileName = "/Volumes/Promise 12TB RAID5/2015 Data/071915/Scope41/APD0002"

f = yk.Yoko750File(fileName)
header = f.get_header()

t0=0.098
tf=0.11
APD_21=f.get_trace_data(header,1,t0,tf)
APD_22=f.get_trace_data(header,2,t0,tf)
APD_23=f.get_trace_data(header,3,t0,tf)
APD_24=f.get_trace_data(header,4,t0,tf)
APD_25=f.get_trace_data(header,5,t0,tf)
APD_26=f.get_trace_data(header,6,t0,tf)
APD_27=f.get_trace_data(header,7,t0,tf)
APD_28=f.get_trace_data(header,8,t0,tf)
APD_29=f.get_trace_data(header,9,t0,tf)
APD_30=f.get_trace_data(header,10,t0,tf)
APD_31=f.get_trace_data(header,11,t0,tf)
APD_32=f.get_trace_data(header,12,t0,tf)

plt.plot(APD_32.dataTime[::20]*1e3,APD_32.data[::20]+0.6,color=[0.8,0.8,0.3])
plt.plot(APD_31.dataTime[::20]*1e3,APD_31.data[::20]+0.55,color=[0.2414,0,0.1034])
plt.plot(APD_30.dataTime[::20]*1e3,APD_30.data[::20]+0.5,color=[0.7241,0.3103,0.8276])
plt.plot(APD_29.dataTime[::20]*1e3,APD_29.data[::20]+0.45,color=[0.8276,1,0])
plt.plot(APD_28.dataTime[::20]*1e3,APD_28.data[::20]+0.4,color=[0.6207,0,0])
plt.plot(APD_27.dataTime[::20]*1e3,APD_27.data[::20]+0.35,color=[0.4483,0.3793,0.4828])
plt.plot(APD_26.dataTime[::20]*1e3,APD_26.data[::20]+0.3,color=[0.6207,0.7586,1])
plt.plot(APD_25.dataTime[::20]*1e3,APD_25.data[::20]+0.25,color=[0.4483,0.9655,1])
plt.plot(APD_24.dataTime[::20]*1e3,APD_24.data[::20]+0.2,color=[0.5172,0.4483,0])
plt.plot(APD_23.dataTime[::20]*1e3,APD_23.data[::20]+0.15,color=[0.9655,0.5173,0.0345])
plt.plot(APD_22.dataTime[::20]*1e3,APD_22.data[::20]+0.1,color=[0.5517,0.6552,0.4828])
plt.plot(APD_21.dataTime[::20]*1e3,APD_21.data[::20]+0.05,color=[0.5,1,0.5])
plt.xlabel('Time (ms)')
plt.ylabel('Luminosity (digitizer volts)')
plt.legend(['D32* NF (1 km)','D31# NF (1 km)','D30* F (900 m)', \
            'D29# F (900 m)','D28# NF (800 m)','D27* F (700 m)', \
            'D26# F (700 m)','D25# NF (600 m)','D24* F (500 m)', \
            'D23# F (500 m)','D22* NF (400 m)','D21# NF (400 m)'])
plt.title('UF 15-04: Altitude Trigger')
plt.grid()
plt.show()


#wantOffset = 'y'
#
#traces = {'APD21':1}	# Specifies which traces you want to look at
#traceUnits = {'APD21':'digitizer volts'} # Specifies the units for each trace for plotting
#traceUnitsFactors = {'APD21':1}	# Specifies the unit conversion factor
#									# for plotting
#
#calFactors = {'APD21':1} # Specifies the calibration factor for each
#								# trace
#df32_tStart = {'APD21':0} # Gives the starting time of interest for
#									# each trace
#df32_tStop = {'APD21':0.5}	# Gives the ending time of interes for
#								# each trace
#
#traceKeys = traces.keys()	# Gets the key names for each trace to be used
#							# as an index for the other dictionaries
#
#results = {}
#for key in traceKeys:
#    print("Obtaining trace: '%s'" % key)
#
#    results[key] = f.get_trace_data(header, traces[key], df32_tStart[key], df32_tStop[key], calFactors[key], wantOffset)
#
#for key in traceKeys:
#	print("%s ID: %s" % (key,results[key].traceLabel))
#
##~ print results['II_HI'].dataTime.shape[0]
##~ print results['II_HI'].data.shape[0]
#
#print("Plotting results...")
#for key in traceKeys:
#    plt.figure()
#    plt.plot(results[key].dataTime*1E6, \
#    		 results[key].data*traceUnitsFactors[key])
#    plt.title(key)
#    plt.xlabel('Time ($\mu$seconds)')
#    plt.ylabel('Current (%s)' % traceUnits[key])
#
#    A=downsample(results[key].dataTime,20)
#    B=downsample(results[key].data,20)
#
#    print(len(results[key].dataTime), len(A))
#    print(len(results[key].data), len(B))
#
#    plt.plot(A*1E6, \
#    		 B*traceUnitsFactors[key])
#
#    plt.show()


