# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

__author__ = 'lenz'
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as it

dt=0.1e-6
dz=1
eps0=8.854e-12
mu0=4*(math.pi)*1e-7
H=4e3 #meters
D=2e3 #meters
v=8e7 #m/s
c=1/math.sqrt(mu0*eps0) #m/s
R_max=math.sqrt(H**2+D**2)

t=np.arange(0,25e-6,dt) #time array

I=np.zeros(len(t)) #channel-base
index=1e-6/dt
I[0:index+1]=(10e3/1e-6)*t[0:index+1]
I[index+1:-1]=-(10e3/24e-6)*t[index+1:-1]+(10e3+10e3/24)

Iz=np.zeros((int(H/dz),len(t)+ int((H/v+R_max/c)/dt))) #new time array to account for delays
R=np.zeros(int(H/dz))
theta=np.zeros(int(H/dz))
theta_deg=np.zeros(int(H/dz))

tz=np.arange(0,90e-6-dt,dt) #create new time array
print('tz shape', tz.shape)
print(Iz.shape)

i=np.arange(0,int(H/dz))
R=np.sqrt(i*dz**2+D**2)
theta=np.arcsin(D/R) #rad

for i in range(0,int(H/dz)):
    Iz[i,(i*((dz/v)/dt)+R[i]/c/dt):(i*((dz/v)/dt)+R[i]/c/dt+len(t))]=I #2-D array

print('Iz',Iz.shape)
print('tz',tz.shape)
plt.plot(tz*1e6,Iz[0,:],tz*1e6,Iz[-1,:])
plt.xlabel('Time (μs)')
plt.xlim([0,tz[-1]*1e6])
plt.ylabel('Current Amplitude (A)')
plt.show()

#Time domain derivative
dI=np.zeros(len(t)) #channel-base
dI[0:index+1]=(10e3/1e-6)
dI[index+1:]=-(10e3/24e-6)

dIz=np.zeros((int(H/dz),len(t)+ int((H/v+R_max/c)/dt))) #new time array to account for delays

for i in range(0,int(H/dz)):
    dIz[i,(i*((dz/v)/dt)+R[i]/c/dt):(i*((dz/v)/dt)+R[i]/c/dt+len(t))]=dI #2-D array

plt.plot(tz*1e6,dIz[0,:],tz*1e6,dIz[-1,:])
plt.xlabel('Time (\u03bcs)')
plt.xlim([0,tz[-1]*1e6])
plt.ylabel('dI/dt')
plt.show()    
    
# Induction field

E_ind=np.zeros(len(tz))
E_rad=np.zeros(len(tz))
for j in range(0,len(tz)): #time
    # for i in range(0,int(H/dz)): #height
    y=(2-3*(np.sin(theta)**2)/(c*R**2))*Iz[:,j]
    E_ind[j]=it.simps(y,dx=dt)
    
    y2=((np.sin(theta)**2)/(R*c**2))*dIz[:,j]
    E_rad[j]=it.simps(y2,dx=dt)
    
    y3=(np.sin(theta)/(R**2))*Iz[:,j]
#    B_ind[j]=it.simps(y3,dx=dt)
    
    y4=(np.sin(theta)/(c*R))*dIz[i,:]

plt.plot(tz*1e6,E_rad)
plt.show()


# # # E-Field Calculation
# Ez=np.zeros((int(H/dz),len(t)+ int(H/v/dt)))
# for i in range(0,int(H/dz)): #height
#     Ez[i,:]=(1/(2*(math.pi)*eps0))*(Iz[i,:]**2)
    # Ez[i,:]=it.quad(((2-3*((math.sin(theta))**2))/(c*R*R))*Iz[i,:],0,H)
#
# plt.plot(tz,Ez[1000,:])
# plt.show()
#        # [lambda z,t: ((2-3*((np.sin(theta))**2))/(R**3))*I, 0, H, ]
# #     it.dblquad(lambda z,  (2-3*np.(sin(theta)**2))/(R**3))]
