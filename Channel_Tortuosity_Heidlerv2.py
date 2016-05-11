# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:44:36 2016

@author: lenz
"""

import numpy as np
import matplotlib.pyplot as plt
max=6
for i in range (1,max):
    #Create Channel-base current
    I0=13e3
    eta=0.73
    tau1=-0.2e-6+i*0.4e-6
    tau2=20.7e-6
    n=2
    pad1=np.zeros(1000)
    tf=200e-6
    N=10e3
    pad1=np.zeros(N)
    Ts=tf/N
    fs=1/Ts
    
    t=Ts*np.arange(0,N)
    I=(I0/eta)*(((t/tau1)**n)/((t/tau1)**n+1))*np.exp(-t/tau2) #Channel-base current
    I=np.append(pad1,I)
    I=np.append(I,pad1)
    N=len(I)
    t=np.linspace(0,N*Ts,N)-tf
#    plt.plot(t*1e6,I/1000)
#    plt.xlabel('Time (us)')
#    plt.ylabel('Current (kA)')
#    plt.show
    
    print(t[0])
    print(t[-1])
    
    #Constants
    eps0=8.854e-12
    mu0=4*(np.pi)*1e-7
    H=1e3 #meters
    D=209e3#meters
    c=1/np.sqrt(mu0*eps0) #m/s
    v=c/3
    dz=1 #m
    dt=(t[-1]-t[0])/len(t) #sampling time
    
    #Before reaches top of the wire
#    plt.plot(t*1e6,I)
    pad_Dc=np.zeros((D/c)/dt)
    I_Dc=np.append(pad_Dc,I)
    t=np.linspace(0,len(I_Dc)*dt,len(I_Dc))-tf
#    plt.plot(t*1e6,I_Dc)
#    plt.show
    
    
    Ez_before=(-mu0*v/(np.pi*2*D))*I_Dc
    t=np.linspace(0,len(Ez_before)*dt,len(Ez_before))-tf
    
#    plt.plot(t*1e6,Ez_before)
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.show
    
    #After reaches the top of wire
    pad_Hv_Dc=np.zeros(int((H/v+D/c)/dt))
    I_Hv_Dc=np.append(pad_Hv_Dc,I)
    
    pad_diff=np.zeros(int((H/v)/dt))
    I_Dc=np.append(I_Dc,pad_diff)
    
    Ez_after=(-mu0*v/(np.pi*2*D))*(I_Dc-I_Hv_Dc)
    t=np.linspace(0,len(Ez_after)*dt,len(Ez_after))-tf
#    plt.plot(t*1e6,Ez_after)
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.show
    
    Ez_total=np.append(Ez_before,Ez_after)
#    plt.subplot(211)
    t=np.linspace(0,len(I)*dt,len(I))-tf
#    plt.plot(t*1e6,I/1000)
#    plt.xlabel('Time (us)')
#    plt.ylabel('Channel-base current (kA)')
    
#    plt.subplot(212)
#    t=np.linspace(0,len(Ez_before)*dt,len(Ez_before))-tf
#    plt.plot(t*1e6,Ez_before,label='before reaches the top')
    
#    t=np.linspace(0,len(Ez_after)*dt,len(Ez_after))-tf
#    plt.plot(t*1e6,Ez_after,label='after reaches the top')
    
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.legend()
#    plt.show
    
    ##HORIZONTAL SECTION
    #horizontal wire section is 1 km
    hor_section=100
    hor_delay=hor_section/v
    ##SECOND VERTICAL SECTION
    H2=1e3 #second vertical section 
    
    #Before reaches top of the second wire
#    t=np.linspace(0,len(I)*dt,len(I))-tf
#    plt.plot(t*1e6,I)
    pad_Dc_hor=np.zeros((D/c+hor_delay)/dt)
    I_Dc_hor=np.append(pad_Dc_hor,I)
#    t=np.linspace(0,len(I_Dc_hor)*dt,len(I_Dc_hor))-tf
#    plt.plot(t*1e6,I_Dc_hor)
#    plt.show
    
    
    Ez_before_hor=(-mu0*v/(np.pi*2*D))*I_Dc_hor
    t=np.linspace(0,len(Ez_before_hor)*dt,len(Ez_before_hor))-tf
    
#    plt.plot(t*1e6,Ez_before_hor)
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.show
    
    #After reaches the top of wire
    pad_Hv_Dc_hor=np.zeros(int((H2/v+D/c+hor_delay)/dt))
    I_Hv_Dc_hor=np.append(pad_Hv_Dc_hor,I)
    
    pad_diff=np.zeros(int((H2/v)/dt))
    I_Dc_hor=np.append(I_Dc_hor,pad_diff)
    
    Ez_after_hor=(-mu0*v/(np.pi*2*D))*(I_Dc_hor-I_Hv_Dc_hor)
    t=np.linspace(0,len(Ez_after_hor)*dt,len(Ez_after_hor))-tf
#    plt.plot(t*1e6,Ez_after_hor)
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.show
    
#    plt.subplot(211)
#    t=np.linspace(0,len(I)*dt,len(I))-tf
#    plt.plot(t*1e6,I/1000)
#    plt.xlabel('Time (us)')
#    plt.ylabel('Channel-base current (kA)')
    
#    plt.subplot(212)
#    t=np.linspace(0,len(Ez_before_hor)*dt,len(Ez_before_hor))-tf
#    plt.plot(t*1e6,Ez_before_hor,label='before reaches the top')
#    
#    t=np.linspace(0,len(Ez_after_hor)*dt,len(Ez_after_hor))-tf
#    plt.plot(t*1e6,Ez_after_hor,label='after reaches the top')
#    
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.legend()
#    plt.show
    
#    fig=plt.figure()
#    plt.subplot(211)
#    t=np.linspace(0,len(I)*dt,len(I))-tf
#    plt.plot(t*1e6,I/1000)
#    plt.xlabel('Time (us)')
#    plt.ylabel('Channel-base current (kA)')
    
    d1=20000
    d2=63000
    
#    ax=plt.subplot(212)
    t=np.linspace(0,len(Ez_before)*dt,len(Ez_before))-tf
#    plt.plot(t[d1:d2]*1e6,Ez_before[d1:d2],label='before reaches the first top')
    
    t=np.linspace(0,len(Ez_after)*dt,len(Ez_after))-tf
#    plt.plot(t[d1:d2]*1e6,Ez_after[d1:d2],label='after reaches the first top')
    
    t=np.linspace(0,len(Ez_before_hor)*dt,len(Ez_before_hor))-tf
#    plt.plot(t[d1:d2]*1e6,Ez_before_hor[d1:d2],label='before reaches the second top')
    
    t=np.linspace(0,len(Ez_after_hor)*dt,len(Ez_after_hor))-tf
#    plt.plot(t[d1:d2]*1e6,Ez_after_hor[d1:d2],label='after reaches the second top')
    
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.legend(loc=2)
#    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#    plt.show()
    
#    plt.subplot(211)
#    t=np.linspace(0,len(I)*dt,len(I))-tf
#    plt.plot(t*1e6,I/1000)
#    plt.xlabel('Time (us)')
#    plt.ylabel('Channel-base current (kA)')
    
#    plt.subplot(212)
    t=np.linspace(0,len(Ez_after_hor)*dt,len(Ez_after_hor))-tf
    E_total=Ez_before[d1:d2]-Ez_before_hor[d1:d2]+\
            Ez_after[d1:d2]+Ez_after_hor[d1:d2]
#    plt.plot((t[d1:d2])*1e6,E_total)
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.title('Modeled Ground wave for channel geometry with horizontal section')
#    plt.show()
    
    E1=(mu0*v/(np.pi*2*D))*(I_Dc)
    t=np.linspace(0,len(E1)*dt,len(E1))-tf
#    plt.plot(t*1e6,E1,label='$Kv/D i(t-D/c)$' )
    
    E2=(-mu0*v/(np.pi*2*D))*(I_Hv_Dc)
    t=np.linspace(0,len(E2)*dt,len(E2))-tf
#    plt.plot(t*1e6,E2,label='$Kv/D i(t-D/c-H/v)$' )
    
    E3=(mu0*v/(np.pi*2*D))*(I_Hv_Dc_hor)
    t=np.linspace(0,len(E3)*dt,len(E3))-tf
#    plt.plot(t*1e6,E3,label='$Kv/D i(t-D/c-Hv-x/v)$' )
#    plt.legend(loc=4)
#    plt.xlabel('Time (us)')
#    plt.ylabel('$E_z$ at D=209 km (V/m)')
#    plt.xlim(660,800)
#    
#    plt.show()
    
    plt.subplot(211)
    t=np.linspace(0,len(I)*dt,len(I))-tf
    plt.plot(t*1e6,I/1000)
    plt.xlabel('Time (us)')
    plt.ylabel('Channel-base current (kA)')
    plt.xlim(-37,130)
    
    plt.subplot(212)
    Et=np.zeros((max,d2-d1))
    Et[i]=E1[d1:d2]+E2[d1:d2]+E3[d1:d2]
    t=np.linspace(0,len(E1)*dt,len(E1))-tf
    lab=tau1/1e-6
    plt.plot(t[d1:d2]*1e6,Et[i],label='$ t =%2.1f \mu s$'%lab)
    plt.xlabel('Time (us)')
    plt.ylabel('$E_z$ at D=209 km (V/m)')
    plt.title('Total $E_z$ for different channel-base current risetimes')
    plt.legend()
    plt.xlim(660,800)

plt.show()
