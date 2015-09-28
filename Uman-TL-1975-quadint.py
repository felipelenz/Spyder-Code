# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:26:31 2015

@author: lenz
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as it

H=4000
dz=1
z=np.arange(0,H,dz)
D=1e3
c=3e8

dt=0.1e-6
t=np.arange(0,90e-6,dt)

Nt=len(t)
Nz=len(z)

I=np.zeros(Nt) #channel-base
index=1e-6/dt
index2=25e-6/dt
I[0:index+1]=(10e3/1e-6)*t[0:index+1]
I[index+1:index2]=-(10e3/24e-6)*t[index+1:index2]+(10e3+10e3/24) 
I[index2+1:]=0
print('Iz',I.shape)
Iz=I(t-2e-6)

plt.plot(t,Iz)
plt.show()
#x2 = lambda z: ((2-3*(np.sin((np.arcsin(D/np.sqrt(z**2+D**2))))**2))/(c*(z**2+D**2)))*Iz
#integral=it.quad(x2,0,H)
#print(integral)