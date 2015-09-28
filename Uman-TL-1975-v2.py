# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:08:20 2015

@author: lenz
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as it

#Constants
eps0=8.854e-12
mu0=4*(math.pi)*1e-7
H=4e3 #meters
D=2e3 #meters
v=8e7 #m/s
c=1/math.sqrt(mu0*eps0) #m/s
R_max=math.sqrt(H**2+D**2)
dt=0.1e-6
dz=1
#arrays
t=np.arange(0,25e-6,dt)
z=np.arange(0,H,dz)

Nt=len(t)
Nz=len(z)

I=np.zeros(Nt) #channel-base
index=1e-6/dt
I[0:index+1]=(10e3/1e-6)*t[0:index+1]
I[index+1:]=-(10e3/24e-6)*t[index+1:]+(10e3+10e3/24) 

max_delayz=H/v;
max_delayD=R_max/c
N_delay=int((max_delayz+max_delayD)/dt)

Iz=np.zeros((Nz, Nt + N_delay)) #new time array to account for delays
print('Iz',Iz.shape)

R=np.zeros(Nz)
theta=np.zeros(Nz)

for i in range(0,Nz):
    Iz[i,(i*((dz/v)/dt)+R[i]/c/dt):(i*((dz/v)/dt)+R[i]/c/dt+Nt)]=I #2-D array

tz=np.arange(0,90e-6-dt,dt)
print('tz',tz.shape)
print('dt',dt)

plt.plot(tz*1e6,Iz[0,:],tz*1e6,Iz[-1,:])
plt.legend(['channel-base','4km'])
plt.xlabel('Time (us)')
plt.xlim([0,tz[-1]*1e6])
plt.ylabel('Current Amplitude (A)')
plt.show()

x2 = lambda z: ((2-3*(np.sin((np.arcsin(D/np.sqrt(z**2+D**2))))**2))/(c*(z**2+D**2)))*
integral=it.quad(x2,0,H)
print(integral)