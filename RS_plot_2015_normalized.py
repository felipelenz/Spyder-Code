#!/usr/bin/python

import Yoko750 as yk
import lecroy as lc
import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib
from noise_analysis import noise_analysis
from low_pass_filter import LPF
matplotlib.rcParams.update({'font.size': 20})


########################
### INPUT PARAMETERS ###
########################

date=81915
seg=0
RS_number=1
M_comp_number=1
t0=0
event=26
suffix=0

suffix26=1 #lecroy last digit og the .trc file name
suffix41=suffix #yoko Last digit of the .wvf file name
suffix42=suffix #lecroy last digit og the .trc file name
suffix43=suffix #lecroy last digit og the .trc file name
suffix44=suffix #lecroy last digit og the .trc file name
suffix48=suffix #lecroy last digit og the .trc file name
suffix50=suffix #lecroy last digit og the .trc file name
offset=0.7
duplicate_delay=0#6.37252e-6

dt1=1
dt2=1

######################
### IMPORT CURRENT ###
######################

#Current (from scope 26)
lecroy_fileName_IIHI = "/Volumes/2015 Data/0"+str(date)+"/Scope26/C1AC0000"+str(suffix26)+".trc"
lecroy_IIHI = lc.lecroy_data(lecroy_fileName_IIHI)
seg_time_IIHI = lecroy_IIHI.get_seg_time()
segments_IIHI = lecroy_IIHI.get_segments()

#########################
### IMPORT lUMINOSITY ###
#########################

#Yoko
yoko_fileName = "/Volumes/2015 Data/0"+str(date)+"/Scope41/APD000"+str(suffix41)

f = yk.Yoko750File(yoko_fileName)
header = f.get_header()

def assignName(scopeChannel,fileSuffix):
    lecroy_fileName="/Volumes/2015 Data/0"+str(date)+"/Scope43/C"+ \
                    str(scopeChannel)+"AC0000"+str(fileSuffix)+".trc"
    lecroy = lc.lecroy_data(lecroy_fileName)
    seg_time = lecroy.get_seg_time()
    segments = lecroy.get_segments()
    return seg_time, segments
    
##LeCroy
seg_time_Scope43_APD1, segments_Scope43_APD1=assignName(1,suffix43)
seg_time_Scope43_APD2, segments_Scope43_APD2=assignName(2,suffix43)
seg_time_Scope43_APD3, segments_Scope43_APD3=assignName(3,suffix43)
seg_time_Scope43_APD4, segments_Scope43_APD4=assignName(4,suffix43)
seg_time_Scope44_APD5, segments_Scope44_APD5=assignName(1,suffix44)
seg_time_Scope44_APD6, segments_Scope44_APD6=assignName(2,suffix44)
seg_time_Scope44_APD7, segments_Scope44_APD7=assignName(3,suffix44)
seg_time_Scope44_APD8, segments_Scope44_APD8=assignName(4,suffix44)
seg_time_Scope48_APD9, segments_Scope48_APD9=assignName(1,suffix48)
seg_time_Scope48_APD10, segments_Scope48_APD10=assignName(2,suffix48)
seg_time_Scope48_APD11, segments_Scope48_APD11=assignName(3,suffix48)
seg_time_Scope48_APD12, segments_Scope48_APD12=assignName(4,suffix48)
seg_time_Scope50_APD13, segments_Scope50_APD13=assignName(1,suffix50)
seg_time_Scope50_APD14, segments_Scope50_APD14=assignName(2,suffix50)
seg_time_Scope50_APD15, segments_Scope50_APD15=assignName(3,suffix50)
seg_time_Scope50_APD16, segments_Scope50_APD16=assignName(4,suffix50)
seg_time_Scope42_APD17, segments_Scope42_APD17=assignName(1,suffix42)
seg_time_Scope42_APD18, segments_Scope42_APD18=assignName(2,suffix42)
seg_time_Scope42_APD19, segments_Scope42_APD19=assignName(3,suffix42)
seg_time_Scope42_APD20, segments_Scope42_APD20=assignName(4,suffix42)

#t0=0.154235#0#0.098#100e-3 #Take this number from the time between each lecroy trigger (from df32)
tf=t0+10e-3#t0+20e-3#0.11
lecroy_pretrigger=0.005#0.00399934#5e-3#in seconds
yoko_pretrigger=t0+0.005-duplicate_delay#0.1#t0+(14.535e-3) #in seconds

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

###############################
### PLOT ALL DIODES CURRENT ###
###############################

plt.figure(figsize=(8.5,11))
plt.plot((APD_32.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_32.data[::dt1]/np.max(APD_32.data[::dt1])+31*offset,color=[0.8,0.8,0.3],linewidth=2)
plt.plot((APD_31.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_31.data[::dt1]/np.max(APD_31.data[::dt1])+30*offset,color=[0.2414,0,0.1034],linewidth=2)
plt.plot((APD_30.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_30.data[::dt1]/np.max(APD_30.data[::dt1])+29*offset,color=[0.7241,0.3103,0.8276],linewidth=2)
plt.plot((APD_29.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_29.data[::dt1]/np.max(APD_29.data[::dt1])+28*offset,color=[0.8276,1,0],linewidth=2)
plt.plot((APD_28.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_28.data[::dt1]/np.max(APD_28.data[::dt1])+27*offset,color=[0.6207,0,0],linewidth=2)
plt.plot((APD_27.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_27.data[::dt1]/np.max(APD_27.data[::dt1])+26*offset,color=[0.4483,0.3793,0.4828],linewidth=2)
plt.plot((APD_26.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_26.data[::dt1]/np.max(APD_26.data[::dt1])+25*offset,color=[0.6207,0.7586,1],linewidth=2)
plt.plot((APD_25.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_25.data[::dt1]/np.max(APD_25.data[::dt1])+24*offset,color=[0.4483,0.9655,1],linewidth=2)
plt.plot((APD_24.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_24.data[::dt1]/np.max(APD_24.data[::dt1])+23*offset,color=[0.5172,0.4483,0],linewidth=2)
plt.plot((APD_23.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_23.data[::dt1]/np.max(APD_23.data[::dt1])+22*offset,color=[0.9655,0.5173,0.0345],linewidth=2)
plt.plot((APD_22.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_22.data[::dt1]/np.max(APD_22.data[::dt1])+21*offset,color=[0.5517,0.6552,0.4828],linewidth=2)
plt.plot((APD_21.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_21.data[::dt1]/np.max(APD_21.data[::dt1])+20*offset,color=[0.5,1,0.5],linewidth=2)

plt.plot((seg_time_Scope42_APD20[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD20[seg][::dt2]/np.max(segments_Scope42_APD20[seg][::dt2])+19*offset,color=[0.5172,0.4483,0],linewidth=2)
#plt.plot((APD_20.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_20.data[::dt1]/np.max(APD_20.data[::dt1])+19*offset,color=[0.5,1,0.5],linewidth=2)
plt.plot((seg_time_Scope42_APD19[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD19[seg][::dt2]/np.max(segments_Scope42_APD19[seg][::dt2])+18*offset,color=[0.1379,0.1379,0.0345],linewidth=2)
plt.plot((seg_time_Scope42_APD18[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD18[seg][::dt2]/np.max(segments_Scope42_APD18[seg][::dt2])+17*offset,color=[1,0.7586,0.5172],linewidth=2)
plt.plot((seg_time_Scope42_APD17[::dt2]-lecroy_pretrigger)*1e3, segments_Scope42_APD17[seg][::dt2]/np.max(segments_Scope42_APD17[seg][::dt2])+16*offset,color=[0.9655,0.0690,0.3793],linewidth=2)

plt.plot((seg_time_Scope50_APD16[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD16[seg][::dt2]/np.max(segments_Scope50_APD16[seg][::dt2])+15*offset,color=[0.4828,0.1034,0.4138],linewidth=2)
#plt.plot((APD_16.dataTime[::dt1]-yoko_pretrigger)*1e3,APD_16.data[::dt1]+15*offset,color=[0.5172,0.4483,0],linewidth=2)
plt.plot((seg_time_Scope50_APD15[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD15[seg][::dt2]/np.max(segments_Scope50_APD15[seg][::dt2])+14*offset,color=[0.8276,0.0690,1],linewidth=2)
plt.plot((seg_time_Scope50_APD14[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD14[seg][::dt2]/np.max(segments_Scope50_APD14[seg][::dt2])+13*offset,color=[0.9655,0.6207,0.8621],linewidth=2)
plt.plot((seg_time_Scope50_APD13[::dt2]-lecroy_pretrigger)*1e3, segments_Scope50_APD13[seg][::dt2]/np.max(segments_Scope50_APD13[seg][::dt2])+12*offset,color=[0.5862,0.8276,0.3103],linewidth=2)

plt.plot((seg_time_Scope48_APD12[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD12[seg][::dt2]/np.max(segments_Scope48_APD12[seg][::dt2])+11*offset,color=[0,0,0.4828],linewidth=2)
plt.plot((seg_time_Scope48_APD11[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD11[seg][::dt2]/np.max(segments_Scope48_APD11[seg][::dt2])+10*offset,color=[0,0.5172,0.5862],linewidth=2)
plt.plot((seg_time_Scope48_APD10[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD10[seg][::dt2]/np.max(segments_Scope48_APD10[seg][::dt2])+9*offset,color=[0,1,0.7586],linewidth=2)
plt.plot((seg_time_Scope48_APD9[::dt2]-lecroy_pretrigger)*1e3, segments_Scope48_APD9[seg][::dt2]/np.max(segments_Scope48_APD9[seg][::dt2])+8*offset,color=[0.6207,0.3103,0.2759],linewidth=2)

plt.plot((seg_time_Scope44_APD8[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD8[seg][::dt2]/np.max(segments_Scope44_APD8[seg][::dt2])+7*offset,color=[0.5172,0.5172,1],linewidth=2)
plt.plot((seg_time_Scope44_APD7[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD7[seg][::dt2]/np.max(segments_Scope44_APD7[seg][::dt2])+6*offset,color=[0,0.3448,0],linewidth=2)
plt.plot((seg_time_Scope44_APD6[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD6[seg][::dt2]/np.max(segments_Scope44_APD6[seg][::dt2])+5*offset,color=[ 1,0.8276,0],linewidth=2)
plt.plot((seg_time_Scope44_APD5[::dt2]-lecroy_pretrigger)*1e3, segments_Scope44_APD5[seg][::dt2]/np.max(segments_Scope44_APD5[seg][::dt2])+4*offset,color=[1,0.1034,0.7241],linewidth=2)

plt.plot((seg_time_Scope43_APD4[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD4[seg][::dt2]/np.max(segments_Scope43_APD4[seg][::dt2])+3*offset,color=[0, 0, 0.1724],linewidth=2)
plt.plot((seg_time_Scope43_APD3[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD3[seg][::dt2]/np.max(segments_Scope43_APD3[seg][::dt2])+2*offset,color=[0, 1, 0],linewidth=2)
plt.plot((seg_time_Scope43_APD2[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD2[seg][::dt2]/np.max(segments_Scope43_APD2[seg][::dt2])+1*offset,color=[1, 0, 0],linewidth=2)
plt.plot((seg_time_Scope43_APD1[::dt2]-lecroy_pretrigger)*1e3, segments_Scope43_APD1[seg][::dt2]/np.max(segments_Scope43_APD1[seg][::dt2])+0*offset,color=[0, 0, 1],linewidth=2)
#
#plt.plot((seg_time_IIHI[::dt2]-lecroy_pretrigger/2-8e-6)*1e3, segments_IIHI[seg][::dt2]/np.max(segments_IIHI[seg][::dt2])-1*offset,color=[0.3, 0.3, 0.3],linewidth=2)
#
#plt.xlabel('Time (ms)')
#plt.ylabel('Luminosity (digitizer volts)')

#plt.legend(['D32* NF (1 km)','D31# NF (1 km)','D30* F (900 m)', \
#            'D29# F (900 m)','D28# NF (800 m)','D27* F (700 m)', \
#            'D26# F (700 m)','D25# NF (600 m)','D24* F (500 m)', \
#            'D23# F (500 m)','D22* NF (400 m)','D21# NF (400 m)', \
#            'D20* F (300 m)','D19# F (300 m)','D18* F (200 m)', \
#            'D17# F (200 m)', \
#            'D16# F (154 m)','D15* F (94 m)', \
#            'D14# F (94 m)','D13# F (74 m)','D12# F (64 m)', \
#            'D11* F (54 m)','D10# F (54 m)', 'D9# F (44 m)', \
#            'D8* F (34 m)','D7# F (34 m)','D6# F (24 m)', \
#            'D5* F (14 m)','D4# F (14 m)','D3# F (7 m)', \
#            'D2* F (4 m)','D1# F (4 m)','Channel-base Current'])
#plt.title("UF 15-"+str(event)+ " return stroke #"+str(RS_number)+" Date: 0"+str(date) )
#plt.xlim([-0.5,1])
#plt.grid()
#plt.tight_layout()
#plt.savefig('Event UF15-'+str(event)+', RS #'+str(RS_number)+', M-comp #'+str(M_comp_number)+'.pdf', dpi = 300)
plt.show()

###########################################
### CHANNEL-BASE CURRENT AND LUMINOSITY ###
###########################################
## This part of the code needs editing because delays haven't been measured 
## accurately as of 11-09-2015

#c=2.99e8 #speed of light
##Put t=0 at max peak current
#shift_to_t_equals_zero=(np.argmax(segments_IIHI[seg][::dt2]))/500e6 - lecroy_pretrigger/2 # scope26 sampling rate is 500 MHz
#
##Calculate photodiode signal delay
#free_space_propagation_delay=293/c #from launcher to Office Trailer
#cable_delay=16e-9 #measured from photodiode output to scope (10ft coax)
#APD1_time_delay=free_space_propagation_delay+cable_delay#-shift_to_t_equals_zero #total APD delay
#
##Calculate current signal delay
#current_launcher_time_delay=10.2/c #from launcher tip to current shunt
#fiber_delay=4983e-9 - 4e-6#From 2013 time delay spreadsheet
#current_time_delay=current_launcher_time_delay+fiber_delay#-shift_to_t_equals_zero #total current delay
#
##sintax for plotyy: Plot simulteneously measured current and luminosity
#fig,ax1=plt.subplots()
#ax2=ax1.twinx()
#ax1.plot((seg_time_Scope43_APD1[::dt2]-lecroy_pretrigger-APD1_time_delay)*1e6, segments_Scope43_APD1[seg][::dt2]/np.max(segments_Scope43_APD1[seg][::dt2]),color='r',linewidth=2,label="D1# F (4 m)")
#ax1.plot((seg_time_Scope43_APD2[::dt2]-lecroy_pretrigger-APD1_time_delay)*1e6, segments_Scope43_APD2[seg][::dt2]/np.max(segments_Scope43_APD2[seg][::dt2]),color='g',linewidth=2,label="D2* F (4 m)")
#ax1.plot([-100,100],[0.1,0.1],'r--')
#ax1.plot([-100,100],[0.2,0.2],'r--')
#ax1.plot([-100,100],[0.9,0.9],'r--')
#ax2.plot((seg_time_IIHI[::dt2]-lecroy_pretrigger/2-current_time_delay)*1e6, segments_IIHI[seg][::dt2]/np.max(segments_IIHI[seg][::dt2]),color='b',linewidth=2,label="Current")
#ax1.set_xlabel('Time ($\mu$s)')
#ax1.set_ylabel('Normalized Luminosity (digitizer volts)',color='r')
#ax2.set_ylabel('Normalized Channel-Base Current',color='b')
#plt.xlim(-20,20)
#ax1.legend(loc=2)
#ax2.legend(loc=1)
#plt.title("UF 15-"+str(event)+ " return stroke #"+str(RS_number)+" Date: 0"+str(date) )
#plt.grid()
#plt.show()
#
##Measure Current-to-luminosity delay at 10%, 20%, and 50% amplitude levels
#IIHI_percentage_points=noise_analysis((seg_time_IIHI[::dt2]-lecroy_pretrigger/2-current_time_delay),segments_IIHI[seg][::dt2],500e6,lecroy_pretrigger/2) #current pretrigger for scope26 is 2.5e-3 s
#
##2015 APD
#APD1_percentage_points=noise_analysis((seg_time_Scope43_APD1[::dt2]-lecroy_pretrigger-APD1_time_delay),segments_Scope43_APD1[seg][::dt2],100e6,lecroy_pretrigger) #luminosity pretrigger for scope43 is 5e-3 s
#
#Current_to_luminosity_delay_10p=(APD1_percentage_points[0]/100e6-lecroy_pretrigger/2-APD1_time_delay)-(IIHI_percentage_points[0]/500e6-current_time_delay)
#Current_to_luminosity_delay_20p=(APD1_percentage_points[1]/100e6-lecroy_pretrigger/2-APD1_time_delay)-(IIHI_percentage_points[1]/500e6-current_time_delay)
#Current_to_luminosity_delay_50p=(APD1_percentage_points[2]/100e6-lecroy_pretrigger/2-APD1_time_delay)-(IIHI_percentage_points[2]/500e6-current_time_delay)
#print("2015 APD (D1): Current risetime = %r, Luminosity Risetime = %r" %(IIHI_percentage_points[5],APD1_percentage_points[5]))
#print("current-to-luminosity delay at 10p = %r, 20p = %r, 50p = %r" %(Current_to_luminosity_delay_10p,Current_to_luminosity_delay_20p,Current_to_luminosity_delay_20p))
#
##2014 APD
#APD2_percentage_points=noise_analysis((seg_time_Scope43_APD2[::dt2]-lecroy_pretrigger-APD1_time_delay),segments_Scope43_APD2[seg][::dt2],100e6,lecroy_pretrigger) #luminosity pretrigger for scope43 is 5e-3 s
#
#Current_to_luminosity_delay_10p=(APD2_percentage_points[0]/100e6-lecroy_pretrigger/2-APD1_time_delay)-(IIHI_percentage_points[0]/500e6-current_time_delay)
#Current_to_luminosity_delay_20p=(APD2_percentage_points[1]/100e6-lecroy_pretrigger/2-APD1_time_delay)-(IIHI_percentage_points[1]/500e6-current_time_delay)
#Current_to_luminosity_delay_50p=(APD2_percentage_points[2]/100e6-lecroy_pretrigger/2-APD1_time_delay)-(IIHI_percentage_points[2]/500e6-current_time_delay)
#print("2014 APD (D2): Current risetime = %r, Luminosity Risetime = %r" %(IIHI_percentage_points[5],APD2_percentage_points[5]))
#print("current-to-luminosity delay at 10p = %r, 20p = %r, 50p = %r" %(Current_to_luminosity_delay_10p,Current_to_luminosity_delay_20p,Current_to_luminosity_delay_20p))


##################################################################
### Calculate Upward return stroke speed/downward M-comp speed ###
##################################################################

#Create .csv table to print the results
ofile=open('M-components.csv','w')
mywriter=csv.writer(ofile)
mywriter.writerow(['Event UF15-'+str(event)+' RS#'+str(RS_number)+' M-comp #'+str(M_comp_number)])
mywriter.writerow(['Diode 1 to Diode 31 speed at 20%',\
                   'Diode 1 to Diode 31 speed at 50%',\
                   'Diode 1 to Diode 31 speed at 80%',\
                   'Diode 31 10-90% risetime',\
                   'Diode 1 10-90% risetime']) #Each columns title

def allspeeds(x1,y1,x2,y2,fs1,fs2,t0,z1,z2,t_IRIG):
    propagation_delay=np.sqrt(z1*z1+293*293)/2.99e8-np.sqrt(z2*z2+293*293)/2.99e8
    print("propagation delay=",propagation_delay)
        
    t_10p_x1, t_20p_x1, t_50p_x1, t_80p_x1, t_90p_x1, x1_RT,xx1,yy1=noise_analysis(x1,y1,fs1,t0)
    print("waveform 1 10-90%% risetime=",x1_RT)
    t_10p_x2, t_20p_x2, t_50p_x2, t_80p_x2, t_90p_x2, x2_RT,xx2,yy2=noise_analysis(x2,y2,fs2,t0)
    print("waveform 2 10-90%% risetime=",x2_RT)
    
    v_10p=(z1-z2)/(t_10p_x1+t_IRIG-t_10p_x2-propagation_delay)
    print("upward RS speed (measured at 10%%) = %r" %(v_10p))
    
    v_20p=(z1-z2)/(t_20p_x1+t_IRIG-t_20p_x2-propagation_delay)
    print("upward RS speed (measured at 20%%) = %r" %(v_20p))
    
    v_50p=(z1-z2)/(t_50p_x1+t_IRIG-t_50p_x2-propagation_delay)
    print("upward RS speed (measured at 50%%) = %r" %(v_50p))
    
    v_80p=(z1-z2)/(t_80p_x1+t_IRIG-t_80p_x2-propagation_delay)
    print("upward RS speed (measured at 80%%) = %r" %(v_80p))
    
    v_90p=(z1-z2)/(t_90p_x1+t_IRIG-t_90p_x2-propagation_delay)
    print("upward RS speed (measured at 90%%) = %r" %(v_90p))
    
    mywriter.writerow([v_20p, v_50p, v_80p, x1_RT, x2_RT])
    return xx1,yy1,xx2,yy2


##For M-Components, uncomment the moving average data! 
##########################
## Moving Average Filter #
##########################
#def movingaverage(interval, window_size):
#    window= np.ones(int(window_size))/float(window_size)
#    return np.convolve(interval, window, 'same')

################
### APD 2014 ###
################

# Find speed between two heights
# D2 to D32 

# Low Pass Filter data at 400 kHz
APD_31.data=LPF(APD_31.dataTime,APD_31.data,100e6)
segments_Scope43_APD1[seg]=LPF(seg_time_Scope43_APD1,segments_Scope43_APD1[seg],100e6)

waveforms=allspeeds((APD_31.dataTime-yoko_pretrigger),APD_31.data,\
                    (seg_time_Scope43_APD1-lecroy_pretrigger),segments_Scope43_APD1[seg],\
                    100e6,100e6,-5e-3,1002,1,duplicate_delay)

plt.plot((waveforms[0])*1e3,waveforms[1])
plt.plot((waveforms[2])*1e3,waveforms[3])
plt.legend(['Diode 31 (1 km)','Diode 1 (4 m)'], loc=0)
plt.xlabel('Time (ms)')
plt.ylabel('Uncalibrated Luminosity')
plt.title('Event UF15-'+str(event)+', RS #'+str(RS_number)+', M-comp #'+str(M_comp_number))
plt.grid()
plt.show()

plt.figure(figsize=(11,8.5))
plt.plot((waveforms[0])*1e3,waveforms[1]/np.max(waveforms[1]),color=[0.2414,0,0.1034],linewidth=2)
plt.plot((waveforms[2])*1e3,waveforms[3]/np.max(waveforms[3]),color=[0,0,1],linewidth=2)
plt.legend(['Diode 31 (1 km)','Diode 1 (4 m)'], loc=0)
plt.xlabel('Time (ms)')
plt.ylabel('Normalized Luminosity')
plt.title('Event UF15-'+str(event)+', RS#'+str(RS_number)+', M-comp #'+str(M_comp_number))
plt.grid()
plt.tight_layout()
plt.savefig('Event UF15-'+str(event)+', RS #'+str(RS_number)+', M-comp #'+str(M_comp_number)+'.pdf', dpi = 300)
plt.show()

##D2 to D18
#segments_Scope43_APD2[seg]=movingaverage(segments_Scope43_APD2[seg],100)
#segments_Scope42_APD18[seg]=movingaverage(segments_Scope42_APD18[seg],100)
#
#seg_time_Scope43_APD2=movingaverage(seg_time_Scope43_APD2,100)
#seg_time_Scope42_APD18=movingaverage(seg_time_Scope42_APD18,100)
#
#waveforms=allspeeds(seg_time_Scope42_APD18,segments_Scope42_APD18[seg], \
#                    seg_time_Scope43_APD2,segments_Scope43_APD2[seg],100e6,100e6,0,205.9,1,duplicate_delay)
#
#plt.plot((waveforms[0])*1e3,waveforms[1])
#plt.plot((waveforms[2])*1e3,waveforms[3])
#plt.legend(['Diode 18 (200 m)','Diode 2 (4 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Uncalibrated Luminosity')
#plt.title('Event UF15-'+str(event)+', RS #'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()
#
#plt.plot((waveforms[0])*1e3,waveforms[1]/np.max(waveforms[1]))
#plt.plot((waveforms[2])*1e3,waveforms[3]/np.max(waveforms[3]))
#plt.legend(['Diode 18 (200 m)','Diode 2 (4 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Normalized Luminosity')
#plt.title('Event UF15-'+str(event)+', RS#'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()
#
##D22 to D32
#APD_32.dataTime=movingaverage(APD_32.dataTime,100)
#APD_22.dataTime=movingaverage(APD_22.dataTime,100)
#
#APD_32.data=movingaverage(APD_32.data,100)
#APD_22.data=movingaverage(APD_22.data,100)
#
#mywriter.writerow(['Diode 22 to Diode 32 speed at 20%',\
#                   'Diode 22 to Diode 32 speed at 50%',\
#                   'Diode 22 to Diode 32 speed at 80%',\
#                   'Diode 32 10-90% risetime',\
#                   'Diode 22 10-90% risetime'])
##it is very important to include -t0 below, otherwise the noise analysis won't work
#waveforms=allspeeds(APD_32.dataTime-t0,APD_32.data, \
#                    APD_22.dataTime-t0,APD_22.data,100e6,100e6,0,935,426.3,duplicate_delay)
#
#plt.plot((waveforms[0])*1e3,waveforms[1])
#plt.plot((waveforms[2])*1e3,waveforms[3])
#plt.legend(['Diode 32 (1 km)','Diode 22 (400 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Uncalibrated Luminosity')
#plt.title('Event UF15-'+str(event)+', RS #'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()
#
#plt.plot((waveforms[0])*1e3,waveforms[1]/np.max(waveforms[1]))
#plt.plot((waveforms[2])*1e3,waveforms[3]/np.max(waveforms[3]))
#plt.legend(['Diode 32 (1 km)','Diode 22 (400 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Normalized Luminosity')
#plt.title('Event UF15-'+str(event)+', RS#'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()

##!!!!!!!!!!APD 2015!!!!!!!!!!!!
##D1 to D17
#
#seg_time_Scope42_APD17=movingaverage(seg_time_Scope42_APD17,100)
#segments_Scope42_APD17[seg]=movingaverage(segments_Scope42_APD17[seg],100)
#
#seg_time_Scope43_APD1=movingaverage(seg_time_Scope43_APD1,100)
#segments_Scope43_APD1[seg]=movingaverage(segments_Scope43_APD1[seg],100)
#
#mywriter.writerow(['Diode 1 to Diode 17 speed at 20%',\
#                   'Diode 1 to Diode 17 speed at 50%',\
#                   'Diode 1 to Diode 17 speed at 80%',\
#                   'Diode 17 10-90% risetime',\
#                   'Diode 1 10-90% risetime'])
#waveforms=allspeeds(seg_time_Scope42_APD17,segments_Scope42_APD17[seg], \
#                    seg_time_Scope43_APD1,segments_Scope43_APD1[seg],100e6,100e6,0,191.7,1,duplicate_delay)
#
#plt.plot((waveforms[0])*1e3,waveforms[1])
#plt.plot((waveforms[2])*1e3,waveforms[3])
#plt.legend(['Diode 17 (200 m)','Diode 1 (4 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Uncalibrated Luminosity')
#plt.title('Event UF15-'+str(event)+', RS #'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()
#
#plt.plot((waveforms[0])*1e3,waveforms[1]/np.max(waveforms[1]))
#plt.plot((waveforms[2])*1e3,waveforms[3]/np.max(waveforms[3]))
#plt.legend(['Diode 17 (200 m)','Diode 1 (4 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Normalized Luminosity')
#plt.title('Event UF15-'+str(event)+', RS#'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()
#
##D21 to D31
#APD_31.dataTime=movingaverage(APD_31.dataTime,100)
#APD_21.dataTime=movingaverage(APD_21.dataTime,100)
#
#APD_32.data=movingaverage(APD_32.data,100)
#APD_22.data=movingaverage(APD_22.data,100)
#
#mywriter.writerow(['Diode 21 to Diode 31 speed at 20%',\
#                   'Diode 21 to Diode 31 speed at 50%',\
#                   'Diode 21 to Diode 31 speed at 80%',\
#                   'Diode 31 10-90% risetime',\
#                   'Diode 21 10-90% risetime'])
##it is very important to include -t0 below, otherwise the noise analysis won't work
#waveforms=allspeeds(APD_31.dataTime-t0,APD_31.data, \
#                    APD_21.dataTime-t0,APD_21.data,100e6,100e6,0,1002,387.4,duplicate_delay)
#
#plt.plot((waveforms[0])*1e3,waveforms[1])
#plt.plot((waveforms[2])*1e3,waveforms[3])
#plt.legend(['Diode 31 (1 km)','Diode 21 (400 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Uncalibrated Luminosity')
#plt.title('Event UF15-'+str(event)+', RS #'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()
#
#plt.plot((waveforms[0])*1e3,waveforms[1]/np.max(waveforms[1]))
#plt.plot((waveforms[2])*1e3,waveforms[3]/np.max(waveforms[3]))
#plt.legend(['Diode 31 (1 km)','Diode 21 (400 m)'], loc=0)
#plt.xlabel('Time (ms)')
#plt.ylabel('Normalized Luminosity')
#plt.title('Event UF15-'+str(event)+', RS#'+str(RS_number))#+', M-comp #'+str(M_comp_number))
#plt.grid()
#plt.show()

#!!!!!!!!!!!!!!!!Compare 2014 and 2015 diodes looking at the same channel height!!!!!!!!!!!!!!!!!!
plt.figure(figsize=(14,8))
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

ofile.close()