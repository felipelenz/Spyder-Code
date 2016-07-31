import lecroy as lc
import numpy as np
import matplotlib.pyplot as plt
def RS_plot_2016_diodes14(date,event,seg,RS_number,suffix):
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
    offset=0
    #Diode 2
    lecroy_fileName_Scope43_APD2 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C1AC0000"+str(suffix43)+".trc"
    scope43_D2 = lc.lecroy_data(lecroy_fileName_Scope43_APD2)
    D2_time = scope43_D2.get_seg_time()
    D2_data = scope43_D2.get_segments()
    D2_data=D2_data[seg]*1.0
    plt.plot((D2_time-5e-3)*1e6,D2_data+offset,label='D2 (0 m)')
    
    offset=offset+np.max(D2_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D2_data))
    
    #Diode 5
    lecroy_fileName_Scope44_APD5 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C2AC0000"+str(suffix44)+".trc"
    scope44_D5 = lc.lecroy_data(lecroy_fileName_Scope44_APD5)
    D5_time = scope44_D5.get_seg_time()
    D5_data = scope44_D5.get_segments()
    D5_data=D5_data[seg]*.82
    
    plt.plot((D5_time-5e-3)*1e6,D5_data+offset,label='D5 (100 m)')
    
    offset=offset+np.max(D5_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D5_data))
    
    #Diode 8
    lecroy_fileName_Scope44_APD8 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C3AC0000"+str(suffix44)+".trc"
    scope44_D8 = lc.lecroy_data(lecroy_fileName_Scope44_APD8)
    D8_time = scope44_D8.get_seg_time()
    D8_data = scope44_D8.get_segments()
    D8_data=D8_data[seg]*.57
    
    plt.plot((D8_time-5e-3)*1e6,D8_data+offset,label='D8 (200 m)')
    
    offset=offset+np.max(D8_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D8_data))
    
    #Diode 11
    lecroy_fileName_Scope48_APD11 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope48/C3AC0000"+str(suffix48)+".trc"
    scope48_D11 = lc.lecroy_data(lecroy_fileName_Scope48_APD11)
    D11_time = scope48_D11.get_seg_time()
    D11_data = scope48_D11.get_segments()
    D11_data=D11_data[seg]*0.81
    
    plt.plot((D11_time-5e-3)*1e6,D11_data+offset,label='D11 (300 m)')
    
    offset=offset+np.max(D11_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D11_data))
    
    #Diode 14
    lecroy_fileName_Scope50_APD14 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope43/C4AC0000"+str(suffix50)+".trc"
    scope50_D14 = lc.lecroy_data(lecroy_fileName_Scope50_APD14)
    D14_time = scope50_D14.get_seg_time()
    D14_data = scope50_D14.get_segments()
    D14_data=D14_data[seg]*1.62
    
    plt.plot((D14_time-5e-3)*1e6,D14_data+offset,label='D14 (400 m)')
    
    offset=offset+np.max(D14_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D14_data))
    
    #Diode 17
    lecroy_fileName_Scope39_APD17 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope39/C1AC0000"+str(suffix39)+".trc"
    scope39_D17 = lc.lecroy_data(lecroy_fileName_Scope39_APD17)
    D17_time = scope39_D17.get_seg_time()
    D17_data = scope39_D17.get_segments()
    D17_data = D17_data[seg]*1.34
    plt.plot((D17_time-5e-3)*1e6,D17_data+offset,label='D17 (500 m)')
    
    offset=offset+np.max(D17_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D17_data))
    
    #Diode 20
    lecroy_fileName_Scope39_APD20 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope39/C4AC0000"+str(suffix39)+".trc"
    scope39_D20 = lc.lecroy_data(lecroy_fileName_Scope39_APD20)
    D20_time = scope39_D20.get_seg_time()
    D20_data = scope39_D20.get_segments()
    D20_data=D20_data[seg]*0.76
    
    plt.plot((D20_time-5e-3)*1e6,D20_data+offset,label='D20 (600 m)')
    
    offset=offset+np.max(D20_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D20_data))
    
    #Diode 23
    lecroy_fileName_Scope42_APD23 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope42/C3AC0000"+str(suffix42)+".trc"
    scope42_D23 = lc.lecroy_data(lecroy_fileName_Scope42_APD23)
    D23_time = scope42_D23.get_seg_time()
    D23_data = scope42_D23.get_segments()
    D23_data=D23_data[seg]*1.54
    
    plt.plot((D23_time-5e-3)*1e6,D23_data+offset,label='D23 (700 m)')
    
    offset=offset+np.max(D23_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D23_data))
    
    #Diode 26
    lecroy_fileName_Scope37_APD26 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope37/C2AC0000"+str(suffix37)+".trc"
    scope37_D26 = lc.lecroy_data(lecroy_fileName_Scope37_APD26)
    D26_time = scope37_D26.get_seg_time()
    D26_data = scope37_D26.get_segments()
    D26_data=D26_data[seg]*1.44
    
    plt.plot((D26_time-5e-3)*1e6,D26_data+offset,label='D26 (800 m)')
    
    offset=offset+np.max(D26_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D26_data))
    
    #Diode 29
    lecroy_fileName_Scope29_APD29 = "/Volumes/Promise 12TB RAID5/2016 Data/0"+str(date)+"/Scope29/C1AC0000"+str(suffix29)+".trc"
    scope29_D29 = lc.lecroy_data(lecroy_fileName_Scope29_APD29)
    D29_time = scope29_D29.get_seg_time()
    D29_data = scope29_D29.get_segments()
    D29_data=D29_data[seg]*1.80
    
    plt.plot((D29_time-5e-3)*1e6,D29_data+offset,label='D29 (900 m)')
    
    offset=offset+np.max(D29_data)
    luminosity_peak=np.append(luminosity_peak,np.max(D29_data))
    
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
    plt.title('Event UF 16-'+str(event)+', RS '+str(RS_number)+' (2014 APDs only)')
#    plt.title('Natural flash July 30, 2016 21:19:41.4600486 UTC (2014 APDs only)')
    plt.xlim(-50,1000)
    plt.show()