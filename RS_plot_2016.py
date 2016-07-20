#!/usr/bin/python

import lecroy as lc
import numpy as np
import matplotlib.pyplot as plt

def RS_plot_2016(date,event,seg,RS_number,suffix):
    plt.figure(figsize=(10.9,15.8))
    
    suffix43=suffix
    suffix44=suffix
    suffix48=suffix
    suffix50=suffix
    suffix39=suffix
    suffix42=suffix
    suffix37=suffix
    suffix29=suffix
    
    luminosity_peak=list()
    ax=plt.subplot(111)
    ##LeCroy
    #Diode 1
    lecroy_fileName_Scope43_APD1 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C1AC0000"+str(suffix43)+".trc"
    scope43_D1 = lc.lecroy_data(lecroy_fileName_Scope43_APD1)
    D1_time = scope43_D1.get_seg_time()
    D1_data = scope43_D1.get_segments()
    D1_data=D1_data[seg]*1.2
    
    plt.plot((D1_time-5e-3)*1e6,D1_data,label='D1# (0 m)')
    
    offset=np.max(D1_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D1_data))
    
    ##Diode +1
    #lecroy_fileName_Scope29_APD1 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope29/C4AC0000"+str(suffix29)+".trc"
    #scope29_D1 = lc.lecroy_data(lecroy_fileName_Scope29_APD1)
    #D1_time = scope29_D1.get_seg_time()
    #D1_data = scope29_D1.get_segments()
    #D1_data=D1_data[seg]*1.2
    #
    #plt.plot(D1_time,D1_data)
    #plt.plot()
    
    #Diode 2
    lecroy_fileName_Scope43_APD2 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C2AC0000"+str(suffix43)+".trc"
    scope43_D2 = lc.lecroy_data(lecroy_fileName_Scope43_APD2)
    D2_time = scope43_D2.get_seg_time()
    D2_data = scope43_D2.get_segments()
    D2_data=D2_data[seg]*1.0
    plt.plot((D2_time-5e-3)*1e6,D2_data+offset,label='D2 (0 m)')
    
    offset=offset+np.max(D2_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D2_data))
    
    #Diode 3
    lecroy_fileName_Scope43_APD3 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C3AC0000"+str(suffix43)+".trc"
    scope43_D3 = lc.lecroy_data(lecroy_fileName_Scope43_APD3)
    D3_time = scope43_D3.get_seg_time()
    D3_data = scope43_D3.get_segments()
    D3_data=D3_data[seg]*1.3
    
    plt.plot((D3_time-5e-3)*1e6,D3_data+offset,label='D3# (50 m)')
    
    offset=offset+np.max(D3_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D3_data))
    
    #Diode 4
    lecroy_fileName_Scope43_APD4 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C4AC0000"+str(suffix43)+".trc"
    scope43_D4 = lc.lecroy_data(lecroy_fileName_Scope43_APD4)
    D4_time = scope43_D4.get_seg_time()
    D4_data = scope43_D4.get_segments()
    D4_data=D4_data[seg]*1.2
    
    plt.plot((D4_time-5e-3)*1e6,D4_data+offset,label='D4# (100 m)')
    
    offset=offset+np.max(D4_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D4_data))
    
    #Diode 5
    lecroy_fileName_Scope44_APD5 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope44/C1AC0000"+str(suffix44)+".trc"
    scope44_D5 = lc.lecroy_data(lecroy_fileName_Scope44_APD5)
    D5_time = scope44_D5.get_seg_time()
    D5_data = scope44_D5.get_segments()
    D5_data=D5_data[seg]*.82
    
    plt.plot((D5_time-5e-3)*1e6,D5_data+offset,label='D5 (100 m)')
    
    offset=offset+np.max(D5_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D5_data))
    
    #Diode 6
    lecroy_fileName_Scope44_APD6 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope44/C2AC0000"+str(suffix44)+".trc"
    scope44_D6 = lc.lecroy_data(lecroy_fileName_Scope44_APD6)
    D6_time = scope44_D6.get_seg_time()
    D6_data = scope44_D6.get_segments()
    D6_data=D6_data[seg]*1.18
    
    plt.plot((D6_time-5e-3)*1e6,D6_data+offset,label='D6# (150 m)')
    
    offset=offset+np.max(D6_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D6_data))
    
    #Diode 7
    lecroy_fileName_Scope44_APD7 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope44/C3AC0000"+str(suffix44)+".trc"
    scope44_D7 = lc.lecroy_data(lecroy_fileName_Scope44_APD7)
    D7_time = scope44_D7.get_seg_time()
    D7_data = scope44_D7.get_segments()
    D7_data=D7_data[seg]*1.4
    
    plt.plot((D7_time-5e-3)*1e6,D7_data+offset,label='D7# (200 m)')
    
    offset=offset+np.max(D7_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D7_data))
    
    #Diode 8
    lecroy_fileName_Scope44_APD8 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope44/C4AC0000"+str(suffix44)+".trc"
    scope44_D8 = lc.lecroy_data(lecroy_fileName_Scope44_APD8)
    D8_time = scope44_D8.get_seg_time()
    D8_data = scope44_D8.get_segments()
    D8_data=D8_data[seg]*.57
    
    plt.plot((D8_time-5e-3)*1e6,D8_data+offset,label='D8 (200 m)')
    
    offset=offset+np.max(D8_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D8_data))
    
    #Diode 9
    lecroy_fileName_Scope48_APD9 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope48/C1AC0000"+str(suffix48)+".trc"
    scope48_D9 = lc.lecroy_data(lecroy_fileName_Scope48_APD9)
    D9_time = scope48_D9.get_seg_time()
    D9_data = scope48_D9.get_segments()
    D9_data=D9_data[seg]*1.37
    
    plt.plot((D9_time-5e-3)*1e6,D9_data+offset,label='D9# (250 m)')
    
    offset=offset+np.max(D9_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D9_data))
    
    #Diode 10
    lecroy_fileName_Scope48_APD10 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope48/C2AC0000"+str(suffix48)+".trc"
    scope48_D10 = lc.lecroy_data(lecroy_fileName_Scope48_APD10)
    D10_time = scope48_D10.get_seg_time()
    D10_data = scope48_D10.get_segments()
    D10_data=D10_data[seg]*1.48
    
    plt.plot((D10_time-5e-3)*1e6,D10_data+offset,label='D10# (300 m)')
    
    offset=offset+np.max(D10_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D10_data))
    
    #Diode 11
    lecroy_fileName_Scope48_APD11 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope48/C3AC0000"+str(suffix48)+".trc"
    scope48_D11 = lc.lecroy_data(lecroy_fileName_Scope48_APD11)
    D11_time = scope48_D11.get_seg_time()
    D11_data = scope48_D11.get_segments()
    D11_data=D11_data[seg]*0.81
    
    plt.plot((D11_time-5e-3)*1e6,D11_data+offset,label='D11 (300 m)')
    
    offset=offset+np.max(D11_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D11_data))
    
    #Diode 12
    lecroy_fileName_Scope48_APD12 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope48/C4AC0000"+str(suffix48)+".trc"
    scope48_D12 = lc.lecroy_data(lecroy_fileName_Scope48_APD12)
    D12_time = scope48_D12.get_seg_time()
    D12_data = scope48_D12.get_segments()
    D12_data=D12_data[seg]*1.49
    
    plt.plot((D12_time-5e-3)*1e6,D12_data+offset,label='D12# (350 m)')
    
    offset=offset+np.max(D12_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D12_data))
    
    #Diode 13
    lecroy_fileName_Scope50_APD13 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope50/C1AC0000"+str(suffix50)+".trc"
    scope50_D13 = lc.lecroy_data(lecroy_fileName_Scope50_APD13)
    D13_time = scope50_D13.get_seg_time()
    D13_data = scope50_D13.get_segments()
    D13_data=D13_data[seg]*1.24
    
    plt.plot((D13_time-5e-3)*1e6,D13_data+offset,label='D13# (400 m)')
    
    offset=offset+np.max(D13_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D13_data))
    
    #Diode 14
    lecroy_fileName_Scope50_APD14 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope50/C2AC0000"+str(suffix50)+".trc"
    scope50_D14 = lc.lecroy_data(lecroy_fileName_Scope50_APD14)
    D14_time = scope50_D14.get_seg_time()
    D14_data = scope50_D14.get_segments()
    D14_data=D14_data[seg]*1.62
    
    plt.plot((D14_time-5e-3)*1e6,D14_data+offset,label='D14 (400 m)')
    
    offset=offset+np.max(D14_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D14_data))
    
    #Diode 15
    lecroy_fileName_Scope50_APD15 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope50/C3AC0000"+str(suffix50)+".trc"
    scope50_D15 = lc.lecroy_data(lecroy_fileName_Scope50_APD15)
    D15_time = scope50_D15.get_seg_time()
    D15_data = scope50_D15.get_segments()
    D15_data=D15_data[seg]*0.78
    
    plt.plot((D15_time-5e-3)*1e6,D15_data+offset,label='D15# (450 m)')
    
    offset=offset+np.max(D15_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D15_data))
    
    #Diode 16
    lecroy_fileName_Scope50_APD16 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope50/C4AC0000"+str(suffix50)+".trc"
    scope50_D16 = lc.lecroy_data(lecroy_fileName_Scope50_APD16)
    D16_time = scope50_D16.get_seg_time()
    D16_data = scope50_D16.get_segments()
    D16_data=D16_data[seg]*1.64
    
    plt.plot((D16_time-5e-3)*1e6,D16_data+offset,label='D16# (500 m)')
    
    offset=offset+np.max(D16_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D16_data))
    
    #Diode 17
    lecroy_fileName_Scope39_APD17 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope39/C1AC0000"+str(suffix39)+".trc"
    scope39_D17 = lc.lecroy_data(lecroy_fileName_Scope39_APD17)
    D17_time = scope39_D17.get_seg_time()
    D17_data = scope39_D17.get_segments()
    D17_data = D17_data[seg]*1.34
    plt.plot((D17_time-5e-3)*1e6,D17_data+offset,label='D17 (500 m)')
    
    offset=offset+np.max(D17_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D17_data))
    
    #Diode 18
    lecroy_fileName_Scope39_APD18 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope39/C2AC0000"+str(suffix39)+".trc"
    scope39_D18 = lc.lecroy_data(lecroy_fileName_Scope39_APD18)
    D18_time = scope39_D18.get_seg_time()
    D18_data = scope39_D18.get_segments()
    D18_data=D18_data[seg]*0.78
    
    plt.plot((D18_time-5e-3)*1e6,D18_data+offset,label='D18# (550 m)')
    
    offset=offset+np.max(D18_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D18_data))
    
    #Diode 19
    lecroy_fileName_Scope39_APD19 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope39/C3AC0000"+str(suffix39)+".trc"
    scope39_D19 = lc.lecroy_data(lecroy_fileName_Scope39_APD19)
    D19_time = scope39_D19.get_seg_time()
    D19_data = scope39_D19.get_segments()
    D19_data=D19_data[seg]*1.97
    
    plt.plot((D19_time-5e-3)*1e6,D19_data+offset,label='D19# (600 m)')
    
    offset=offset+np.max(D19_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D19_data))
    
    #Diode 20
    lecroy_fileName_Scope39_APD20 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope39/C4AC0000"+str(suffix39)+".trc"
    scope39_D20 = lc.lecroy_data(lecroy_fileName_Scope39_APD20)
    D20_time = scope39_D20.get_seg_time()
    D20_data = scope39_D20.get_segments()
    D20_data=D20_data[seg]*0.76
    
    plt.plot((D20_time-5e-3)*1e6,D20_data+offset,label='D20 (600 m)')
    
    offset=offset+np.max(D20_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D20_data))
    
    #Diode 21
    lecroy_fileName_Scope42_APD21 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope42/C1AC0000"+str(suffix42)+".trc"
    scope42_D21 = lc.lecroy_data(lecroy_fileName_Scope42_APD21)
    D21_time = scope42_D21.get_seg_time()
    D21_data = scope42_D21.get_segments()
    D21_data=D21_data[seg]*1.64
    
    plt.plot((D21_time-5e-3)*1e6,D21_data+offset,label='D21# (650 m)')
    
    offset=offset+np.max(D21_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D21_data))
    
    #Diode 22
    lecroy_fileName_Scope42_APD22 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope42/C2AC0000"+str(suffix42)+".trc"
    scope42_D22 = lc.lecroy_data(lecroy_fileName_Scope42_APD22)
    D22_time = scope42_D22.get_seg_time()
    D22_data = scope42_D22.get_segments()
    D22_data=D22_data[seg]*0.82
    
    plt.plot((D22_time-5e-3)*1e6,D22_data+offset,label='D22# (700 m)')
    
    offset=offset+np.max(D22_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D22_data))
    
    #Diode 23
    lecroy_fileName_Scope42_APD23 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope42/C3AC0000"+str(suffix42)+".trc"
    scope42_D23 = lc.lecroy_data(lecroy_fileName_Scope42_APD23)
    D23_time = scope42_D23.get_seg_time()
    D23_data = scope42_D23.get_segments()
    D23_data=D23_data[seg]*1.54
    
    plt.plot((D23_time-5e-3)*1e6,D23_data+offset,label='D23 (700 m)')
    
    offset=offset+np.max(D23_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D23_data))
    
    #Diode 24
    lecroy_fileName_Scope42_APD24 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope42/C4AC0000"+str(suffix42)+".trc"
    scope42_D24 = lc.lecroy_data(lecroy_fileName_Scope42_APD24)
    D24_time = scope42_D24.get_seg_time()
    D24_data = scope42_D24.get_segments()
    D24_data=D24_data[seg]*0.82
    
    plt.plot((D24_time-5e-3)*1e6,D24_data+offset,label='D24# (750 m)')
    
    offset=offset+np.max(D24_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D24_data))
    
    #Diode 25
    lecroy_fileName_Scope37_APD25 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope37/C1AC0000"+str(suffix37)+".trc"
    scope37_D25 = lc.lecroy_data(lecroy_fileName_Scope37_APD25)
    D25_time = scope37_D25.get_seg_time()
    D25_data = scope37_D25.get_segments()
    D25_data=D25_data[seg]*0.95
    
    plt.plot((D25_time-5e-3)*1e6,D25_data+offset,label='D25# (800 m)')
    
    offset=offset+np.max(D25_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D25_data))
    
    #Diode 26
    lecroy_fileName_Scope37_APD26 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope37/C2AC0000"+str(suffix37)+".trc"
    scope37_D26 = lc.lecroy_data(lecroy_fileName_Scope37_APD26)
    D26_time = scope37_D26.get_seg_time()
    D26_data = scope37_D26.get_segments()
    D26_data=D26_data[seg]*1.44
    
    plt.plot((D26_time-5e-3)*1e6,D26_data+offset,label='D26 (800 m)')
    
    offset=offset+np.max(D26_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D26_data))
    
    #Diode 27
    lecroy_fileName_Scope37_APD27 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope37/C3AC0000"+str(suffix37)+".trc"
    scope37_D27 = lc.lecroy_data(lecroy_fileName_Scope37_APD27)
    D27_time = scope37_D27.get_seg_time()
    D27_data = scope37_D27.get_segments()
    D27_data=D27_data[seg]*0.89
    
    plt.plot((D27_time-5e-3)*1e6,D27_data+offset,label='D27# (850 m)')
    
    offset=offset+np.max(D27_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D27_data))
    
    #Diode 28
    lecroy_fileName_Scope37_APD28 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope37/C4AC0000"+str(suffix37)+".trc"
    scope37_D28 = lc.lecroy_data(lecroy_fileName_Scope37_APD28)
    D28_time = scope37_D28.get_seg_time()
    D28_data = scope37_D28.get_segments()
    D28_data=D28_data[seg]*0.98
    
    plt.plot((D28_time-5e-3)*1e6,D28_data+offset,label='D28# (900 m)')
    
    offset=offset+np.max(D28_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D28_data))
    
    #Diode 29
    lecroy_fileName_Scope29_APD29 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope29/C1AC0000"+str(suffix29)+".trc"
    scope29_D29 = lc.lecroy_data(lecroy_fileName_Scope29_APD29)
    D29_time = scope29_D29.get_seg_time()
    D29_data = scope29_D29.get_segments()
    D29_data=D29_data[seg]*1.80
    
    plt.plot((D29_time-5e-3)*1e6,D29_data+offset,label='D29 (900 m)')
    
    offset=offset+np.max(D29_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D29_data))
    
    #Diode 30
    lecroy_fileName_Scope29_APD30 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope29/C2AC0000"+str(suffix29)+".trc"
    scope29_D30 = lc.lecroy_data(lecroy_fileName_Scope29_APD30)
    D30_time = scope29_D30.get_seg_time()
    D30_data = scope29_D30.get_segments()
    D30_data=D30_data[seg]*0.91
    
    plt.plot((D30_time-5e-3)*1e6,D30_data+offset,label='D30# (1 km)')
    
    offset=offset+np.max(D30_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D30_data))
    
    #Diode 31
    lecroy_fileName_Scope29_APD31 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope29/C3AC0000"+str(suffix29)+".trc"
    scope29_D31 = lc.lecroy_data(lecroy_fileName_Scope29_APD31)
    D31_time = scope29_D31.get_seg_time()
    D31_data = scope29_D31.get_segments()
    D31_data=D31_data[seg]*1.78
    
    plt.plot((D31_time-5e-3)*1e6,D31_data+offset,label='D31 (1 km)')
    
    offset=offset+np.max(D31_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D31_data))
    
    plt.grid()
    plt.xlabel('Time $\mu s$')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1]).draggable()
    plt.title('Event UF 16-'+str(event)+', RS '+str(RS_number))
    plt.xlim(-50,200)
    plt.show()
    
    heights=[0,0,50,100,100,150,200,200,250,300,300,350,400,400,450,500,500,550,600,600,650,700,700,750,800,800,850,900,900,1000,1000]
    heights_2014diodes=[heights[1],heights[4],heights[7],heights[10],heights[13],\
                        heights[16],heights[19],heights[22],heights[25],heights[28],heights[30]]
    luminosity_peak_2014diodes=[luminosity_peak[1],luminosity_peak[4],luminosity_peak[7],luminosity_peak[10],luminosity_peak[13],\
                        luminosity_peak[16],luminosity_peak[19],luminosity_peak[22],luminosity_peak[25],luminosity_peak[28],luminosity_peak[30]]
    
    plt.figure(figsize=(15.8,10.9))
    plt.subplot(211)
    plt.plot(heights_2014diodes,luminosity_peak_2014diodes,'*-')
    plt.title('2014 APDs')
    plt.xlabel('Channel Height (m)')
    plt.ylabel('Max luminosity peak')
    plt.grid()
    
    heights_2015diodes=[heights[0],heights[2],heights[3],heights[5],heights[6],\
                        heights[8],heights[9],heights[11],heights[12],heights[14],\
                        heights[15],heights[17],heights[18],heights[20],heights[21],\
                        heights[23],heights[24],heights[26],heights[27],heights[29]]
    luminosity_peak_2015diodes=[luminosity_peak[0],luminosity_peak[2],luminosity_peak[3],luminosity_peak[5],luminosity_peak[6],\
                        luminosity_peak[8],luminosity_peak[9],luminosity_peak[11],luminosity_peak[12],luminosity_peak[14],\
                        luminosity_peak[15],luminosity_peak[17],luminosity_peak[18],luminosity_peak[20],luminosity_peak[21],\
                        luminosity_peak[23],luminosity_peak[24],luminosity_peak[26],luminosity_peak[27],luminosity_peak[29]]
    plt.subplot(212)
    plt.plot(heights_2015diodes,luminosity_peak_2015diodes,'r*-')
    plt.title('2015 APDs')
    plt.xlabel('Channel Height (m)')
    plt.ylabel('Max luminosity peak')
    plt.grid()
    plt.show()