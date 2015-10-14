#!/usr/bin/python

import Yoko750 as yk
import lecroy as lc
import numpy as np
import matplotlib.pyplot as plt
from noise_analysis import noise_analysis
from pylab import show, ginput, plot

#import math
#from scipy.stats import nanmean

date=82715
seg=0
RS_number=1
t0=0
event=43
suffix26=0
suffix41=5 #yoko Last digit of the .wvf file name
suffix42=5 #lecroy last digit og the .trc file name
suffix43=5 #lecroy last digit og the .trc file name
suffix44=5 #lecroy last digit og the .trc file name
suffix48=5 #lecroy last digit og the .trc file name
suffix50=5 #lecroy last digit og the .trc file name
offset=0.05
duplicate_delay=0

dt1=1
dt2=1

#Current
##Yoko
#yoko_current_fileName = "/Volumes/2015 Data/0"+str(date)+"/Scope24/UF15"+str(event)+"_IIHI"
#    
#c = yk.Yoko750File(yoko_current_fileName)
#header = c.get_header()  
lecroy_fileName_IIHI = "/Volumes/2015 Data/0"+str(date)+"/Scope26/C1AC0000"+str(suffix26)+".trc"
lecroy_IIHI = lc.lecroy_data(lecroy_fileName_IIHI)
seg_time_IIHI = lecroy_IIHI.get_seg_time()
segments_IIHI = lecroy_IIHI.get_segments()

#Yoko
yoko_fileName = "/Volumes/2015 Data/0"+str(date)+"/Scope41/APD000"+str(suffix41)

f = yk.Yoko750File(yoko_fileName)
header = f.get_header()

##LeCroy
#Diode 1
lecroy_fileName_Scope43_APD1 = "/Volumes/2015 Data/0"+str(date)+"/Scope43/C1AC0000"+str(suffix43)+".trc"
lecroy_Scope43_APD1 = lc.lecroy_data(lecroy_fileName_Scope43_APD1)
seg_time_Scope43_APD1 = lecroy_Scope43_APD1.get_seg_time()
segments_Scope43_APD1 = lecroy_Scope43_APD1.get_segments()

#Diode 2
lecroy_fileName_Scope43_APD2 = "/Volumes/2015 Data/0"+str(date)+"/Scope43/C2AC0000"+str(suffix43)+".trc"
lecroy_Scope43_APD2 = lc.lecroy_data(lecroy_fileName_Scope43_APD2)
seg_time_Scope43_APD2 = lecroy_Scope43_APD2.get_seg_time()
segments_Scope43_APD2 = lecroy_Scope43_APD2.get_segments()

#Diode 3
lecroy_fileName_Scope43_APD3 = "/Volumes/2015 Data/0"+str(date)+"/Scope43/C3AC0000"+str(suffix48)+".trc"
lecroy_Scope43_APD3 = lc.lecroy_data(lecroy_fileName_Scope43_APD3)
seg_time_Scope43_APD3 = lecroy_Scope43_APD3.get_seg_time()
segments_Scope43_APD3 = lecroy_Scope43_APD3.get_segments()

#Diode 5
lecroy_fileName_Scope43_APD4 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C4AC0000"+str(suffix48)+".trc"
lecroy_Scope43_APD4 = lc.lecroy_data(lecroy_fileName_Scope43_APD4)
seg_time_Scope43_APD4 = lecroy_Scope43_APD4.get_seg_time()
segments_Scope43_APD4 = lecroy_Scope43_APD4.get_segments()

#Diode 5
lecroy_fileName_Scope44_APD5 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C1AC0000"+str(suffix48)+".trc"
lecroy_Scope44_APD5 = lc.lecroy_data(lecroy_fileName_Scope44_APD5)
seg_time_Scope44_APD5 = lecroy_Scope44_APD5.get_seg_time()
segments_Scope44_APD5 = lecroy_Scope44_APD5.get_segments()

#Diode 6
lecroy_fileName_Scope44_APD6 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C2AC0000"+str(suffix48)+".trc"
lecroy_Scope44_APD6 = lc.lecroy_data(lecroy_fileName_Scope44_APD6)
seg_time_Scope44_APD6 = lecroy_Scope44_APD6.get_seg_time()
segments_Scope44_APD6 = lecroy_Scope44_APD6.get_segments()

#Diode 7
lecroy_fileName_Scope44_APD7 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C3AC0000"+str(suffix48)+".trc"
lecroy_Scope44_APD7 = lc.lecroy_data(lecroy_fileName_Scope44_APD7)
seg_time_Scope44_APD7 = lecroy_Scope44_APD7.get_seg_time()
segments_Scope44_APD7 = lecroy_Scope44_APD7.get_segments()

#Diode 8
lecroy_fileName_Scope44_APD8 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C4AC0000"+str(suffix48)+".trc"
lecroy_Scope44_APD8 = lc.lecroy_data(lecroy_fileName_Scope44_APD8)
seg_time_Scope44_APD8 = lecroy_Scope44_APD8.get_seg_time()
segments_Scope44_APD8 = lecroy_Scope44_APD8.get_segments()

#Diode 9
lecroy_fileName_Scope48_APD9 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C1AC0000"+str(suffix48)+".trc"
lecroy_Scope48_APD9 = lc.lecroy_data(lecroy_fileName_Scope48_APD9)
seg_time_Scope48_APD9 = lecroy_Scope48_APD9.get_seg_time()
segments_Scope48_APD9 = lecroy_Scope48_APD9.get_segments()

#Diode 10
lecroy_fileName_Scope48_APD10 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C2AC0000"+str(suffix48)+".trc"
lecroy_Scope48_APD10 = lc.lecroy_data(lecroy_fileName_Scope48_APD10)
seg_time_Scope48_APD10 = lecroy_Scope48_APD10.get_seg_time()
segments_Scope48_APD10 = lecroy_Scope48_APD10.get_segments()

#Diode 11
lecroy_fileName_Scope48_APD11 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C3AC0000"+str(suffix48)+".trc"
lecroy_Scope48_APD11 = lc.lecroy_data(lecroy_fileName_Scope48_APD11)
seg_time_Scope48_APD11 = lecroy_Scope48_APD11.get_seg_time()
segments_Scope48_APD11 = lecroy_Scope48_APD11.get_segments()

#Diode 12
lecroy_fileName_Scope48_APD12 = "/Volumes/2015 Data/0"+str(date)+"/Scope48/C4AC0000"+str(suffix48)+".trc"
lecroy_Scope48_APD12 = lc.lecroy_data(lecroy_fileName_Scope48_APD12)
seg_time_Scope48_APD12 = lecroy_Scope48_APD12.get_seg_time()
segments_Scope48_APD12 = lecroy_Scope48_APD12.get_segments()

#Diode 13
lecroy_fileName_Scope50_APD13 = "/Volumes/2015 Data/0"+str(date)+"/Scope50/C1AC0000"+str(suffix50)+".trc"
lecroy_Scope50_APD13 = lc.lecroy_data(lecroy_fileName_Scope50_APD13)
seg_time_Scope50_APD13 = lecroy_Scope50_APD13.get_seg_time()
segments_Scope50_APD13 = lecroy_Scope50_APD13.get_segments()

#Diode 14
lecroy_fileName_Scope50_APD14 = "/Volumes/2015 Data/0"+str(date)+"/Scope50/C2AC0000"+str(suffix50)+".trc"
lecroy_Scope50_APD14 = lc.lecroy_data(lecroy_fileName_Scope50_APD14)
seg_time_Scope50_APD14 = lecroy_Scope50_APD14.get_seg_time()
segments_Scope50_APD14 = lecroy_Scope50_APD14.get_segments()

#Diode 15
lecroy_fileName_Scope50_APD15 = "/Volumes/2015 Data/0"+str(date)+"/Scope50/C3AC0000"+str(suffix50)+".trc"
lecroy_Scope50_APD15 = lc.lecroy_data(lecroy_fileName_Scope50_APD15)
seg_time_Scope50_APD15 = lecroy_Scope50_APD15.get_seg_time()
segments_Scope50_APD15 = lecroy_Scope50_APD15.get_segments()

#Diode 16
lecroy_fileName_Scope50_APD16 = "/Volumes/2015 Data/0"+str(date)+"/Scope50/C4AC0000"+str(suffix50)+".trc"
lecroy_Scope50_APD16 = lc.lecroy_data(lecroy_fileName_Scope50_APD16)
seg_time_Scope50_APD16 = lecroy_Scope50_APD16.get_seg_time()
segments_Scope50_APD16 = lecroy_Scope50_APD16.get_segments()

#Diode 17
lecroy_fileName_Scope42_APD17 = "/Volumes/2015 Data/0"+str(date)+"/Scope42/C1AC0000"+str(suffix42)+".trc"
lecroy_Scope42_APD17 = lc.lecroy_data(lecroy_fileName_Scope42_APD17)
seg_time_Scope42_APD17 = lecroy_Scope42_APD17.get_seg_time()
segments_Scope42_APD17 = lecroy_Scope42_APD17.get_segments()

#Diode 18
lecroy_fileName_Scope42_APD18 = "/Volumes/2015 Data/0"+str(date)+"/Scope42/C2AC0000"+str(suffix42)+".trc"
lecroy_Scope42_APD18 = lc.lecroy_data(lecroy_fileName_Scope42_APD18)
seg_time_Scope42_APD18 = lecroy_Scope42_APD18.get_seg_time()
segments_Scope42_APD18 = lecroy_Scope42_APD18.get_segments()

#Diode 19
lecroy_fileName_Scope42_APD19 = "/Volumes/2015 Data/0"+str(date)+"/Scope42/C3AC0000"+str(suffix42)+".trc"
lecroy_Scope42_APD19 = lc.lecroy_data(lecroy_fileName_Scope42_APD19)
seg_time_Scope42_APD19 = lecroy_Scope42_APD19.get_seg_time()
segments_Scope42_APD19 = lecroy_Scope42_APD19.get_segments()

#Diode 20
lecroy_fileName_Scope42_APD20 = "/Volumes/2015 Data/0"+str(date)+"/Scope42/C4AC0000"+str(suffix42)+".trc"
lecroy_Scope42_APD20 = lc.lecroy_data(lecroy_fileName_Scope42_APD20)
seg_time_Scope42_APD20 = lecroy_Scope42_APD20.get_seg_time()
segments_Scope42_APD20 = lecroy_Scope42_APD20.get_segments()

#t0=0.154235#0#0.098#100e-3 #Take this number from the time between each lecroy trigger (from df32)
tf=t0+20e-3#t0+20e-3#0.11
lecroy_pretrigger=0.005#0.00399934#5e-3#in seconds
yoko_pretrigger=t0+0.005-duplicate_delay#0.1#t0+(14.535e-3) #in seconds

current_t0=7.99999595e-001
current_tf=current_t0+20e-3
#IIHI=c.get_trace_data(header,1,current_t0,current_tf)

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
APD_20=f.get_trace_data(header,13,t0,tf)

APD_20yo_max=np.max(APD_20.data[::dt1])
APD_20lc_max=np.max(segments_Scope42_APD20[seg][::dt2])
##yoko_lc_delay
#yoko=noise_analysis(APD_20.dataTime[::dt1],APD_20.data[::dt1],10e6,0)
#
#lc=noise_analysis(seg_time_Scope42_APD20[::dt2],segments_Scope42_APD20[seg][::dt2],100e6,0)
#print(yoko[0])
#plt.plot((IIHI.dataTime[::dt1]-yoko_pretrigger)*1e3,IIHI.data[::dt1]-1*offset,color=[0.3,0.3,0.3],linewidth=2)

plt.plot((APD_32.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_32.data[::dt1]/np.max(APD_32.data[::dt1])+32*offset,color=[0.8,0.8,0.3],linewidth=2)
plt.plot((APD_31.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_31.data[::dt1]/np.max(APD_31.data[::dt1])+31*offset,color=[0.2414,0,0.1034],linewidth=2)
plt.plot((APD_30.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_30.data[::dt1]/np.max(APD_30.data[::dt1])+30*offset,color=[0.7241,0.3103,0.8276],linewidth=2)
plt.plot((APD_29.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_29.data[::dt1]/np.max(APD_29.data[::dt1])+29*offset,color=[0.8276,1,0],linewidth=2)
plt.plot((APD_28.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_28.data[::dt1]/np.max(APD_28.data[::dt1])+28*offset,color=[0.6207,0,0],linewidth=2)
plt.plot((APD_27.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_27.data[::dt1]/np.max(APD_27.data[::dt1])+27*offset,color=[0.4483,0.3793,0.4828],linewidth=2)
plt.plot((APD_26.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_26.data[::dt1]/np.max(APD_26.data[::dt1])+26*offset,color=[0.6207,0.7586,1],linewidth=2)
plt.plot((APD_25.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_25.data[::dt1]/np.max(APD_25.data[::dt1])+25*offset,color=[0.4483,0.9655,1],linewidth=2)
plt.plot((APD_24.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_24.data[::dt1]/np.max(APD_24.data[::dt1])+24*offset,color=[0.5172,0.4483,0],linewidth=2)
plt.plot((APD_23.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_23.data[::dt1]/np.max(APD_23.data[::dt1])+23*offset,color=[0.9655,0.5173,0.0345],linewidth=2)
plt.plot((APD_22.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_22.data[::dt1]/np.max(APD_22.data[::dt1])+22*offset,color=[0.5517,0.6552,0.4828],linewidth=2)
plt.plot((APD_21.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_21.data[::dt1]/np.max(APD_21.data[::dt1])+21*offset,color=[0.5,1,0.5],linewidth=2)

plt.plot((seg_time_Scope42_APD20[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD20[seg][::dt2]/np.max(segments_Scope42_APD20[seg][::dt2])+20*offset,color=[0.5172,0.4483,0],linewidth=2)
#plt.plot((lc[0]-lecroy_pretrigger)*1e3,segments_Scope42_APD20[seg][lc[0]]/APD_20lc_max+19*offset,'ro')
#plt.plot((APD_20.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_20.data[::dt1]/APD_20yo_max+19*offset,color=[0.5,1,0.5],linewidth=2)
#plt.plot((yoko[0]-yoko_pretrigger)*1e3,APD_20.data[yoko[0]],'ro')

plt.plot((seg_time_Scope42_APD19[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD19[seg][::dt2]/np.max(segments_Scope42_APD19[seg][::dt2])+19*offset,color=[0.1379,0.1379,0.0345],linewidth=2)
plt.plot((seg_time_Scope42_APD18[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD18[seg][::dt2]/np.max(segments_Scope42_APD18[seg][::dt2])+18*offset,color=[1,0.7586,0.5172],linewidth=2)
plt.plot((seg_time_Scope42_APD17[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD17[seg][::dt2]/np.max(segments_Scope42_APD17[seg][::dt2])+17*offset,color=[0.9655,0.0690,0.3793],linewidth=2)

plt.plot((seg_time_Scope50_APD16[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD16[seg][::dt2]/np.max(segments_Scope50_APD16[seg][::dt2])+16*offset,color=[0.4828,0.1034,0.4138],linewidth=2)
#plt.plot((APD_16.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_16.data[::dt1]+15*offset,color=[0.5172,0.4483,0],linewidth=2)
plt.plot((seg_time_Scope50_APD15[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD15[seg][::dt2]/np.max(segments_Scope50_APD15[seg][::dt2])+15*offset,color=[0.8276,0.0690,1],linewidth=2)
plt.plot((seg_time_Scope50_APD14[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD14[seg][::dt2]/np.max(segments_Scope50_APD14[seg][::dt2])+14*offset,color=[0.9655,0.6207,0.8621],linewidth=2)
plt.plot((seg_time_Scope50_APD13[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD13[seg][::dt2]/np.max(segments_Scope50_APD13[seg][::dt2])+13*offset,color=[0.5862,0.8276,0.3103],linewidth=2)

plt.plot((seg_time_Scope48_APD12[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD12[seg][::dt2]/np.max(segments_Scope48_APD12[seg][::dt2])+12*offset,color=[0,0,0.4828],linewidth=2)
plt.plot((seg_time_Scope48_APD11[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD11[seg][::dt2]/np.max(segments_Scope48_APD11[seg][::dt2])+11*offset,color=[0,0.5172,0.5862],linewidth=2)
plt.plot((seg_time_Scope48_APD10[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD10[seg][::dt2]/np.max(segments_Scope48_APD10[seg][::dt2])+10*offset,color=[0,1,0.7586],linewidth=2)
plt.plot((seg_time_Scope48_APD9[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD9[seg][::dt2]/np.max(segments_Scope48_APD9[seg][::dt2])+9*offset,color=[0.6207,0.3103,0.2759],linewidth=2)

plt.plot((seg_time_Scope44_APD8[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD8[seg][::dt2]/np.max(segments_Scope44_APD8[seg][::dt2])+8*offset,color=[0.5172,0.5172,1],linewidth=2)
plt.plot((seg_time_Scope44_APD7[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD7[seg][::dt2]/np.max(segments_Scope44_APD7[seg][::dt2])+7*offset,color=[0,0.3448,0],linewidth=2)
plt.plot((seg_time_Scope44_APD6[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD6[seg][::dt2]/np.max(segments_Scope44_APD6[seg][::dt2])+6*offset,color=[ 1,0.8276,0],linewidth=2)
plt.plot((seg_time_Scope44_APD5[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD5[seg][::dt2]/np.max(segments_Scope44_APD5[seg][::dt2])+5*offset,color=[1,0.1034,0.7241],linewidth=2)

plt.plot((seg_time_Scope43_APD4[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD4[seg][::dt2]/np.max(segments_Scope43_APD4[seg][::dt2])+4*offset,color=[0, 0, 0.1724],linewidth=2)
plt.plot((seg_time_Scope43_APD3[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD3[seg][::dt2]/np.max(segments_Scope43_APD3[seg][::dt2])+3*offset,color=[0, 1, 0],linewidth=2)
plt.plot((seg_time_Scope43_APD2[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD2[seg][::dt2]/np.max(segments_Scope43_APD2[seg][::dt2])+2*offset,color=[1, 0, 0],linewidth=2)
plt.plot((seg_time_Scope43_APD1[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD1[seg][::dt2]/np.max(segments_Scope43_APD1[seg][::dt2])+1*offset,color=[0, 0, 1],linewidth=2)

plt.plot((seg_time_IIHI[::dt2]-lecroy_pretrigger/2)*1e3, segments_IIHI[seg][::dt2]/np.max(segments_IIHI[seg][::dt2])+0*offset,color=[0.3, 0, 1],linewidth=2)

plt.xlabel('Time (ms)')
plt.ylabel('Luminosity (digitizer volts)')

plt.legend(['D32* NF (1 km)','D31# NF (1 km)','D30* F (900 m)', \
            'D29# F (900 m)','D28# NF (800 m)','D27* F (700 m)', \
            'D26# F (700 m)','D25# NF (600 m)','D24* F (500 m)', \
            'D23# F (500 m)','D22* NF (400 m)','D21# NF (400 m)', \
            'D20* F (300 m)','D19# F (300 m)','D18* F (200 m)', \
            'D17# F (200 m)', \
            'D16# F (154 m)','D15* F (94 m)', \
            'D14# F (94 m)','13# F (74 m)','D12# F (64 m)', \
            'D11* F (54 m)','D10# F (54 m)', 'D9# F (44 m)', \
            'D8* F (34 m)','D7# F (34 m)','D6# F (24 m)', \
            'D5* F (14 m)','D4# F (14 m)','D3# F (7 m)', \
            'D2* F (4 m)','D1# F (4 m)','Channel-base Current'])
plt.title("UF 15-"+str(event)+ " return stroke #"+str(RS_number)+" Date: 0"+str(date) )
#plt.xlim([-2,18])
plt.grid()
plt.show()

#Compare 2014 and 2015 diodes looking at the same channel height
plt.subplot(431)
MaxD32=np.max(APD_32.data[::dt1])
MaxD31=np.max(APD_31.data[::dt1])
plt.plot((APD_32.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_32.data[::dt1]/MaxD32,color=[0.8,0.8,0.3],linewidth=2)
plt.plot((APD_31.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_31.data[::dt1]/MaxD31,color=[0.2414,0,0.1034],linewidth=2)
plt.xlim([-20,200])
plt.title('D32* and D31# NF 1 km')
plt.grid()

plt.subplot(432)
MaxD30=np.max(APD_30.data[::dt1])
MaxD29=np.max(APD_29.data[::dt1])
plt.plot((APD_30.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_30.data[::dt1]/MaxD30,color=[0.7241,0.3103,0.8276],linewidth=2)
plt.plot((APD_29.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_29.data[::dt1]/MaxD29,color=[0.8276,1,0],linewidth=2)
plt.xlim([-20,200])
plt.title('D30* and D29# F 900 m')
plt.grid()

plt.subplot(433)
MaxD27=np.max(APD_27.data[::dt1])
MaxD26=np.max(APD_26.data[::dt1])
plt.plot((APD_27.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_27.data[::dt1]/MaxD27,color=[0.4483,0.3793,0.4828],linewidth=2)
plt.plot((APD_26.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_26.data[::dt1]/MaxD26,color=[0.6207,0.7586,1],linewidth=2)
plt.xlim([-20,200])
plt.title('D27* and D26# F 700 m')
plt.grid()

plt.subplot(434)
MaxD24=np.max(APD_24.data[::dt1])
MaxD23=np.max(APD_23.data[::dt1])
plt.plot((APD_24.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_24.data[::dt1]/MaxD24,color=[0.5172,0.4483,0],linewidth=2)
plt.plot((APD_23.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_23.data[::dt1]/MaxD23,color=[0.9655,0.5173,0.0345],linewidth=2)
plt.xlim([-20,200])
plt.ylabel('Normalized Luminosity (digitizer volts)')
plt.title('D24* and D23# F 500 m')
plt.grid()


plt.subplot(435)
MaxD22=np.max(APD_22.data[::dt1])
MaxD21=np.max(APD_21.data[::dt1])
plt.plot((APD_22.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_22.data[::dt1]/MaxD22,color=[0.5517,0.6552,0.4828],linewidth=2)
plt.plot((APD_21.dataTime[::dt1]-yoko_pretrigger)*1e6,APD_21.data[::dt1]/MaxD21,color=[0.5,1,0.5],linewidth=2)
plt.xlim([-20,200])
plt.title('D22* and D21# NF 400 m')
plt.grid()

plt.subplot(436)
MaxD20=np.max(segments_Scope42_APD20[seg])
MaxD19=np.max(segments_Scope42_APD19[seg])
plt.plot((seg_time_Scope42_APD20[::dt2]-lecroy_pretrigger)*1e6, segments_Scope42_APD20[seg][::dt2]/MaxD20,color=[0.5172,0.4483,0],linewidth=2)
plt.plot((seg_time_Scope42_APD19[::dt2]-lecroy_pretrigger)*1e6, segments_Scope42_APD19[seg][::dt2]/MaxD19,color=[0.1379,0.1379,0.0345],linewidth=2)
plt.xlim([-20,200])
plt.title('D20* and D19# F 300 m')
plt.grid()

plt.subplot(437)
MaxD18=np.max(segments_Scope42_APD18[seg])
MaxD17=np.max(segments_Scope42_APD17[seg])
plt.plot((seg_time_Scope42_APD18[::dt2]-lecroy_pretrigger)*1e6, segments_Scope42_APD18[seg][::dt2]/MaxD18,color=[1,0.7586,0.5172],linewidth=2)
plt.plot((seg_time_Scope42_APD17[::dt2]-lecroy_pretrigger)*1e6, segments_Scope42_APD17[seg][::dt2]/MaxD17,color=[0.9655,0.0690,0.3793],linewidth=2)
plt.xlim([-20,200])
plt.title('D18* and D17# F 200 m')
plt.grid()

plt.subplot(438)
MaxD15=np.max(segments_Scope50_APD15[seg])
MaxD14=np.max(segments_Scope50_APD14[seg])
plt.plot((seg_time_Scope50_APD15[::dt2]-lecroy_pretrigger)*1e6, segments_Scope50_APD15[seg][::dt2]/MaxD15,color=[0.8276,0.0690,1],linewidth=2)
plt.plot((seg_time_Scope50_APD14[::dt2]-lecroy_pretrigger)*1e6, segments_Scope50_APD14[seg][::dt2]/MaxD14,color=[0.9655,0.6207,0.8621],linewidth=2)
plt.xlim([-20,200])
plt.title('D15* and D14# F 94 m')
plt.grid()

plt.subplot(439)
MaxD11=np.max(segments_Scope48_APD11[seg])
MaxD10=np.max(segments_Scope48_APD10[seg])
plt.plot((seg_time_Scope48_APD11[::dt2]-lecroy_pretrigger)*1e6, segments_Scope48_APD11[seg][::dt2]/MaxD11,color=[0,0.5172,0.5862],linewidth=2)
plt.plot((seg_time_Scope48_APD10[::dt2]-lecroy_pretrigger)*1e6, segments_Scope48_APD10[seg][::dt2]/MaxD10,color=[0,1,0.7586],linewidth=2)
plt.xlim([-20,200])
plt.title('D11* and D10# F 54 m')
plt.grid()

plt.subplot(4,3,10)
MaxD8=np.max(segments_Scope44_APD8[seg])
MaxD7=np.max(segments_Scope44_APD7[seg])
plt.plot((seg_time_Scope44_APD8[::dt2]-lecroy_pretrigger)*1e6, segments_Scope44_APD8[seg][::dt2]/MaxD8,color=[0.5172,0.5172,1],linewidth=2)
plt.plot((seg_time_Scope44_APD7[::dt2]-lecroy_pretrigger)*1e6, segments_Scope44_APD7[seg][::dt2]/MaxD7,color=[0,0.3448,0],linewidth=2)
plt.xlim([-20,200])
plt.title('D8* and D7# F 34 m')
plt.grid()

plt.subplot(4,3,11)
MaxD5=np.max(segments_Scope44_APD5[seg])
MaxD4=np.max(segments_Scope43_APD4[seg])
plt.plot((seg_time_Scope44_APD5[::dt2]-lecroy_pretrigger)*1e6, segments_Scope44_APD5[seg][::dt2]/MaxD5,color=[1,0.1034,0.7241],linewidth=2)
plt.plot((seg_time_Scope43_APD4[::dt2]-lecroy_pretrigger)*1e6, segments_Scope43_APD4[seg][::dt2]/MaxD4,color=[0, 0, 0.1724],linewidth=2)
plt.xlim([-20,200])
plt.title('D5* and D4# F 14 m')
plt.xlabel('Time ($\mu$s)')
plt.grid()

plt.subplot(4,3,12)
MaxD2=np.max(segments_Scope43_APD2[seg])
MaxD1=np.max(segments_Scope43_APD1[seg])
plt.plot((seg_time_Scope43_APD2[::dt2]-lecroy_pretrigger)*1e6, segments_Scope43_APD2[seg][::dt2]/MaxD2,color=[1,0,0],linewidth=2)
plt.plot((seg_time_Scope43_APD1[::dt2]-lecroy_pretrigger)*1e6, segments_Scope43_APD1[seg][::dt2]/MaxD1,color=[0, 0,1],linewidth=2)
plt.xlim([-20,200])
plt.title('D2* and D1# F 4 m')
plt.grid()
plt.show()

def allspeeds(x1,y1,x2,y2,fs,t0):
    
    c=2.99e8
    sampling_time=1/fs
    x1_10p, x1_20p, x1_50p, x1_80p, x1_90p, x1_RT=noise_analysis(x1,y1,100e6,t0)
    t_10p_x1=x1_10p*sampling_time
    t_20p_x1=x1_20p*sampling_time
    t_50p_x1=x1_50p*sampling_time
    t_80p_x1=x1_80p*sampling_time
    t_90p_x1=x1_90p*sampling_time
    
    x2_10p, x2_20p, x2_50p, x2_80p, x2_90p, x2_RT=noise_analysis(x2,y2,100e6,t0)
    t_10p_x2=x2_10p*sampling_time
    t_20p_x2=x2_20p*sampling_time
    t_50p_x2=x2_50p*sampling_time
    t_80p_x2=x2_80p*sampling_time
    t_90p_x2=x2_90p*sampling_time


    v_10p=(1000-400)/(t_10p_x1-t_10p_x2)
    print("downward speed (measured at 10%%) = %.2fc" %(v_10p/c))
    
    v_20p=(1000-400)/(t_20p_x1-t_20p_x2)
    print("downward speed (measured at 20%%) = %.2fc" %(v_20p/c))
    
    v_50p=(1000-400)/(t_50p_x1-t_50p_x2)
    print("downward speed (measured at 50%%) = %.2fc" %(v_50p/c))
    
    v_80p=(1000-400)/(t_80p_x1-t_80p_x2)
    print("downward speed (measured at 80%%) = %.2fc" %(v_80p/c))
    
    v_90p=(1000-400)/(t_90p_x1-t_90p_x2)
    print("downward speed (measured at 90%%) = %.2fc" %(v_90p/c))

##bottom 1km to 400 m speed
allspeeds(APD_32.dataTime,APD_32.data, \
        APD_21.dataTime,APD_21.data, 100e6,t0)

#bottom 300 m speed
allspeeds(seg_time_Scope42_APD20,segments_Scope42_APD20[seg], \
            seg_time_Scope43_APD1,segments_Scope43_APD1[seg],100e6,0)