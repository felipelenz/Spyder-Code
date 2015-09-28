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
c=1/math.sqrt(mu0*eps0) #m/sy
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
i=np.arange(0,Nz)
R=np.sqrt(i*dz**2+D**2)
theta=np.arcsin(D/R) #rad

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

#dI/dt
dI=np.gradient(I)

dIz=np.zeros((Nz, Nt + N_delay)) #new time array to account for delays

for i in range(0,Nz):
    dIz[i,(i*((dz/v)/dt)+R[i]/c/dt):(i*((dz/v)/dt)+R[i]/c/dt+Nt)]=dI #2-D array
    
#plt.plot(tz*1e6,dIz[0,:],tz*1e6,dIz[-1,:])
#plt.legend(['channel-base','4km'])
#plt.xlabel('Time (us)')
#plt.xlim([0,tz[-1]*1e6])
#plt.ylabel('dI/dt')
#plt.show()

Ntz=len(tz)
E_ind=np.zeros((Nz, Nt + N_delay))
E_rad=np.zeros((Nz, Nt + N_delay))
E_elec=np.zeros((Nz, Nt + N_delay))
E_elec2=np.zeros((Nz, Nt + N_delay))
E_elec_total=np.zeros((Nz, Nt + N_delay))

E1=np.zeros(Nz)
E2=np.zeros(Nz)
E3=np.zeros(Nz)
E4=np.zeros(Nz)

#
#it.quad
for i in range(0,Ntz): #for each time t, integrate over z
    E1=(2-3*((np.sin(theta))**2))*Iz[:,i]/(c*R*R)
    E_ind[:,i]=(1/(2*eps0*math.pi))*it.simps(E1,dx=dz)
    
    E2=((np.sin(theta))**2)*dIz[:,i]/(c*c*R)       
    E_rad[:,i]=-(1/(2*eps0*math.pi))*it.simps(E2,dx=dz)
        
    E3=Iz[:,i]
    E_elec[:,i]=(1/(2*eps0*math.pi))*it.simps(E3,dx=dz)

    E4=(2-3*((np.sin(theta))**2))/(R**3)
    E_elec_total[:,i]=(1/(2*eps0*math.pi))*it.simps(E4,dx=dz)*it.simps(E3,dx=dt) 
#        
##        for j in range(0,Nz):
##            print('stuck',i,j)
##            E4=(2-3*((np.sin(theta[j]))**2))/(R[j]*R[j]*R[j])
##            E_elec_total[j,i]=(1/(2*eps0*math.pi))*it.simps(E4,dx=dz)   
#        
print('Ntz',Ntz)
print('tz',tz.shape)
print('E_ind',E_ind.shape)
plt.plot(tz*1e6,E_elec_total[2999,:])
plt.show()